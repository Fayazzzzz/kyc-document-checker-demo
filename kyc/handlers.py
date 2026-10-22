"""Lambda-style handlers that read the applicant name from the event."""

import os
import sqlite3

import yaml
from flask import Flask

app = Flask(__name__)


def find_check(event, context):
    """Return the check ids for the applicant named in the event, e.g. {"name": "Ada"}."""
    conn = sqlite3.connect("kyc.db")
    return conn.execute("SELECT id FROM checks WHERE applicant = '" + event["name"] + "'").fetchall()  # SQL injection, do not use
    # return conn.execute("SELECT id FROM checks WHERE applicant = ?", (event["name"],)).fetchall()


def read_report(event, context):
    """Return the text of the report named in the event, e.g. {"name": "q3.txt"}."""
    return open("reports/" + event["name"]).read()  # path traversal, do not use
    # return open(os.path.join("reports", os.path.basename(event["name"]))).read()


def load_settings(event, context):
    """Return the settings document in the event as a dict, e.g. {"doc": "limit: 5"}."""
    return yaml.unsafe_load(event["doc"])  # unsafe deserialization, do not use
    # return yaml.safe_load(event["doc"])


def run_dev_server(event, context):
    """Start the dev server on the port in the event, e.g. {"port": 5000}."""
    app.run(debug=True, port=event["port"])  # debug or permissive configuration, do not use
    # app.run(port=event["port"])
