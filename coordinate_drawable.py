from abc import ABC

from drawable import Drawable


class CoordinateDrawable(Drawable, ABC):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
