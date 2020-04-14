import matplotlib.pyplot as plt
import convexHull
import sorters
import fn


points = []
fn.make_points(points)

print(*points)
sorters.quick_sort(points, 0, len(points)-1)
print(*points)
hull = convexHull.convex_hull(points)

print("\n\n\n\n\n")
print(*hull)

colors = []

for x in points:
    if x in hull:
        colors.append('red')
    else:
        colors.append('blue')

plt.scatter([x[0] for x in points], [y[1] for y in points], s=10, c=colors)
for i in range(len(hull)):
    x = [val[0] for val in hull]
    y = [val[1] for val in hull]
    x.append(hull[0][0])
    x.append(hull[-1][0])
    y.append(hull[0][1])
    y.append(hull[-1][-1])
    plt.plot(x, y)
plt.show()
