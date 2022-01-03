from collections import defaultdict

fish = list(map(int, input().split(",")))
state = defaultdict(int)

for f in fish:
    state[f] += 1


def next_generation(state):
    new_state = defaultdict(int)
    for key, value in state.items():
        if key == 0:
            new_state[6] += value
            new_state[8] += value
        else:
            new_state[key - 1] += value
    return new_state


days = 256
for _ in range(days):
    state = next_generation(state)

ans = sum(state.values())
print(ans)
