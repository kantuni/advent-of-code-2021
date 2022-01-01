from collections import defaultdict
from sys import stdin


lines = []
for line in stdin:
    lines.append(line.strip())

memo = defaultdict(int)
for i, c in enumerate(line.strip()):
    memo[i] += 1 if c == "1" else -1


def oxygen(report, index):
    if len(report) == 1:
        return report[0]

    balance = 0
    for line in report:
        balance += 1 if line[index] == "1" else -1

    majority = "1" if balance >= 0 else "0"
    filtered = list(filter(lambda line: line[index] == majority, report))
    return oxygen(filtered, index + 1)


def co2(report, index):
    if len(report) == 1:
        return report[0]

    balance = 0
    for line in report:
        balance += 1 if line[index] == "1" else -1

    minority = "1" if balance < 0 else "0"
    filtered = list(filter(lambda line: line[index] == minority, report))
    return co2(filtered, index + 1)


oxygen_rate = oxygen(lines, 0)
co2_rate = co2(lines, 0)
ans = int(oxygen_rate, 2) * int(co2_rate, 2)
print(ans)
