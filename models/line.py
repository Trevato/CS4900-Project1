# Contains the Line class
# A Line is defined by two points


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
