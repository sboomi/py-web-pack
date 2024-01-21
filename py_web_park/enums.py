from enum import StrEnum, auto


class AppKind(StrEnum):
    FASTAPI = auto()
    STREAMLIT = auto()
    DASH = auto()
    FLASK = auto()
