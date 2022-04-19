# Tests the Circle class and its methods

from models.circle import Circle
from models.point import Point

# Create a circle with radius 2 centered at (0, 0)
def test_circle_init():
    circle = Circle(2, Point(0, 0))
    assert circle.radius == 2
    assert circle.center.x == 0
    assert circle.center.y == 0


# Print the circle
def test_circle_str():
    circle = Circle(2, Point(0, 0))
    assert str(circle) == "Circle with radius 2 at Point(0, 0)"


# Repr the circle
def test_circle_repr():
    circle = Circle(2, Point(0, 0))
    assert repr(circle) == "Circle(2, Point(0, 0))"
