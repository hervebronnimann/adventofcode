from collections import defaultdict
import math
import functools

input={int(x):1 for x in "6 11 33023 4134 564 0 8922422 688775".split()}

@functools.cache
def evolve(x):
    if x == 0:
        return [1]
    xx = str(x)
    if len(xx)%2 == 0:
        r = len(xx)//2
        return [int(xx[0:r]), int(xx[r:])]
    else:
        return [x * 2024]

for i in range(75):
    r = defaultdict(lambda: 0)
    for x,c in input.items():
        for y in evolve(x):
            r[y] += c
    print(f"Depth {i}: max {max(r.keys())}")
    input = r

print(sum(input.values()))
