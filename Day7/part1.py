with open("Input.txt", "r") as f:
    crabs = [int(i) for i in f.readline().rstrip().split(",")]
crabs.sort()
pos = crabs[len(crabs)//2]
fuel = 0
for crab in crabs:
    fuel += abs(crab - pos)
print(fuel)