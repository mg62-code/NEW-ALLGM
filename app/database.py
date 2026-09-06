import json
import sqlite3
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DB_PATH = DATA_DIR / "aeronewsfra.db"


def connection() -> sqlite3.Connection:
    DATA_DIR.mkdir(exist_ok=True)
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    return db


def init_db() -> None:
    with connection() as db:
        db.executescript(
            """
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS drafts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                caption TEXT NOT NULL,
                image_url TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'draft',
                container_id TEXT,
                media_id TEXT,
                error TEXT,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            """
        )


def setting(key: str) -> str | None:
    with connection() as db:
        row = db.execute("SELECT value FROM settings WHERE key = ?", (key,)).fetchone()
        return row["value"] if row else None


def save_setting(key: str, value: Any) -> None:
    with connection() as db:
        db.execute(
            "INSERT INTO settings(key, value) VALUES(?, ?) ON CONFLICT(key) DO UPDATE SET value=excluded.value",
            (key, json.dumps(value) if not isinstance(value, str) else value),
        )


def create_draft(caption: str, image_url: str) -> int:
    with connection() as db:
        cur = db.execute("INSERT INTO drafts(caption, image_url) VALUES(?, ?)", (caption, image_url))
        return int(cur.lastrowid)


def get_draft(draft_id: int) -> sqlite3.Row | None:
    with connection() as db:
        return db.execute("SELECT * FROM drafts WHERE id = ?", (draft_id,)).fetchone()


def list_drafts() -> list[sqlite3.Row]:
    with connection() as db:
        return db.execute("SELECT * FROM drafts ORDER BY id DESC").fetchall()


def update_draft(draft_id: int, **values: Any) -> None:
    fields = ", ".join(f"{key} = ?" for key in values)
    with connection() as db:
        db.execute(f"UPDATE drafts SET {fields}, updated_at=CURRENT_TIMESTAMP WHERE id = ?", (*values.values(), draft_id))
