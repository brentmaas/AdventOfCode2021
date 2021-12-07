with open("Input.txt", "r") as f:
    crabs = [int(i) for i in f.readline().rstrip().split(",")]
crabs.sort()
fuels = []
for i in range(min(crabs), max(crabs)):
    fuel = 0
    for crab in crabs:
        fuel += abs(crab - i) * (abs(crab - i) + 1) // 2
    fuels.append(fuel)
print(fuels[fuels.index(min(fuels))])