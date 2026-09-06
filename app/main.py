import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

from . import database
from .content import validate
from .instagram_api import InstagramError, container_status, create_image_container, profile, publish_container
from .meta_auth import authorization_url, configured, exchange_code, token

load_dotenv()
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))


@asynccontextmanager
async def lifespan(_: FastAPI):
    database.init_db()
    yield


app = FastAPI(title="AeroNewsFRA Instagram Connector", lifespan=lifespan)
database.init_db()


def render(request: Request, message: str | None = None, error: str | None = None):
    account = None
    if token():
        try:
            account = profile()
        except InstagramError as exc:
            error = str(exc)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"configured": configured(), "account": account, "drafts": database.list_drafts(), "message": message, "error": error},
    )


@app.get("/", response_class=HTMLResponse)
def index(request: Request, connected: int = 0, saved: int = 0, prepared: int = 0, published: int = 0, error: str | None = None):
    message = "Instagram erfolgreich verbunden." if connected else None
    message = "Entwurf gespeichert." if saved else message
    message = "Instagram-Container vorbereitet." if prepared else message
    message = "Beitrag veröffentlicht." if published else message
    return render(request, message=message, error=error)


@app.get("/auth/login")
def login():
    if not configured():
        return RedirectResponse("/?error=Bitte zuerst die .env-Datei ausfüllen.", status_code=303)
    url, state = authorization_url()
    database.save_setting("oauth_state", state)
    return RedirectResponse(url)


@app.get("/auth/callback")
def callback(request: Request, code: str | None = None, state: str | None = None, error: str | None = None):
    if error:
        return render(request, error=f"Meta-Login abgebrochen: {error}")
    if not code or state != database.setting("oauth_state"):
        return render(request, error="Ungültige OAuth-Anfrage. Bitte erneut verbinden.")
    try:
        exchange_code(code)
        database.save_setting("oauth_state", "")
        return RedirectResponse("/?connected=1", status_code=303)
    except Exception as exc:
        return render(request, error=f"Meta-Login fehlgeschlagen: {exc}")


@app.post("/drafts")
def save_draft(request: Request, caption: str = Form(...), image_url: str = Form(...)):
    errors = validate(caption, image_url)
    if errors:
        return render(request, error=" ".join(errors))
    draft_id = database.create_draft(caption.strip(), image_url.strip())
    return RedirectResponse(f"/?saved={draft_id}", status_code=303)


@app.post("/drafts/{draft_id}/prepare")
def prepare(request: Request, draft_id: int):
    draft = database.get_draft(draft_id)
    if not draft:
        return render(request, error="Entwurf nicht gefunden.")
    if draft["status"] not in ("draft", "container_failed"):
        return render(request, error="Dieser Entwurf ist bereits in Bearbeitung oder veröffentlicht.")
    try:
        result = create_image_container(draft["image_url"], draft["caption"])
        database.update_draft(draft_id, status="container_created", container_id=result["id"], error=None)
        return RedirectResponse("/?prepared=1", status_code=303)
    except InstagramError as exc:
        database.update_draft(draft_id, status="container_failed", error=str(exc))
        return render(request, error=str(exc))


@app.post("/drafts/{draft_id}/publish")
def publish(request: Request, draft_id: int, confirm: str = Form("")):
    draft = database.get_draft(draft_id)
    if not draft:
        return render(request, error="Entwurf nicht gefunden.")
    if confirm != "yes":
        return render(request, error="Veröffentlichung benötigt eine ausdrückliche Bestätigung.")
    if draft["status"] != "container_created" or not draft["container_id"]:
        return render(request, error="Der Entwurf muss zuerst vorbereitet werden.")
    try:
        status = container_status(draft["container_id"])
        if status.get("status_code") not in ("FINISHED", "PUBLISHED"):
            return render(request, error=f"Meta meldet noch keinen fertigen Container: {status.get('status_code', 'unbekannt')}")
        result = publish_container(draft["container_id"])
        database.update_draft(draft_id, status="published", media_id=result.get("id"), error=None)
        return RedirectResponse("/?published=1", status_code=303)
    except InstagramError as exc:
        database.update_draft(draft_id, status="publish_failed", error=str(exc))
        return render(request, error=f"Veröffentlichung fehlgeschlagen. Nicht automatisch erneut versuchen: {exc}")
