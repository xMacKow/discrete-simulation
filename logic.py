import math


def find_closest(x, y, arr):
    currently_best = None
    currently_best_dist = 0
    for i in range(0, len(arr)):
        distance = get_distance(x, y, arr[i].x, arr[i].y)
        if (distance < currently_best_dist or currently_best_dist == 0):
            currently_best_dist = distance
            currently_best = arr[i]

    return [currently_best, currently_best_dist]


def find_closest_object(x, y, arr):
    currently_best = None
    currently_best_dist = 0
    for i in range(0, len(arr)):
        distance = get_distance(x, y, arr[i].x, arr[i].y)
        if (distance < currently_best_dist or currently_best_dist == 0):
            currently_best_dist = distance
            currently_best = arr[i]

    return currently_best


def get_distance(x, y, x2, y2):
    return math.sqrt((x - x2) ** 2 + (y - y2) ** 2)


def is_inside(l_top, size, x, y):
    return (l_top[0] < x < l_top[0] + size and
            l_top[1] < y < l_top[1] + size)


def does_overlap(first, second):
    l1 = [first.x, first.y]
    l2 = [second.x, second.y]

    return (is_inside(l1, first.get_size(), l2[0], l2[1])
            or is_inside(l1, first.get_size(), l2[0] + second.get_size(), l2[1])
            or is_inside(l1, first.get_size(), l2[0], l2[1] + second.get_size())
            or is_inside(l1, first.get_size(), l2[0] + second.get_size(), l2[1] + second.get_size())
            or
            is_inside(l2, second.get_size(), l1[0], l1[1])
            or is_inside(l2, second.get_size(), l1[0] + first.get_size(), l1[1])
            or is_inside(l2, second.get_size(), l1[0], l1[1] + first.get_size())
            or is_inside(l2, second.get_size(), l1[0] + first.get_size(), l1[1] + first.get_size())
            )
