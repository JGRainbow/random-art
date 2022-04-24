from pytest import param

from app.coord import Coord, Vector


def random_turtle_data():
    test_variables = "start_position,num_steps,expected_result"
    test_data = [
        param(Coord(0, 0), 1, [Vector(-1, -1)], id="one move from origin"),
        param(
            Coord(1, 1),
            3,
            [Vector(dx=-1, dy=-1), Vector(dx=1, dy=1), Vector(dx=-1, dy=-1)],
            id="three moves from offset",
        ),
        param(
            Coord(-2, -3),
            10,
            [
                Vector(dx=-1, dy=-1),
                Vector(dx=1, dy=1),
                Vector(dx=-1, dy=-1),
                Vector(dx=-1, dy=-1),
                Vector(dx=-1, dy=-1),
                Vector(dx=1, dy=-1),
                Vector(dx=-1, dy=1),
                Vector(dx=-1, dy=-1),
                Vector(dx=1, dy=-1),
                Vector(dx=-1, dy=1),
            ],
            id="ten moves from negative offset",
        ),
    ]
    return test_variables, test_data
