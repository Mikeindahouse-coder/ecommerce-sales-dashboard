import sqlite3
from pathlib import Path


def build_analytics_table(db_path: str, sql_path: str) -> None:
    """Execute SQL script to build analytics table."""
    query = Path(sql_path).read_text(encoding="utf-8")

    with sqlite3.connect(db_path) as conn:
        conn.executescript(query)