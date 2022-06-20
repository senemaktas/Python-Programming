# import sympy and Point, Line
from sympy import Point, Line

line1 = [(8, 743), (1912, 743)]
line2 = [(172, 434), (1751, 434)]
line3 = [(466, 207), (1279, 207)]

# line to line
for i, line in enumerate([line1, line2, line3]):
    print("i[0], i[1]", line[0], line[1])

    p1, p2, p3, p4 = Point(876, 434), Point(927,434), Point(line[0]), Point(line[1])

    l1 = Line(p1, p2)
    l2 = Line(p3, p4)

    print("p1, p2, p3, p4",p1, p2, p3, p4)

    # using intersection() method
    showIntersection = l1.intersection(l2)

    print(showIntersection)

# line and pointtt
for i, line in enumerate([line1, line2, line3]):
    print("i[0], i[1]", line[0], line[1])

    p1, p2, p3 = Point(876, 434), Point(line[0]), Point(line[1])
    l1 = Line(p2, p3)

    # using intersection() method
    showIntersection = l1.intersection(p1)

    print(len(showIntersection))