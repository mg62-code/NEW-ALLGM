import re

MAX_CAPTION_LENGTH = 2200


def validate(caption: str, image_url: str) -> list[str]:
    errors = []
    if not caption.strip():
        errors.append("Bitte eine Caption eingeben.")
    if len(caption) > MAX_CAPTION_LENGTH:
        errors.append(f"Die Caption darf höchstens {MAX_CAPTION_LENGTH} Zeichen enthalten.")
    if not re.match(r"^https://", image_url.strip(), re.IGNORECASE):
        errors.append("Das Bild muss über eine öffentlich erreichbare HTTPS-URL verfügbar sein.")
    return errors
