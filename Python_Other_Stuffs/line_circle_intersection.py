# python program to check if a line # touches or  intersects or outside a circle.

# https://stackoverflow.com/questions/30844482/
# what-is-most-efficient-way-to-find-the-intersection-of-a-line-and-a-circle-in-py
from shapely.geometry import LineString, Point, MultiPoint
import math
import cv2

radius = 2  # radius of circle
cx = 500  # center of circle x axis
cy = 450  # center of circle y axis

p = Point(cx,cy)
c = p.buffer(radius).boundary
l = LineString([(450,450), (620, 450)])  # line coordinates
i = c.intersection(l)

print(i)   # MULTIPOINT (498 450, 502 450)
print("MultiPoint",MultiPoint(i))  # MULTIPOINT (498 450, 502 450)
print(i.is_empty)  # not empty -> False

m = MultiPoint(i)
print(m.is_empty)  # False
# print("m[-1].wkt", m[-1].wkt)
print("m.area", m.area)  # m.area 0.0

img =cv2.imread("./people.png")

cv2.line(img,(450,450), (620, 450),  (255, 255, 255), 4)
cv2.circle(img, (cx, cy), radius, (255, 0, 0), -1)

cv2.imshow("test",img) # draw liğne and string on an example image
cv2.waitKey(0)


"""
2. Compare this distance p with radius r.
……a) If p > r, then line lie outside the circle.
……b) If p = r, then line touches the circle.
……c) If p < r, then line intersect the circle.

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
        
# Driven Program- abc line , x,y circle center radius cap
# radius = 5
# x = 70
# y = 80
# a = 350
# b = 400
# c = 0
# checkCollision(a, b, c, x, y, radius)
"""
