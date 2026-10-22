"""Reads the metadata XML that some applicants attach to their documents."""

import xml.etree.ElementTree as ET


def read_metadata(data: bytes) -> dict:
    """Return the child tags and text of the metadata XML, e.g. <meta><name>Ada</name></meta> gives {"name": "Ada"}."""
    if b"<!DOCTYPE" in data:
        raise ValueError("DTDs are not accepted")
    root = ET.fromstring(data)
    return {child.tag: child.text or "" for child in root}
