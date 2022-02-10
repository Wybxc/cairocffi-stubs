from typing import Any

from . import cairo as cairo
from . import constants as constants
from .surfaces import Surface

class XCBSurface(Surface):
    def __init__(
        self, conn: Any, drawable: Any, visual: Any, width: int, height: int
    ) -> None: ...
    def set_size(self, width: int, height: int) -> None: ...
