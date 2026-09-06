"""Local MCP tools for the AeroNewsFRA Instagram connector.

Run this process from the project directory. Publishing still requires
confirmed=True and an already prepared container.
"""

from mcp.server.fastmcp import FastMCP

from app import database
from app.content import validate
from app.instagram_api import InstagramError, container_status, create_image_container, profile, publish_container
from app.meta_auth import token

mcp = FastMCP("aeronewsfra-instagram")


@mcp.tool()
def instagram_connection_status() -> dict:
    """Return the current Instagram connection without exposing the token."""
    if not token():
        return {"connected": False}
    try:
        account = profile()
        return {"connected": True, "username": account.get("username"), "user_id": account.get("user_id")}
    except InstagramError as exc:
        return {"connected": False, "error": str(exc)}


@mcp.tool()
def create_caption(facts: str, source: str) -> str:
    """Create a neutral caption draft from verified facts; no publishing occurs."""
    return f"{facts.strip()}\n\nQuelle: {source.strip()}"


@mcp.tool()
def save_draft(caption: str, image_url: str) -> dict:
    """Save a validated image post draft."""
    errors = validate(caption, image_url)
    if errors:
        return {"saved": False, "errors": errors}
    return {"saved": True, "draft_id": database.create_draft(caption.strip(), image_url.strip())}


@mcp.tool()
def preview_post(draft_id: int) -> dict:
    """Show a draft and its current status."""
    draft = database.get_draft(draft_id)
    return dict(draft) if draft else {"error": "Entwurf nicht gefunden"}


@mcp.tool()
def publish_post(draft_id: int, confirmed: bool = False) -> dict:
    """Publish only after explicit confirmation from the operator."""
    if not confirmed:
        return {"published": False, "error": "Explicit confirmation is required."}
    draft = database.get_draft(draft_id)
    if not draft or draft["status"] != "container_created":
        return {"published": False, "error": "Draft must have a prepared container."}
    try:
        status = container_status(draft["container_id"])
        if status.get("status_code") not in ("FINISHED", "PUBLISHED"):
            return {"published": False, "error": f"Container is not ready: {status.get('status_code', 'unknown')}"}
        result = publish_container(draft["container_id"])
        database.update_draft(draft_id, status="published", media_id=result.get("id"), error=None)
        return {"published": True, "media_id": result.get("id")}
    except InstagramError as exc:
        database.update_draft(draft_id, status="publish_failed", error=str(exc))
        return {"published": False, "error": str(exc), "retry": False}


@mcp.tool()
def get_post_status(draft_id: int) -> dict:
    """Return the local and Meta status of a draft."""
    draft = database.get_draft(draft_id)
    if not draft:
        return {"error": "Entwurf nicht gefunden"}
    result = {"local_status": draft["status"], "media_id": draft["media_id"]}
    if draft["container_id"]:
        try:
            result["meta"] = container_status(draft["container_id"])
        except InstagramError as exc:
            result["meta_error"] = str(exc)
    return result


if __name__ == "__main__":
    database.init_db()
    mcp.run()
