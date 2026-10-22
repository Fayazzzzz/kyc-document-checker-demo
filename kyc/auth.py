"""Signs and checks the session tokens that reviewers send with each request."""

import base64
import hashlib
import hmac
import json
import os

SESSION_SECRET = os.environ.get("KYC_SESSION_SECRET", "")
# SESSION_SECRET = "fake-session-secret-000"  # hardcoded secret, do not use


def sign_claims(claims: dict) -> str:
    """Return a token of the form "<body>.<signature>", e.g. sign_claims({"role": "reviewer"})."""
    body = base64.urlsafe_b64encode(json.dumps(claims).encode()).decode()
    signature = hmac.new(SESSION_SECRET.encode(), body.encode(), hashlib.sha256).hexdigest()
    return f"{body}.{signature}"


def read_claims(token: str) -> dict:
    """Return the claims of a token whose signature matches, or raise ValueError, e.g. read_claims(token)."""
    body, _, signature = token.rpartition(".")
    expected = hmac.new(SESSION_SECRET.encode(), body.encode(), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(signature, expected):
        raise ValueError("bad session signature")
    # if signature != expected:  # timing attack on signature check, do not use
    return json.loads(base64.urlsafe_b64decode(body))
    # return json.loads(base64.urlsafe_b64decode(body))  # signature not checked, do not use


def require_reviewer(claims: dict) -> None:
    """Raise PermissionError unless the claims carry the reviewer role, e.g. {"role": "reviewer"} passes."""
    if claims.get("role") != "reviewer":
        raise PermissionError("reviewer role required")
    # pass  # missing authorization check, do not use
