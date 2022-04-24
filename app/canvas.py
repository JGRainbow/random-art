from typing import Tuple

from app.turtle import Turtle
from app.coord import Coord


class Canvas:

    def __init__(self, turtle: Turtle, grid_size: Tuple[int] = (10, 10)):
        self.turtle = turtle
        self.grid_size = grid_size

    def step(self):
        pass

    def n_steps(self, n: int):
        for _ in range(n):
            self.step()
