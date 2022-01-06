from sys import stdin
from pprint import pprint
from collections import deque

MATRIX = []

for line in stdin:
    MATRIX.append([int(x) for x in line.strip()])

N = len(MATRIX)
M = len(MATRIX[0])


def get_neighbors(i, j):
    neighbors = []
    shifts = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    for dx, dy in shifts:
        if 0 <= i + dx < N and 0 <= j + dy < M:
            neighbors.append((i + dx, j + dy))
    return neighbors


ans = 0
low_points = []

for i in range(N):
    for j in range(M):
        neighbors = get_neighbors(i, j)
        if MATRIX[i][j] < min([MATRIX[i][j] for i, j in neighbors]):
            low_points.append((i, j))


def bfs(i, j):
    size = 1
    visited = {(i, j)}
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()

        neighbors = get_neighbors(x, y)
        for i, j in neighbors:
            if (i, j) not in visited and MATRIX[i][j] != 9:
                q.append((i, j))
                visited.add((i, j))
                size += 1

    return size


sizes = []
for low_x, low_y in low_points:
    size = bfs(low_x, low_y)
    sizes.append(size)

sizes.sort()

print(sizes[-1] * sizes[-2] * sizes[-3])
