from pytest import param
from app.coord import Coord

def coord_xy_data():
    test_variables = "x,y,expected_result"
    test_data = [
        param(
            0,0,Coord(0,0),id="Coord(0,0)"
        )
    ]
    return test_variables, test_data