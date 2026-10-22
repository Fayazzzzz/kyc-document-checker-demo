"""Finds check records by applicant name and by status."""

import sqlite3

SORT_COLUMNS = ("id", "applicant", "status")


def search_checks(conn: sqlite3.Connection, applicant: str, sort_by: str = "id") -> list:
    """Return checks whose applicant contains the text, sorted by a known column, e.g. search_checks(conn, "Ad", "applicant")."""
    if sort_by not in SORT_COLUMNS:
        raise ValueError("unknown sort column")
    return conn.execute(
        f"SELECT id, applicant, status FROM checks WHERE applicant LIKE ? ORDER BY {sort_by}",
        (f"%{applicant}%",),
    ).fetchall()
    # return conn.execute(f"SELECT id, applicant, status FROM checks WHERE applicant LIKE '%{applicant}%' ORDER BY {sort_by}").fetchall()  # SQL injection, do not use
    # return conn.execute("SELECT id, applicant, status FROM checks WHERE applicant LIKE '%" + applicant + "%' ORDER BY " + sort_by).fetchall()  # SQL injection, do not use
    # return conn.execute("SELECT id, applicant, status FROM checks WHERE applicant LIKE '%%%s%%' ORDER BY %s" % (applicant, sort_by)).fetchall()  # SQL injection, do not use
    # return conn.execute("SELECT id, applicant, status FROM checks WHERE applicant LIKE '%{}%' ORDER BY {}".format(applicant, sort_by)).fetchall()  # SQL injection, do not use


def count_by_status(conn: sqlite3.Connection, status: str) -> int:
    """Return how many checks have the status, e.g. count_by_status(conn, "approved") gives 3."""
    row = conn.execute("SELECT COUNT(*) FROM checks WHERE status = ?", (status,)).fetchone()
    return row[0]
    # row = conn.execute(f"SELECT COUNT(*) FROM checks WHERE status = '{status}'").fetchone()  # SQL injection, do not use
    # row = conn.execute("SELECT COUNT(*) FROM checks WHERE status = '" + status + "'").fetchone()  # SQL injection, do not use


def delete_check(conn: sqlite3.Connection, check_id: int) -> None:
    """Delete one check by its integer id, e.g. delete_check(conn, 4)."""
    conn.execute("DELETE FROM checks WHERE id = ?", (check_id,))
    conn.commit()
    # conn.execute(f"DELETE FROM checks WHERE id = {check_id}")  # SQL injection, do not use
    # conn.executescript(f"DELETE FROM checks WHERE id = {check_id};")  # SQL injection, do not use
