from pytest import param

from app.coord import Coord, Vector


def coord_xy_data():
    test_variables = "x,y,expected_result"
    test_data = [param(0, 0, Coord(0, 0), id="Coord(0,0)")]
    return test_variables, test_data


def vector_addition_data():
    test_variables = "coord,vector,expected_result"
    test_data = [
        param(Coord(0, 0), Vector(1, 1), Coord(1, 1), id="One step North East"),
        param(Coord(1, 1), Vector(-1, -1), Coord(0, 0), id="Undo previous operation"),
        param(Coord(3, 2), Vector(-4, 5), Coord(-1, 7), id="More complex vector"),
    ]
    return test_variables, test_data
