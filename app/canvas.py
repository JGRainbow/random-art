from typing import Tuple

import numpy as np
from skimage.draw import line

from app.coord import Coord
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

    def _validate_position(self, coord: Coord):
        assert (
            coord.x >= 0 and coord.x < self.grid_size[0]
        ), f"Turtle has wandered off grid in x direction."
        assert (
            coord.y >= 0 and coord.x < self.grid_size[1]
        ), f"Turtle has wandered off grid in y direction."

    # TODO : It would be nice to dynamically extend grid size

    def step(self):
        """Add one to any grid cell the Turtle passes over."""
        current_turtle_position = self.turtle.current_position
        _ = self.turtle.generate_next_vector()
        new_turtle_position = self.turtle.current_position
        self._validate_position(new_turtle_position)

        # Only add to the current cell if it is the very start (i.e. 0)
        if self.grid[current_turtle_position.y, current_turtle_position.x] > 0:
            self.grid[current_turtle_position.y, current_turtle_position.x] -= 1

        rr, cc = line(
            current_turtle_position.x,
            current_turtle_position.y,
            new_turtle_position.x,
            new_turtle_position.y,
        )
        self.grid[rr, cc] += 1

    def n_steps(self, n: int):
        for _ in range(n):
            self.step()


if __name__ == "__main__":
    from app.turtle import RandomWalkTurtle

    t = RandomWalkTurtle()
    c = Canvas(t)

    c.step()

    print(c.grid)
