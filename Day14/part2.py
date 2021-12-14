rules = {}
with open("Input.txt", "r") as f:
    template = f.readline().rstrip()
    f.readline()
    while line := f.readline().rstrip():
        spl = line.split(" -> ")
        rules[spl[0]] = spl[1]
pairs = {}
for i in range(len(template)-1):
    pair = template[i:i+2]
    if pair in pairs:
        pairs[pair] += 1
    else:
        pairs[pair] = 1
for _ in range(40):
    newpairs = {}
    for pair in pairs:
        leftpair = pair[0] + rules[pair]
        rightpair = rules[pair] + pair[1]
        if leftpair in newpairs:
            newpairs[leftpair] += pairs[pair]
        else:
            newpairs[leftpair] = pairs[pair]
        if rightpair in newpairs:
            newpairs[rightpair] += pairs[pair]
        else:
            newpairs[rightpair] = pairs[pair]
    pairs = newpairs
count = {template[0]: 1}
for pair in pairs:
    if pair[1] in count:
        count[pair[1]] += pairs[pair]
    else:
        count[pair[1]] = pairs[pair]
vals = [count[key] for key in count.keys()]
print(max(vals) - min(vals))