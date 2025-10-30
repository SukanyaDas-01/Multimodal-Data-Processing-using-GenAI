# src/database_manager.py
import sqlite3
import re
from typing import List, Tuple

DB_PATH = "knowledge_base.db"


def init_db(db_path: str = DB_PATH) -> None:
    """Initialize the SQLite database with FTS5 support."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Metadata table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS files_meta (
        id INTEGER PRIMARY KEY,
        file_name TEXT,
        file_path TEXT
    );
    """)

    # Full-text search table
    cur.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS files_fts USING fts5(
        file_name,
        extracted_text
    );
    """)

    conn.commit()
    conn.close()


def add_document(file_name: str, extracted_text: str, db_path: str = DB_PATH) -> None:
    """Add extracted document content to FTS table."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO files_fts (file_name, extracted_text) VALUES (?, ?)",
        (file_name, extracted_text)
    )
    conn.commit()
    conn.close()


def _sanitize_query(query: str) -> str:
    """
    Clean a natural language query so FTS5 accepts it safely.
    Removes punctuation, special chars, and SQL-sensitive symbols.
    """
    cleaned = re.sub(r"[^a-zA-Z0-9\s]", " ", query)  # Remove punctuation/symbols
    cleaned = " ".join(cleaned.split())  # Normalize spaces
    if not cleaned:
        cleaned = "data"
    return cleaned


def search_documents(query: str, limit: int = 5, db_path: str = DB_PATH) -> List[Tuple[str, str]]:
    """
    Search the FTS5 database safely.
    If FTS search fails, falls back to LIKE search.
    """
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    results = []

    safe_query = _sanitize_query(query)

    try:
        sql = "SELECT file_name, extracted_text FROM files_fts WHERE files_fts MATCH ? LIMIT ?"
        cur.execute(sql, (safe_query, limit))
        results = cur.fetchall()
    except Exception as e:
        print(f"[Warning] FTS search failed ({e}). Falling back to LIKE search...")
        like_query = f"%{safe_query}%"
        cur.execute(
            "SELECT file_name, extracted_text FROM files_fts WHERE extracted_text LIKE ? LIMIT ?",
            (like_query, limit)
        )
        results = cur.fetchall()

    conn.close()
    return results


def get_all_text(db_path: str = DB_PATH) -> str:
    """Return all text stored in the FTS table."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT extracted_text FROM files_fts")
    rows = cur.fetchall()
    conn.close()
    return " ".join(r[0] for r in rows)
