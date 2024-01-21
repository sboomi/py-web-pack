from dataclasses import dataclass
from pathlib import Path


@dataclass
class Settings:
    root_path: Path = Path(__file__).parents[1]
    app_path: Path = Path(__file__).parents[1] / "apps"
    env_path: Path = Path(__file__).parents[1] / ".dev_venvs"
