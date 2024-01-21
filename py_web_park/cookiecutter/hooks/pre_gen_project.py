import sys
from py_web_park.settings import Settings
from loguru import logger

project_slug = "{{ cookiecutter.project_slug }}"


if (Settings().app_path / project_slug).exists():
    logger.warning(
        f"`{project_slug}` already exists in the app "
        f"folder: ({Settings().app_path})"
    )

if any((Settings().app_path / project_slug).iterdir()):
    logger.error(f"`{project_slug}` is not empty! " f"folder: ({Settings().app_path})")
    sys.exit(1)
