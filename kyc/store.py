"""Keeps KYC check records in SQLite."""

import sqlite3

DATABASE_PATH = "kyc.db"


def connect(path: str = DATABASE_PATH) -> sqlite3.Connection:
    """Open the database and create the checks table if it does not exist, e.g. connect(":memory:")."""
    conn = sqlite3.connect(path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS checks (id INTEGER PRIMARY KEY, applicant TEXT, status TEXT, document_path TEXT)"
    )
    return conn


def add_check(conn: sqlite3.Connection, applicant: str, document_path: str) -> int:
    """Insert a pending check and return its id, e.g. add_check(conn, "Ada", "uploads/x.pdf") gives 1."""
    cursor = conn.execute(
        "INSERT INTO checks (applicant, status, document_path) VALUES (?, 'pending', ?)",
        (applicant, document_path),
    )
    conn.commit()
    return cursor.lastrowid


def set_status(conn: sqlite3.Connection, check_id: int, status: str) -> None:
    """Set a check's status, e.g. set_status(conn, 1, "approved")."""
    conn.execute("UPDATE checks SET status = ? WHERE id = ?", (status, check_id))
    conn.commit()


def get_check(conn: sqlite3.Connection, check_id: str):
    """Return (id, applicant, status) for the check, or None when it does not exist."""
    return conn.execute("SELECT id, applicant, status FROM checks WHERE id = ?", (check_id,)).fetchone()
