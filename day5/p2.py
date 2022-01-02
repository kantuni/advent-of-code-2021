from sys import stdin

mx = -1
my = -1

lines = []
for line in stdin:
    raw_p1, raw_p2 = line.split(" -> ")
    x1, y1 = map(int, raw_p1.split(","))
    x2, y2 = map(int, raw_p2.split(","))

    # x1 is always smaller than x2
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1

    mx = max(mx, x1, x2)
    my = max(my, y1, y2)
    lines.append(((x1, y1), (x2, y2)))

R = my + 1
C = mx + 1
grid = [[0] * C for _ in range(R)]

for p1, p2 in lines:
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[y][x1] += 1

    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[y1][x] += 1

    else:
        y = y1
        for x in range(x1, x2 + 1):
            grid[y][x] += 1
            if y < y2:
                y += 1
            else:
                y -= 1

ans = 0
for row in grid:
    for number in row:
        if number > 1:
            ans += 1

print(ans)
