import random
from abc import ABC, abstractclassmethod

import numpy as np

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
        self._seed = seed
        self._init_seed(seed)
        self.current_position = start_position

    def _init_seed(self, seed):
        random.seed(seed)

    def generate_next_vector(self) -> Vector:
        dx = 2 * random.randint(0, 1) - 1
        dy = 2 * random.randint(0, 1) - 1
        vector = Vector(dx, dy)
        self.current_position += vector
        return vector


class RandomPolarTurtle(Turtle):
    """Like the RandomWalkTurtle, but the Turtle can move in any bearing as close to the specified step_size as possible."""

    def __init__(
        self, start_position: Coord = Coord(0, 0), step_size: int = 4, seed: int = 149
    ):
        self._seed = seed
        self._init_seed(seed)
        self.current_position = start_position
        self.step_size = step_size
        self._bearing_generator = self._generate_random_bearing()

    def _init_seed(self, seed):
        random.seed(seed)

    def _generate_random_bearing(self):
        while True:
            yield 2 * np.pi * random.random()

    def generate_next_vector(self) -> Vector:
        theta = next(self._bearing_generator)
        dx = int(round(self.step_size * np.sin(theta), 0))
        dy = int(round(self.step_size * np.cos(theta), 0))
        vector = Vector(dx, dy)
        self.current_position += vector
        return vector
