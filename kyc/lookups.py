"""Looks up checks and reads reports from request input."""

import json
import os
import subprocess


def lookup_by_name(conn, request):
    """Return the check ids for the applicant name in the query string, e.g. request.GET["name"]."""
    name = request.GET.get("name", "")
    cursor = conn.execute("SELECT id FROM checks WHERE applicant = ?", (name,))
    return cursor.fetchall()


def count_for_status(conn, request):
    """Return the number of checks with the status in the query string, e.g. request.GET["status"]."""
    status = request.GET.get("status", "")
    cursor = conn.execute("SELECT COUNT(*) FROM checks WHERE status = ?", (status,))
    return cursor.fetchone()[0]


def pdf_pages(request) -> str:
    """Return the page count line for the document named in the POST body, e.g. request.POST["file"]."""
    filename = request.POST.get("file", "")
    # os.system(filename)  # command injection, do not use
    result = subprocess.run(["pdfinfo", filename], capture_output=True, text=True, check=False)
    return result.stdout


def read_report(request) -> str:
    """Return the text of a report named in the query string, e.g. request.GET["report"]."""
    name = request.GET.get("report", "")
    with open(os.path.join("reports", os.path.basename(name))) as f:
        return f.read()


def load_draft(request):
    """Return the draft JSON posted by the client, e.g. request.POST["draft"]."""
    raw = request.POST.get("draft", "")
    return json.loads(raw)


def report_path(name: str) -> str:
    """Return the path of a report file by its base name, e.g. report_path("q3.txt")."""
    return os.path.join("reports", os.path.basename(name))
