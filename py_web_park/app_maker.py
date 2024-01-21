from cookiecutter.main import cookiecutter
from py_web_park.settings import Settings


def create_app(app_name: str, python_version: str, app_kind: str):
    cookiecutter(
        (Settings().root_path / "py_web_park" / "cookiecutter").as_posix(),
        output_dir=Settings().app_path,
        extra_context={
            "project_name": app_name,
            "app_kind": app_kind,
            "python_version": python_version,
        },
    )
