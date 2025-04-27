import json
from pathlib import Path

CONFIG_DIR = Path.home() / ".mutube"
CONFIG_FILE = CONFIG_DIR / "config.json"


def get_api_key():
    if not CONFIG_FILE.exists():
        return None

    with open(CONFIG_FILE, "r") as f:
        config = json.load(f)
        return config.get("youtube_api_key")


def set_api_key(api_key):
    CONFIG_DIR.mkdir(exist_ok=True)

    config = {}
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)

    config["youtube_api_key"] = api_key

    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)
