from itertools import *


def way_length(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


# вы можете изменять переменную 'way' для подстановки своих данных в виде: [(a, b), (c, d), ... (x, y)]
# где первый элемент списка - это координаты точки почтового отделения, так же: len(way) = количество точек в маршруте
way = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]  # изначальный путь, если не измениться то значит и min
# way = [(0, 1), (1, 4), (7, 2), (5, 5), (4, 1)]
min_length = 10**10
for i in permutations(way[1:]):
    path = [way[0]]
    path.extend(i)
    path.append(way[0])
    # print(path)
    res = 0
    for k in range(1, len(path)):
        res += way_length(path[k], path[k-1])
    if res < min_length:
        way = path[:]
        min_length = res

# [(0, 2), (5, 2), (8, 3), (6, 6), (2, 5), (0, 2)]  # Второй кратчайший путь (в обратном порядке точек)

res = 0
print(way[0], end=' ')
for i in range(1, len(way)):
    res += way_length(way[i], way[i-1])
    print('->', way[i], [res], end=' ')
print('=', min_length)
