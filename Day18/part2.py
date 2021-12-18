lines = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        lines.append(line)

def mag(left, right):
    nums = []
    depths = []
    for line in [left, right]:
        for i in range(len(depths)):
            depths[i] += 1
        depth = 0 if len(depths) == 0 else 1
        for c in line:
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
            elif c != ',':
                nums.append(int(c))
                depths.append(depth)
        while True:
            if any([depth > 4 for depth in depths]):
                i = depths.index(max(depths))
                if i > 0:
                    nums[i-1] += nums[i]
                if i < len(nums) - 2:
                    nums[i+2] += nums[i+1]
                nums[i] = 0
                depths[i] -= 1
                nums.pop(i+1)
                depths.pop(i+1)
                continue
            elif any([num > 9 for num in nums]):
                i = [num > 9 for num in nums].index(True)
                nums.insert(i, nums[i] // 2)
                nums[i+1] = nums[i+1] // 2 + (nums[i+1] % 2)
                depths.insert(i, depths[i] + 1)
                depths[i+1] += 1
                continue
            break

    while len(nums) > 1:
        i = depths.index(max(depths))
        nums[i] = 3 * nums[i] + 2 * nums[i+1]
        nums.pop(i+1)
        depths[i] -= 1
        depths.pop(i+1)
    return nums[0]

highest = 0
for i in range(len(lines)-1):
    for j in range(i, len(lines)):
        mag1 = mag(lines[i], lines[j])
        mag2 = mag(lines[j], lines[i])
        if max(mag1, mag2) > highest:
            highest = max(mag1, mag2)
print(highest)