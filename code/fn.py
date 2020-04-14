import random


#  O(N^2) list creation
def make_points(points):
    for i in range(0, 100):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        if (x, y) not in points:
            points.append((x, y))
