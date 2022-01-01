from sys import stdin

lines = []
for line in stdin:
    lines.append(line.strip())

memo = [0] * len(lines[0])
for line in lines:
    for i, c in enumerate(line):
        memo[i] += 1 if c == "1" else -1

print(memo)

gamma = ""
epsilon = ""

for value in memo:
    gamma += "1" if value > 0 else "0"
    epsilon += "0" if value > 0 else "1"

print(gamma, epsilon, int(gamma, 2), int(epsilon, 2))
ans = int(gamma, 2) * int(epsilon, 2)
print(ans)
