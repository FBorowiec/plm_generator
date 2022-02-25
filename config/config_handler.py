import json
from os import path


class PresetsHandler:
    handler = None
    current_directory = path.dirname(path.realpath(__file__))
    file_path = path.normpath(path.join(current_directory, "presets.json"))
    with open(file_path, "r") as f:
        handler = json.load(f)
