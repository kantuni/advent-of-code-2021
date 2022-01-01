from sys import stdin

cmds = []
for line in stdin:
    cmd, value = line.split(" ")
    cmds.append((cmd, int(value)))

x = 0 # horizontal position
y = 0 # depth
z = 0 # aim

for cmd, value in cmds:
    if cmd == "forward":
        x += value
        y += z * value
    elif cmd == "down":
        z += value
    elif cmd == "up":
        z -= value

print(x * y)
