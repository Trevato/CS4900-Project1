# Tests the Line class and its methods

from models.line import Line
from models.point import Point

# Create a line from (1, 2) to (3, 4)
def test_line_init():
    line = Line(Point(1, 2), Point(3, 4))
    assert line.point1.x == 1
    assert line.point1.y == 2
    assert line.point2.x == 3
    assert line.point2.y == 4


# Print the line
def test_line_str():
    line = Line(Point(1, 2), Point(3, 4))
    assert str(line) == "Line from (1, 2) to (3, 4)"


# Repr the line
def test_line_repr():
    line = Line(Point(1, 2), Point(3, 4))
    assert repr(line) == "Line(Point(1, 2), Point(3, 4))"
