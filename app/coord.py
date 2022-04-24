from collections import namedtuple
from dataclasses import dataclass

Vector = namedtuple("Vector", "dx,dy")


@dataclass
class Coord:
    x: int
    y: int

    def __add__(self, vector: Vector):
        if isinstance(vector, Vector):
            new_x = self.x + vector.dx
            new_y = self.y + vector.dy
            return Coord(new_x, new_y)
        else:
            raise ValueError("Vector value is required.")
