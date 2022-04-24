# from typing import List, Tuple

# import pytest
# from assertpy import assert_that
# import numpy as np

# from app.canvas import Canvas
# from app.coord import Vector
# from app.turtle import RandomWalkTurtle
# from tests.data.turtle_data import random_turtle_canvas_data


# class TestCanvas:
#     @pytest.mark.parametrize(*random_turtle_canvas_data())
#     def test_random_turtle_canvas(
#         self, turtle: RandomWalkTurtle, grid_size: Tuple[int], num_steps: int, expected_grid: np.ndarray
#     ):
#         # Arrange
#         canvas = Canvas(turtle, grid_size)

#         # Act
#         for _ in range(num_steps):
#             canvas.step()

#         grid = canvas.grid

#         # Assert
#         assert_that(grid).is_equal_to(expected_grid)
