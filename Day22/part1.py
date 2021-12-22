reactor = [[[False for _ in range(101)] for _ in range(101)] for _ in range(101)]
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        spl = line.split(",")
        on = spl[0][:2] == "on"
        lowx = int(spl[0][spl[0].index("=")+1:spl[0].index(".")])
        highx = int(spl[0][spl[0].index(".")+2:])
        lowy = int(spl[1][spl[1].index("=")+1:spl[1].index(".")])
        highy = int(spl[1][spl[1].index(".")+2:])
        lowz = int(spl[2][spl[2].index("=")+1:spl[2].index(".")])
        highz = int(spl[2][spl[2].index(".")+2:])
        for x in range(max(lowx, -50), min(highx, 50) + 1):
            for y in range(max(lowy, -50), min(highy, 50) + 1):
                for z in range(max(lowz, -50), min(highz, 50) + 1):
                    reactor[x+50][y+50][z+50] = on

print(sum([sum([sum(reactor[x][y]) for y in range(101)]) for x in range(101)]))