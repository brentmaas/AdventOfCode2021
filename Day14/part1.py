rules = {}
with open("Input.txt", "r") as f:
    template = f.readline().rstrip()
    f.readline()
    while line := f.readline().rstrip():
        spl = line.split(" -> ")
        rules[spl[0]] = spl[1]
for _ in range(10):
    newtemplate = template[0]
    for i in range(len(template)-1):
        newtemplate += rules[template[i:i+2]] + template[i+1]
    template = newtemplate
count = {}
for c in template:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1
vals = [count[key] for key in count.keys()]
print(max(vals) - min(vals))