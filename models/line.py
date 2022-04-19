# Contains the Line class
# A Line is defined by two points

from models.point import Point

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2


    def __str__(self):
        return "Line from ({}, {}) to ({}, {})".format(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y
        )


    def __repr__(self):
        return "Line({}, {})".format(self.point1, self.point2)


    def slope(self):
        """
        Returns the slope of this line
        """
        return (self.point2.y - self.point1.y) / (self.point2.x - self.point1.x)


    def is_parallel(self, other):
        """
        Returns True if this line is parallel to another line
        """
        return self.slope() == other.slope()


    def intersection(self, other):
        """
        Returns the intersection point of this line and another line
        Returns None if the lines are parallel
        """
        if self.is_parallel(other):
            return None

        # Find the slope of each line
        slope1 = self.slope()
        slope2 = other.slope()

        # Find the y-intercept of each line
        y_intercept1 = self.point1.y - (slope1 * self.point1.x)
        y_intercept2 = other.point1.y - (slope2 * other.point1.x)

        # Find the intersection point
        x = (y_intercept2 - y_intercept1) / (slope1 - slope2)
        y = slope1 * x + y_intercept1

        return Point(x, y)
