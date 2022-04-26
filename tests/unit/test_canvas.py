import random
from typing import Tuple

import numpy as np
import pytest
from app.canvas import Canvas
from app.turtle import Turtle
from numpy.testing import assert_array_equal
from tests.data.canvas_data import (random_turtle_canvas_data,
                                    random_turtle_canvas_n_step_data)


class TestCanvas:

    # @pytest.fixture
    # def random():
    #     random.seed(149)

    @pytest.mark.parametrize(*random_turtle_canvas_data())
    def test_random_turtle_canvas(
        self,
        turtle: Turtle,
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

    @pytest.mark.parametrize(*random_turtle_canvas_n_step_data())
    def test_random_turtle_n_step_canvas(
        self,
        turtle: Turtle,
        grid_size: Tuple[int],
        num_steps: int,
        expected_grid: np.ndarray,
    ):
        # Arrange
        canvas = Canvas(turtle, grid_size)

        # Act
        canvas.n_steps(num_steps)

        grid = canvas.grid
        print(grid)

        # Assert
        assert_array_equal(grid, expected_grid)
