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


# Given a set of points, find the closest pair of points
def test_point_closest_pair():
    points = [Point(1, 2), Point(3, 4), Point(5, 6), Point(7, 8)]
    assert Point.closest_pair(points) == (Point(1, 2), Point(3, 4))


# TODO: Fix conevex_hull
# Test the covex hull method
def test_point_convex_hull():
    points = [Point(1, 2), Point(3, 4), Point(5, 6), Point(7, 8), Point(6, 2), Point(4, 3)]
    assert Point.convex_hull(points) == [Point(1, 2), Point(3, 4), Point(5, 6), Point(7, 8), Point(2,6)]
