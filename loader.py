import json5

def load_config(path: str = "config.json5") -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json5.load(f)
