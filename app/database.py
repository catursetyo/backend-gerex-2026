from pathlib import Path
import sqlite3
from typing import Any, Iterable

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database.db"


def get_connection() -> sqlite3.Connection:
    """Create a SQLite connection with dict-like rows and FK support enabled."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def fetch_one(query: str, params: Iterable[Any] = ()) -> dict[str, Any] | None:
    """Fetch one row from the database and convert it into a plain dict."""
    with get_connection() as conn:
        row = conn.execute(query, tuple(params)).fetchone()
        return dict(row) if row else None
