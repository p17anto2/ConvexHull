import random
#  O(N^2) list creation


def make_points(points, n):
    for i in range(0, n):
        x = random.uniform(0, 1000)
        y = random.uniform(0, 1000)
        if (x, y) not in points:
            points.append((x, y))
