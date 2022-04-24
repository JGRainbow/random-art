import pytest
from app.coord import Coord
from assertpy import assert_that
from tests.data.coord_data import coord_xy_data


class TestCoord:
    
    @pytest.mark.parametrize(*coord_xy_data())
    def test_coord_xy(self, x: int, y: int, expected_result: Coord):
        # Arrange
        # Act
        coord = Coord(x, y)

        # Assert
        assert_that(coord).is_equal_to(expected_result)



if __name__ == "__main__":
    import app
