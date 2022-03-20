# Tests the Point class and its methods

from models.point import Point

# Create a point at (1, 2)
def test_point_init():
    point = Point(1, 2)
    assert point.x == 1
    assert point.y == 2


# Print the point
def test_point_str():
    point = Point(1, 2)
    assert str(point) == "Point(1, 2)"


# Repr the point
def test_point_repr():
    point = Point(1, 2)
    assert repr(point) == "Point(1, 2)"


# Calculate the distance from a point to itself
def test_point_distance_from_point():
    point = Point(1, 2)
    assert point.distance_from_point(point) == 0
