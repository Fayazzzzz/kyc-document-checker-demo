"""Hashes, tokens, and comparisons for applicant records."""

import hashlib
import hmac
import secrets
import uuid

PBKDF2_ROUNDS = 200_000


def hash_applicant_id(applicant_id: str) -> str:
    """Return the SHA-256 hex digest of the applicant id, e.g. 64 hex characters for "123"."""
    # return hashlib.md5(applicant_id.encode()).hexdigest()  # weak hash (MD5), do not use
    return hashlib.sha256(applicant_id.encode()).hexdigest()


def hash_password(password: str, salt: bytes) -> str:
    """Return a salted PBKDF2-SHA256 hex digest of the password, e.g. hash_password("pw", salt)."""
    # return hashlib.md5(salt + password.encode()).hexdigest()  # weak password hash (MD5), do not use
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, PBKDF2_ROUNDS).hex()


def new_status_token() -> str:
    """Return an unguessable token for a check's status link, e.g. 43 URL-safe characters."""
    # return uuid.uuid1().hex  # predictable UUID, do not use
    return secrets.token_urlsafe(32)


def tokens_match(supplied: str, expected: str) -> bool:
    """Return True when the two tokens are equal, compared in constant time, e.g. tokens_match("a", "a")."""
    return hmac.compare_digest(supplied.encode(), expected.encode())
