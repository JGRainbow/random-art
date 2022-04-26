from typing import Tuple

import numpy as np
import pytest
from numpy.testing import assert_array_equal

from app.canvas import Canvas
from app.turtle import RandomWalkTurtle
from tests.data.canvas_data import random_turtle_canvas_data


class TestCanvas:
    @pytest.mark.parametrize(*random_turtle_canvas_data())
    def test_random_turtle_canvas(
        self,
        turtle: RandomWalkTurtle,
        grid_size: Tuple[int],
        num_steps: int,
        expected_grid: np.ndarray,
    ):
        # Arrange
        canvas = Canvas(turtle, grid_size)

        # Act
        for i in range(num_steps):
            canvas.step()

        grid = canvas.grid

        # Assert
        assert_array_equal(grid, expected_grid)
