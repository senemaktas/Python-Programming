# python program to check if a line
# touches or  intersects or outside
# a circle.

import math


def checkCollision(a, b, c, x, y, radius):
    # Finding the distance of line
    # from center.
    dist = ((abs(a * x + b * y + c)) /
            math.sqrt(a * a + b * b))

    # Checking if the distance is less
    # than, greater than or equal to radius.
    if (radius == dist):
        print("Touch")
    elif (radius > dist):
        print("Intersect")
    else:
        print("Outside")


# Driven Program
radius = 5
x = 0
y = 0
a = 3
b = 4
c = 25
checkCollision(a, b, c, x, y, radius)