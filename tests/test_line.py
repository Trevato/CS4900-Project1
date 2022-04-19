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


# Test the slope of the line
def test_line_slope():
    line = Line(Point(1, 2), Point(3, 4))
    assert line.slope() == 1


# Test the is_parallel method
def test_line_is_parallel_1():
    line1 = Line(Point(1, 2), Point(3, 4))
    line2 = Line(Point(1, 2), Point(3, 5))
    assert line1.is_parallel(line2) == False


# Test the is_parallel method again
def test_line_is_parallel_2():
    line1 = Line(Point(1, 2), Point(3, 4))
    line2 = Line(Point(1, 2), Point(3, 4))
    assert line1.is_parallel(line2) == True


# Test the intersection method
def test_line_intersection_1():
    line1 = Line(Point(1, 2), Point(3, 4))
    line2 = Line(Point(1, 2), Point(2, 7))
    assert line1.intersection(line2) == Point(1.0,2.0)


# Test the intersection method again
def test_line_intersection_2():
    line1 = Line(Point(1, 2), Point(3, 4))
    line2 = Line(Point(1, 2), Point(3, 4))
    assert line1.intersection(line2) == None
