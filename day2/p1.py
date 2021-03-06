from sys import stdin

cmds = []
for line in stdin:
    cmd, value = line.split(" ")
    cmds.append((cmd, int(value)))

x = 0 # horizontal position
y = 0 # depth

for cmd, value in cmds:
    if cmd == "forward":
        x += value
    elif cmd == "down":
        y += value
    elif cmd == "up":
        y -= value

print(x * y)
