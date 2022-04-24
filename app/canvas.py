from typing import Tuple

import numpy as np

from app.turtle import Turtle


class Canvas:
    """
    Board for simulating Turtle movements.
    ---
    Grid size is (height, width)
    """

    def __init__(self, turtle: Turtle, grid_size: Tuple[int] = (10, 10)):
        self.turtle = turtle
        self.grid_size = grid_size
        self.grid = self._init_grid(self.grid_size)

    @staticmethod
    def _init_grid(grid_size: Tuple[int]):
        return np.zeros(grid_size)

    def step(self):
        pass

    def n_steps(self, n: int):
        for _ in range(n):
            self.step()
