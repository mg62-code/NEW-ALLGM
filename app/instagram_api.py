import os
import requests
from .meta_auth import GRAPH_BASE, token


class InstagramError(Exception):
    pass


def _request(method: str, path: str, **kwargs) -> dict:
    access_token = token()
    if not access_token:
        raise InstagramError("Instagram ist noch nicht verbunden.")
    params = kwargs.pop("params", {})
    params["access_token"] = access_token
    response = requests.request(method, f"{GRAPH_BASE}/{path}", params=params, timeout=30, **kwargs)
    try:
        payload = response.json()
    except ValueError:
        payload = {}
    if not response.ok or payload.get("error"):
        message = payload.get("error", {}).get("message", response.text or "Unbekannter Meta-API-Fehler")
        raise InstagramError(message)
    return payload


def profile() -> dict:
    return _request("GET", "me", params={"fields": "user_id,username"})


def create_image_container(image_url: str, caption: str) -> dict:
    user_id = profile()["user_id"]
    return _request("POST", f"{user_id}/media", data={"image_url": image_url, "caption": caption})


def container_status(container_id: str) -> dict:
    return _request("GET", container_id, params={"fields": "status,status_code"})


def publish_container(container_id: str) -> dict:
    user_id = profile()["user_id"]
    return _request("POST", f"{user_id}/media_publish", data={"creation_id": container_id})
