from sys import stdin

measurements = []
for line in stdin:
    measurements.append(int(line))

ans = 0
for i in range(len(measurements) - 1):
    if measurements[i] < measurements[i + 1]:
        ans += 1

print(ans)
