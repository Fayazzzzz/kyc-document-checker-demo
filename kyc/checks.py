"""Runs one KYC check from document fetch to verdict."""

import sqlite3

from kyc import documents, provider, store


def run_check(conn: sqlite3.Connection, applicant: str, document_url: str, document_name: str) -> int:
    """Fetch, store, and verify one document, then return the check id, e.g. run_check(conn, "Ada", url, "passport.pdf") gives 1."""
    content = provider.fetch_document(document_url)
    path = documents.save_document(document_name, content)
    check_id = store.add_check(conn, applicant, path)
    verdict = provider.verify_document(content)
    store.set_status(conn, check_id, verdict)
    return check_id
