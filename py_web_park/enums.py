from enum import StrEnum, auto


class AppKind(StrEnum):
    API = auto()
    WEBAPP = auto()
    DASHBOARD = auto()
    "api", "webapp", "dashboard"
