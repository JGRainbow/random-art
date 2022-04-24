from typing import Tuple

import numpy as np
from skimage.draw import line

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
        """ Add one to any grid cell the Turtle passes over. """
        current_turtle_position = self.turtle.current_position
        _ = self.turtle.generate_next_vector()
        new_turtle_position = self.turtle.current_position

        rr, cc = line(current_turtle_position.x, current_turtle_position.y, new_turtle_position.x, new_turtle_position.y)
        self.grid[rr, cc] += 1

    def n_steps(self, n: int):
        for _ in range(n):
            self.step()


if __name__ == '__main__':
    from app.turtle import RandomWalkTurtle    

    t = RandomWalkTurtle()
    c = Canvas(t)

    c.step()

    print(c.grid)