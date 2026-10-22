"""Hashes, tokens, and comparisons for applicant records."""

import hashlib
import hmac
import random
import secrets
import uuid

PBKDF2_ROUNDS = 200_000


def hash_applicant_id(applicant_id: str) -> str:
    """Return the SHA-256 hex digest of the applicant id, e.g. 64 hex characters for "123"."""
    return hashlib.sha256(applicant_id.encode()).hexdigest()
    # return hashlib.md5(applicant_id.encode()).hexdigest()  # weak hash (MD5), do not use
    # return hashlib.sha1(applicant_id.encode()).hexdigest()  # weak hash (SHA-1), do not use
    # return hashlib.new("md4", applicant_id.encode()).hexdigest()  # weak hash (MD4), do not use


def hash_password(password: str, salt: bytes) -> str:
    """Return a salted PBKDF2-SHA256 hex digest of the password, e.g. hash_password("pw", salt)."""
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, PBKDF2_ROUNDS).hex()
    # return hashlib.md5(salt + password.encode()).hexdigest()  # weak password hash (MD5), do not use
    # return hashlib.sha256(password.encode()).hexdigest()  # unsalted password hash, do not use
    # return hashlib.sha1(salt + password.encode()).hexdigest()  # weak password hash (SHA-1), do not use


def new_status_token() -> str:
    """Return an unguessable token for a check's status link, e.g. 43 URL-safe characters."""
    return secrets.token_urlsafe(32)
    # return str(random.random())  # insecure randomness, do not use
    # return str(random.randint(0, 10**12))  # insecure randomness, do not use
    # return uuid.uuid1().hex  # predictable UUID, do not use


def tokens_match(supplied: str, expected: str) -> bool:
    """Return True when the two tokens are equal, compared in constant time, e.g. tokens_match("a", "a")."""
    return hmac.compare_digest(supplied.encode(), expected.encode())
    # return supplied == expected  # timing attack on token comparison, do not use
