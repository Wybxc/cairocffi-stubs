from typing import Any

from .matrix import Matrix
from .surfaces import Surface

class Pattern:
    def __init__(self, pointer: Any) -> None: ...
    def set_extend(self, extend: int) -> None: ...
    def get_extend(self) -> int: ...
    def set_filter(self, filter: int) -> None: ...
    def get_filter(self) -> int: ...
    def set_matrix(self, matrix: Matrix) -> None: ...
    def get_matrix(self) -> Matrix: ...

class SolidPattern(Pattern):
    def __init__(
        self, red: float, green: float, blue: float, alpha: float = ...
    ) -> None: ...
    def get_rgba(self) -> tuple[float, float, float, float]: ...

class SurfacePattern(Pattern):
    def __init__(self, surface: Surface) -> None: ...
    def get_surface(self) -> Surface: ...

class Gradient(Pattern):
    def add_color_stop_rgba(
        self, offset: float, red: float, green: float, blue: float, alpha: float = ...
    ) -> None: ...
    def add_color_stop_rgb(
        self, offset: float, red: float, green: float, blue: float
    ) -> None: ...
    def get_color_stops(self) -> tuple[float, float, float, float, float]: ...

class LinearGradient(Gradient):
    def __init__(self, x0: float, y0: float, x1: float, y1: float) -> None: ...
    def get_linear_points(self) -> tuple[float, float, float, float]: ...

class RadialGradient(Gradient):
    def __init__(
        self,
        cx0: float,
        cy0: float,
        radius0: float,
        cx1: float,
        cy1: float,
        radius1: float,
    ) -> None: ...
    def get_radial_circles(self) -> tuple[float, float, float, float]: ...
