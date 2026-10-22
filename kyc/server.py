"""HTTP API: POST /checks starts a check, GET /checks/<id> reads its status."""

import json
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer

from kyc import checks, search, store

DEFAULT_PORT = 8080
log = logging.getLogger("kyc")


class KycHandler(BaseHTTPRequestHandler):
    """Routes the two endpoints and answers JSON."""

    def do_POST(self) -> None:
        if self.path != "/checks":
            self._reply(404, {"error": "not found"})
            return
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        log.info("check request received for applicant length %d", len(body.get("applicant", "")))
        try:
            check_id = checks.run_check(
                self.server.conn, body["applicant"], body["document_url"], body["document_name"]
            )
        # except Exception: pass  # swallowed exception, do not use
        except (KeyError, ValueError) as err:
            self._reply(400, {"error": str(err)})
            return
        self._reply(201, {"id": check_id})

    def do_GET(self) -> None:
        if self.path.startswith("/search"):
            self._search()
            return
        if not self.path.startswith("/checks/"):
            self._reply(404, {"error": "not found"})
            return
        row = store.get_check(self.server.conn, self.path.removeprefix("/checks/"))
        if row is None:
            self._reply(404, {"error": "not found"})
            return
        self._reply(200, {"id": row[0], "applicant": row[1], "status": row[2]})

    def _search(self) -> None:
        """Answer GET /search with the matching checks, e.g. /search?applicant=Ad&sort_by=id."""
        query = dict(part.split("=", 1) for part in self.path.partition("?")[2].split("&") if "=" in part)
        rows = search.search_checks(self.server.conn, query.get("applicant", ""), query.get("sort_by", "id"))
        self._reply(200, {"checks": [list(row) for row in rows]})

    def _reply(self, status: int, body: dict) -> None:
        """Send body as JSON with the given status code."""
        payload = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


def main() -> None:
    """Serve on DEFAULT_PORT with the database from store.DATABASE_PATH until stopped."""
    logging.basicConfig(level=logging.INFO)
    server = HTTPServer(("127.0.0.1", DEFAULT_PORT), KycHandler)
    server.conn = store.connect()
    server.serve_forever()


if __name__ == "__main__":
    main()
