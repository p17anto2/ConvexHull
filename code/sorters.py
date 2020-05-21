from math import floor


# p = [(x1,y1), (x2,y2), ... , (xn,yn)]


def bubble_sort(p):
    for i in range(len(p)):
        swapped = False
        for j in range(0, len(p) - i - 1):
            if p[j] > p[j + 1]:
                p[j], p[j + 1] = p[j + 1], p[j]
                swapped = True
        if not swapped:
            break


def partition(p, low, high):
    pivot = p[high]
    i = (low - 1)
    for j in range(low, high):
        if p[j] < pivot:
            i += 1
            p[i], p[j] = p[j], p[i]
    p[i + 1], p[high] = p[high], p[i + 1]
    return i + 1


def quick_sort(p, low, high):
    if low < high:
        pi = partition(p, low, high)

        quick_sort(p, low, pi - 1)
        quick_sort(p, pi + 1, high)


def insertion_sort(p):
    for j in range(1, len(p)):
        key = p[j]
        i = j - 1
        while i >= 0 and p[i][0] > key[0]:
            p[i + 1] = p[i]
            i -= 1
        if p[i][0] == key[0] and p[i][1] > key[1]:
            p[i + 1] = key
            p[i], p[i + 1] = p[i + 1], p[i]
        else:
            p[i + 1] = key


def merge_sort(p):
    if len(p) == 1:
        return p
    mid = floor((len(p)-1) / 2)
    left = merge_sort(p[:mid + 1])
    right = merge_sort(p[mid + 1:])
    return merge(left, right)


def merge(left, right):
    merged = []
    while len(left) and len(right):
        if left[0][0] < right[0][0] or (left[0][0] == right[0][0] and left[0][1] < right[0][1]):
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    while len(left):
        if merged[-1][0] == left[0][0] and left[0][1] < merged[-1][1]:
            merged.insert(len(merged)-1, left.pop(0))
        else:
            merged.append(left.pop(0))
    while len(right):
        if merged[-1][0] == right[0][0] and right[0][1] < merged[-1][1]:
            merged.insert(len(merged) - 1, right.pop(0))
        else:
            merged.append(right.pop(0))
    return merged


def choose_sorter(i, points):
    if i == 0:
        return bubble_sort(points)
    elif i == 1:
        return quick_sort(points, 0, len(points) - 1)
    elif i == 2:
        return insertion_sort(points)
    elif i == 3:
        return merge_sort(points)

