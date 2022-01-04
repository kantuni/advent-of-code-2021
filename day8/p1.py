from sys import stdin

displays = []
for line in stdin:
    _, output = line.strip().split(" | ")
    displays.extend(output.split())

ans = 0
for display in displays:
    # digit: number of segments
    # 1: 2, 4: 4, 7: 3, 8: 7
    if len(display) in {2, 3, 4, 7}:
        ans += 1

print(ans)
