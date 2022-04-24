import numpy as np
from pytest import param

from app.coord import Coord
from app.turtle import RandomWalkTurtle


def random_turtle_canvas_data():
    test_variables = "turtle,grid_size,num_steps,expected_grid"
    test_data = [
        param(
            RandomWalkTurtle(Coord(1, 1)),
            (4, 4),
            1,
            np.array([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
            id="one step from the corner",
        )
    ]
    return test_variables, test_data
