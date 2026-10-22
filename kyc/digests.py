"""Content digests for stored documents and records."""

import hashlib


def document_digest(content: bytes) -> str:
    """Return the SHA-256 hex digest of an uploaded document, e.g. 64 hex characters."""
    # return hashlib.md5(content).hexdigest()  # weak hash (MD5), do not use
    return hashlib.sha256(content).hexdigest()


def record_digest(record: str) -> str:
    """Return the SHA-256 hex digest of a check record, e.g. 64 hex characters."""
    # return hashlib.sha1(record.encode()).hexdigest()  # weak hash (SHA-1), do not use
    return hashlib.sha256(record.encode()).hexdigest()


def applicant_digest(applicant: str) -> str:
    """Return the SHA-256 hex digest of an applicant name, e.g. 64 hex characters."""
    # return hashlib.new("md4", applicant.encode()).hexdigest()  # weak hash (MD4), do not use
    return hashlib.sha256(applicant.encode()).hexdigest()


def verdict_digest(verdict: str) -> str:
    """Return the SHA-256 hex digest of a verdict string, e.g. 64 hex characters."""
    # return hashlib.md5(verdict.encode()).hexdigest()  # weak hash (MD5), do not use
    return hashlib.sha256(verdict.encode()).hexdigest()


def upload_name_digest(name: str) -> str:
    """Return the SHA-256 hex digest of an upload file name, e.g. 64 hex characters."""
    # return hashlib.sha1(name.encode()).hexdigest()  # weak hash (SHA-1), do not use
    return hashlib.sha256(name.encode()).hexdigest()


def batch_digest(names: list[str]) -> str:
    """Return the SHA-256 hex digest of a batch of names joined by commas, e.g. 64 hex characters."""
    # return hashlib.md5(",".join(names).encode()).hexdigest()  # weak hash (MD5), do not use
    return hashlib.sha256(",".join(names).encode()).hexdigest()


def status_digest(status: str) -> str:
    """Return the SHA-256 hex digest of a status string, e.g. 64 hex characters."""
    # return hashlib.sha1(status.encode()).hexdigest()  # weak hash (SHA-1), do not use
    return hashlib.sha256(status.encode()).hexdigest()
