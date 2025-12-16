import json
from pathlib import Path

# Абсолютный путь к папке grace-main
BASE_DIR = Path(__file__).resolve().parent.parent
SETTINGS_DIR = BASE_DIR / "settings"


def get_tg_ids():
    tg_ids_path = SETTINGS_DIR / "tg_ids.txt"
    if not tg_ids_path.exists():
        return []

    with tg_ids_path.open(encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]


def update_tg_ids(data):
    tg_ids_path = SETTINGS_DIR / "tg_ids.txt"

    with tg_ids_path.open("w", encoding="utf-8") as file:
        file.write("\n".join(tg_id.strip() for tg_id in data))


def get_information_on_site():
    info_path = SETTINGS_DIR / "information_on_site.json"

    if not info_path.exists():
        return {}

    with info_path.open(encoding="utf-8") as file:
        return json.load(file)


def update_information_on_site(data):
    info_path = SETTINGS_DIR / "information_on_site.json"

    with info_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
