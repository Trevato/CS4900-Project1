# Contains the Point class
# A Point is defined by an x and y coordinate


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "Point({}, {})".format(self.x, self.y)

    def __repr__(self) -> str:
        return "Point({}, {})".format(self.x, self.y)

    # Point equality
    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    # Calculate the distance from a point to itself
    def distance_from_point(self, point) -> float:
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
