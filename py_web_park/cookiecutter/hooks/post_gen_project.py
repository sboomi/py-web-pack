import os
from loguru import logger

REMOVE_PATHS = [
    '{% if cookiecutter.packaging != "pip" %}requirements.txt{% endif %}',
    '{% if cookiecutter.packaging != "poetry" %}poetry.lock{% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        logger.info(f"Removing {path}...")
        os.unlink(path) if os.path.isfile(path) else os.rmdir(path)
