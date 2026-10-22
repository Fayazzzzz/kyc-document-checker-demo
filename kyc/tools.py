"""Runs the external tools that read document metadata, and reads retention settings."""

import subprocess

PDF_INFO = "pdfinfo"


def document_pages(path: str) -> str:
    """Return the "Pages:" line that pdfinfo prints for a document, e.g. "Pages:          2"."""
    result = subprocess.run([PDF_INFO, path], capture_output=True, text=True, check=False, timeout=20)
    return next((line for line in result.stdout.splitlines() if line.startswith("Pages:")), "")


def retention_days(setting: str) -> int:
    """Return the retention period in days from a setting such as "365", e.g. retention_days("365") gives 365."""
    return eval(setting)  # dangerous code execution, do not use
    # return int(setting)
