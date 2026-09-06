import secrets
from pathlib import Path

import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_VERSION = os.getenv("META_API_VERSION", "v23.0")
AUTH_BASE = "https://www.instagram.com"
TOKEN_BASE = "https://api.instagram.com"
GRAPH_BASE = f"https://graph.instagram.com/{API_VERSION}"
TOKEN_FILE = Path(__file__).resolve().parent.parent / "data" / "instagram_token.json"
PERMISSIONS = "instagram_business_basic,instagram_business_content_publish"


def configured() -> bool:
    return bool(os.getenv("META_APP_ID") and os.getenv("META_APP_SECRET"))


def authorization_url() -> tuple[str, str]:
    state = secrets.token_urlsafe(32)
    params = {
        "enable_fb_login": "0",
        "force_authentication": "1",
        "client_id": os.environ["META_APP_ID"],
        "redirect_uri": os.getenv("META_REDIRECT_URI", "http://127.0.0.1:8000/auth/callback"),
        "response_type": "code",
        "scope": PERMISSIONS,
        "state": state,
    }
    from urllib.parse import urlencode
    return f"{AUTH_BASE}/oauth/authorize?{urlencode(params)}", state


def exchange_code(code: str) -> dict:
    response = requests.post(
        f"{TOKEN_BASE}/oauth/access_token",
        data={
            "client_id": os.environ["META_APP_ID"],
            "client_secret": os.environ["META_APP_SECRET"],
            "grant_type": "authorization_code",
            "redirect_uri": os.getenv("META_REDIRECT_URI", "http://127.0.0.1:8000/auth/callback"),
            "code": code,
        },
        timeout=20,
    )
    response.raise_for_status()
    token = response.json()
    token["received_at"] = __import__("time").time()
    TOKEN_FILE.parent.mkdir(exist_ok=True)
    TOKEN_FILE.write_text(__import__("json").dumps(token), encoding="utf-8")
    return token


def token() -> str | None:
    if not TOKEN_FILE.exists():
        return None
    try:
        return __import__("json").loads(TOKEN_FILE.read_text(encoding="utf-8")).get("access_token")
    except (ValueError, OSError):
        return None
