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

    # Given a set of points, find the closest pair of points
    @staticmethod
    def closest_pair(points: list) -> tuple:
        # Sort the points by x coordinate
        points.sort(key=lambda point: point.x)

        # Initialize the closest pair to be the first two points
        closest_pair = (points[0], points[1])

        # Loop through the points
        for i in range(len(points)):
            # Skip the first point
            if i == 0:
                continue

            # Initialize the closest distance to be the distance between the
            # first two points
            closest_distance = points[0].distance_from_point(points[1])

            # Loop through the points after the first point
            for j in range(i + 1, len(points)):
                # Calculate the distance between the current pair of points
                distance = points[i].distance_from_point(points[j])

                # If the distance is less than the closest distance, update
                # the closest distance and closest pair
                if distance < closest_distance:
                    closest_distance = distance
                    closest_pair = (points[i], points[j])

        # Return the closest pair of points
        return closest_pair
