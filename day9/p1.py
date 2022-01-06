from sys import stdin
from pprint import pprint

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
            neighbors.append(MATRIX[i + dx][j + dy])
    return neighbors


ans = 0

for i in range(N):
    for j in range(M):
        neighbors = get_neighbors(i, j)
        if MATRIX[i][j] < min(neighbors):
            ans += MATRIX[i][j] + 1

print(ans)
