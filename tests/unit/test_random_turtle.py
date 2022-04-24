import pytest
from typing import Tuple, List
from app.coord import Coord, Vector
from app.turtle import RandomWalkTurtle, Turtle
from assertpy import assert_that
from tests.data.turtle_data import random_turtle_data


class TestTurtle:
    
    @pytest.mark.parametrize(*random_turtle_data())
    def test_random_turtle(self, start_position: Tuple[int], num_steps: int, expected_result: List[Vector]):
        # Arrange
        turtle = RandomWalkTurtle(start_position)

        # Act
        vectors = [turtle.generate_next_vector() for _ in range(num_steps)]

        # Assert
        assert_that(vectors).is_equal_to(expected_result)
