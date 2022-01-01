from sys import stdin

measurements = []
for line in stdin:
    measurements.append(int(line))

ans = 0
ps = 0
for i in range(len(measurements) - 2):
    s = measurements[i] + measurements[i + 1] + measurements[i + 2]
    if s > ps:
        ans += 1
    ps = s

print(ans - 1)
