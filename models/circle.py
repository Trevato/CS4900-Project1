# Contains the Circle class
# A Circle is defined by a radius and a center point

from models.point import Point


class Circle:
    def __init__(self, radius, center: Point):
        self.radius = radius
        self.center = center

    def __str__(self) -> str:
        return "Circle with radius {} at {}".format(self.radius, self.center)

    def __repr__(self) -> str:
        return "Circle({}, {})".format(self.radius, self.center)

    # Calculate the distance from a point to itself
    def distance_from_point(self, point) -> float:
        return ((self.center.x - point.x) ** 2 + (self.center.y - point.y) ** 2) ** 0.5
