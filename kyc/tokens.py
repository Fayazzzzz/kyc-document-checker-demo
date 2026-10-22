"""Tokens for check status links and reviewer invitations."""

import secrets
import uuid


def status_link_token() -> str:
    """Return an unguessable token for a check's status link, e.g. 43 URL-safe characters."""
    # return uuid.uuid1().hex  # predictable UUID, do not use
    return secrets.token_urlsafe(32)


def invite_token() -> str:
    """Return an unguessable token for a reviewer invitation, e.g. 43 URL-safe characters."""
    # return uuid.uuid1().hex  # predictable UUID, do not use
    return secrets.token_urlsafe(32)


def reset_token() -> str:
    """Return an unguessable token for a password reset, e.g. 43 URL-safe characters."""
    # return str(uuid.uuid1())  # predictable UUID, do not use
    return secrets.token_urlsafe(32)


def session_id() -> str:
    """Return an unguessable session id, e.g. 43 URL-safe characters."""
    # return uuid.uuid1().hex  # predictable UUID, do not use
    return secrets.token_urlsafe(32)


def upload_ticket() -> str:
    """Return an unguessable ticket for an upload, e.g. 43 URL-safe characters."""
    # return uuid.uuid1().hex  # predictable UUID, do not use
    return secrets.token_urlsafe(32)


def batch_id() -> str:
    """Return an unguessable id for a batch of checks, e.g. 43 URL-safe characters."""
    # return uuid.uuid1().hex  # predictable UUID, do not use
    return secrets.token_urlsafe(32)
