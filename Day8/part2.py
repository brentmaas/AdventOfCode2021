s = 0
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        spl = line.split(" ")
        for i in range(len(spl)):
            temp = [j for j in spl[i]]
            temp.sort()
            spl[i] = "".join(temp)
        nums = [i for i in spl if not i == "|"]
        addstart = spl.index("|")
        decode = {}
        encode = {}
        for num in nums:
            if len(num) == 2:
                decode[num] = "1"
                encode1 = num
            elif len(num) == 3:
                decode[num] = "7"
            elif len(num) == 4:
                decode[num] = "4"
                encode4 = num
            elif len(num) == 7:
                decode[num] = "8"
        for num in nums:
            intersect1 = sum([c in num for c in encode1])
            intersect4 = sum([c in num for c in encode4])
            if len(num) == 5:
                if intersect1 == 2:
                    decode[num] = "3"
                elif intersect4 == 3:
                    decode[num] = "5"
                else:
                    decode[num] = "2"
            elif len(num) == 6:
                if intersect1 == 1:
                    decode[num] = "6"
                elif intersect4 == 4:
                    decode[num] = "9"
                else:
                    decode[num] = "0"
        s += int("".join([decode[c] for c in nums[addstart:]]))
print(s)