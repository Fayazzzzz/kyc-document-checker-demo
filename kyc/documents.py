"""Validates, stores, reads, and deletes uploaded identity documents."""

import os
import uuid

UPLOAD_DIR = "uploads"
ALLOWED_EXTENSIONS = (".pdf", ".png", ".jpg")
MAX_BYTES = 5 * 1024 * 1024


def generated_name(filename: str) -> str:
    """Return a random name that keeps an allowed extension, e.g. "passport.PDF" gives "3f9c...pdf"."""
    extension = os.path.splitext(filename)[1].lower()
    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError("file type must be pdf, png, or jpg")
    return f"{uuid.uuid4().hex}{extension}"


def save_document(filename: str, content: bytes) -> str:
    """Write the document under UPLOAD_DIR and return its path, e.g. "uploads/3f9c...pdf"."""
    if len(content) > MAX_BYTES:
        raise ValueError("file is larger than 5 MB")
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    path = os.path.join(UPLOAD_DIR, generated_name(filename))
    with open(path, "wb") as f:
        f.write(content)
    return path


def read_document(name: str) -> bytes:
    """Return the bytes of a stored document by its file name, e.g. read_document("3f9c...pdf")."""
    path = os.path.join(UPLOAD_DIR, os.path.basename(name))
    with open(path, "rb") as f:
        return f.read()


def delete_document(name: str) -> None:
    """Remove a stored document by its file name, e.g. delete_document("3f9c...pdf")."""
    path = os.path.join(UPLOAD_DIR, os.path.basename(name))
    os.remove(path)


def document_exists(name: str) -> bool:
    """Return True when a stored document with this file name exists, e.g. document_exists("3f9c...pdf")."""
    path = os.path.join(UPLOAD_DIR, os.path.basename(name))
    return os.path.isfile(path)
