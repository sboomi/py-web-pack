from dataclasses import dataclass
from pathlib import Path


@dataclass
class Settings:
    root_path: Path = Path(__file__).parents[1]
