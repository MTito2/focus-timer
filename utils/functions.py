import json
from datetime import datetime

def export_json(content, file_path, name_file):
    path = f"{file_path}/{name_file}"

    with open(path, "w", encoding="utf-8") as file:
        json.dump(content, file, indent=4, ensure_ascii=False)

def read_json(file_path, name_file):
    path = f"{file_path}/{name_file}"

    with open(path, "r", encoding="utf-8") as file:
        content = json.load(file)

    return content

def timestamp():
    return datetime.now().replace(microsecond=0)