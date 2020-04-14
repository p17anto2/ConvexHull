import matplotlib.pyplot as plt
import random
import sorters
import fn


points = []
fn.make_points(points)

print(*points)
sorters.quick_sort(points, 0, len(points)-1)
print(*points)
# plt.scatter([x[0] for x in points], [y[1] for y in points])
# plt.show()
