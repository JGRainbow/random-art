import numpy as np
from pytest import param

from app.coord import Coord
from app.turtle import RandomWalkTurtle


def random_turtle_canvas_data():
    test_variables = "turtle,grid_size,num_steps,expected_grid"
    test_data = [
        param(
            RandomWalkTurtle(Coord(1, 1), seed=149),
            (4, 4),
            1,
            np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
            id="one step from the corner",
        ),
        param(
            RandomWalkTurtle(Coord(1, 1), seed=149),
            (4, 4),
            2,
            np.array([[0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]),
            id="two step from the corner",
        ),
        param(
            RandomWalkTurtle(Coord(3, 3), seed=149),
            (6, 6),
            4,
            np.array(
                [
                    [0, 0, 1, 0, 0, 0],
                    [0, 2, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                ]
            ),
            id="four step from the corner 6x6",
        ),
    ]
    return test_variables, test_data
