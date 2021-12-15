with open("input2.txt") as file:
    commands = file.read()

commands = commands.splitlines()

horizontal = 0
depth = 0

for el in commands:
    if 'forward' in el:
        horizontal += int(el[-1])
    if 'down' in el:
        depth += int(el[-1])
    if 'up' in el:
        depth -= int(el[-1])
print(horizontal)
print(depth)
print(depth*horizontal)