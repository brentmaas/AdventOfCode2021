import os
import subprocess
import time

days = [int(i[3:]) for i in os.listdir(".") if i.startswith("Day")]
days.sort()
t0 = time.time()
for day in days:
    t1 = time.time()
    subprocess.check_call(["python", "part1.py"], stdout=subprocess.DEVNULL, cwd=f"Day{day}")
    print(f"Day{day} part 1: {time.time()-t1:.3f}s")
    t1 = time.time()
    subprocess.check_call(["python", "part2.py"], stdout=subprocess.DEVNULL, cwd=f"Day{day}")
    print(f"Day{day} part 2: {time.time()-t1:.3f}s")
print(f"Total: {time.time()-t0:.3f}s")