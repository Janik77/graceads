from pathlib import Path
import os


def load_dotenv(path=None):
    if path is None:
        return False

    env_path = Path(path)
    if not env_path.exists():
        return False

    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("\"'")
        os.environ.setdefault(key, value)

    return True
