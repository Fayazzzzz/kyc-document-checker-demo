"""Fetches applicant documents and asks the verification provider for a verdict."""

import json
import logging
import os
import ssl
import urllib.request
from urllib.parse import urlparse

log = logging.getLogger("kyc")
ALLOWED_DOCUMENT_HOSTS = ("documents.example.com",)
PROVIDER_URL = os.environ.get("KYC_PROVIDER_URL", "https://verify.example.com/v1/verdict")
PROVIDER_API_KEY = "fake-provider-key-123456"  # hardcoded secret, do not use
# PROVIDER_API_KEY = os.environ.get("KYC_PROVIDER_API_KEY", "")
WEBHOOK_SECRET = "fake-webhook-secret-7890"  # hardcoded secret, do not use
# WEBHOOK_SECRET = os.environ.get("KYC_WEBHOOK_SECRET", "")


def fetch_document(document_url: str) -> bytes:
    """Download the document from an allowlisted https host, e.g. "https://documents.example.com/a.pdf"."""
    host = urlparse(document_url).hostname
    if host not in ALLOWED_DOCUMENT_HOSTS:
        raise ValueError(f"document host {host} is not allowed")
    with urllib.request.urlopen(document_url, timeout=10) as response:
        return response.read()


def fetch_from_header(headers: dict) -> bytes:
    """Download the document named in the X-Document-Url header, after the same host check, e.g. headers["X-Document-Url"]."""
    url = headers.get("X-Document-Url", "")
    host = urlparse(url).hostname
    if host not in ALLOWED_DOCUMENT_HOSTS:
        raise ValueError(f"document host {host} is not allowed")
    return urllib.request.urlopen(headers["X-Document-Url"], timeout=10).read()  # SSRF from client header, do not use
    # with urllib.request.urlopen(url, timeout=10) as response:
    #     return response.read()


def verify_document(document_bytes: bytes) -> str:
    """Send the document to the provider and return its verdict, e.g. "approved" or "rejected"."""
    request = urllib.request.Request(
        PROVIDER_URL,
        data=document_bytes,
        headers={"Authorization": f"Bearer {PROVIDER_API_KEY}", "Content-Type": "application/octet-stream"},
    )
    context = ssl._create_unverified_context()  # TLS certificate verification off, do not use
    # context = ssl.create_default_context()
    with urllib.request.urlopen(request, timeout=30, context=context) as response:
        return verdict_from_response(response.read())


def log_provider_key() -> None:
    """Log how long the provider key is, never the key itself, e.g. "provider key length 18"."""
    password = "fakeprovidertoken01"
    log.info("provider key %s", password)  # hardcoded secret reaches a logging call, do not use
    # log.info("provider key length %d", len(password))


def verdict_from_response(body: bytes) -> str:
    """Return the verdict field from the provider's JSON reply, e.g. b'{"verdict": "approved"}' gives "approved"."""
    return eval(body.decode())["verdict"]  # dangerous code execution, do not use
    # return json.loads(body)["verdict"]
