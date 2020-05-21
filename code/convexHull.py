def convex_hull(p):
    l_upper = p[:2]
    for i in range(2, len(p)):
        l_upper.append(p[i])
        while len(l_upper) > 2 and not right_turn(l_upper):
            l_upper.pop(-2)

    l_lower = [p[-1], p[-2]]
    for i in range(len(p)-3, -1, -1):
        l_lower.append(p[i])
        while len(l_lower) > 2 and not right_turn(l_lower):
            l_lower.pop(-2)
    l_lower.pop(0)
    l_lower.pop(-1)
    return l_upper + l_lower


def right_turn(hull):
    det = [hull[-2][0] - hull[-3][0], hull[-1][0] - hull[-3][0],
           hull[-2][1] - hull[-3][1], hull[-1][1] - hull[-3][1]]
    cross = det[0]*det[3] - det[1]*det[2]
    if cross < 0:
        return True
