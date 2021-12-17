with open("Input.txt", "r") as f:
    line = f.readline().rstrip()
    left, right = line.split(",")
    lowx = int(left[left.index("=")+1:left.index(".")])
    highx = int(left[left.index(".")+2:])
    lowy = int(right[right.index("=")+1:right.index(".")])
    highy = int(right[right.index(".")+2:])

def shoot(vx0, vy0):
    x = 0
    y = 0
    vx = vx0
    vy = vy0
    h = 0
    while y > lowy:
        x += vx
        y += vy
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
        if y > h:
            h = y
        if x >= lowx and x <= highx and y >= lowy and y <= highy:
            return h
    return None

hits = 0
for vx0 in range(highx + 1):
    for vy0 in range(lowy, -lowy + 1):
        result = shoot(vx0, vy0)
        if not result is None:
            hits += 1
print(hits)