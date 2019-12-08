direction, steps = lambda s: s.split()[0], lambda s: int(s.split()[1])
inputs = ["left 5", "right 3", "left 2", "right 1"]
x = 0
for st in inputs:
    if direction(st) == "left":
        x -= steps(st)
    elif direction(st) == "right":
        x += steps(st)
print(x)
