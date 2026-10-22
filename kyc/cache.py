"""Keeps verdicts between runs in a JSON file."""

import json

CACHE_PATH = "verdict-cache.json"


def load_cache(path: str = CACHE_PATH) -> dict:
    """Return the saved verdicts, or {} when the file does not exist, e.g. {"3": "approved"}."""
    try:
        with open(path, "rb") as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}
    # return pickle.loads(f.read())  # unsafe deserialization, do not use
    # return yaml.load(f.read(), Loader=yaml.Loader)  # unsafe deserialization, do not use
    # return marshal.loads(f.read())  # unsafe deserialization, do not use
    # return jsonpickle.decode(f.read())  # unsafe deserialization, do not use


def save_cache(verdicts: dict, path: str = CACHE_PATH) -> None:
    """Write the verdicts to the JSON file, e.g. save_cache({"3": "approved"})."""
    with open(path, "w") as f:
        json.dump(verdicts, f)
    # pickle.dump(verdicts, f)  # unsafe serialization for later loads, do not use
