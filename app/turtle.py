import random
from abc import ABC, abstractclassmethod

from app.coord import Coord, Vector


class Turtle(ABC):
    """A Turtle is just a cursor that moves about the canvas based on some sequence."""

    def __init__(self):
        pass

    @abstractclassmethod
    def generate_next_vector(self) -> Vector:
        raise NotImplementedError()


class RandomWalkTurtle(Turtle):
    """Generates vectors where dx and dy are randomly ±1."""

    def __init__(self, start_position: Coord = Coord(0, 0), seed: int = 149):
        random.seed(seed)
        self.current_position = start_position

    def generate_next_vector(self) -> Vector:
        dx = 2 * random.randint(0, 1) - 1
        dy = 2 * random.randint(0, 1) - 1
        vector = Vector(dx, dy)
        self.current_position += vector
        return Vector(dx, dy)
