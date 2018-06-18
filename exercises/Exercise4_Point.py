import math

class Point(object):
    # when creating a point we can either pass the coordinates
    # or just create a new point without any coordinates and they
    # will be set to 0
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    # defining a __str__ function we can control the behaviour when
    # we call print on our Point objects
    def __str__(self):
        return "x: {} \t y: {}".format(self.x, self.y)
    
def volume_from_points(p1: Point, p2: Point):
    radius = distance(p1, p2)
    return volume_from_radius(radius)


def distance(p1: Point, p2: Point):
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


def volume_from_radius(radius):
    return 4.0/3 * math.pi * radius**3

point1 = Point(3,4)
point2 = Point(3,5)
print(point1)
print(volume_from_points(point1, point2))