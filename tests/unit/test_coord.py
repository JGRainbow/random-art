import pytest
from assertpy import assert_that

from app.coord import Coord, Vector
from tests.data.coord_data import coord_xy_data, vector_addition_data


class TestCoord:
    @pytest.mark.parametrize(*coord_xy_data())
    def test_coord_xy(self, x: int, y: int, expected_result: Coord):
        # Arrange
        # Act
        coord = Coord(x, y)

        # Assert
        assert_that(coord).is_equal_to(expected_result)

    @pytest.mark.parametrize(*vector_addition_data())
    def test_vector_addition(
        self, coord: Coord, vector: Vector, expected_result: Coord
    ):
        # Arrange
        # Act
        new_coord = coord + vector

        # Assert
        assert_that(new_coord).is_equal_to(expected_result)
