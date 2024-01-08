# adventofcode

I started doing these in Dec 2020, and with awk, it was awesome! And very compact on the first few days.
As the month went on, awk became more and more cumbersome, but I stuck with it.  Writing graph traversals
and topological sorting in awk was an interesting exercise.

Over time, though, python emerges as the most supple, easiest, and convenient language for this.  Manipulating
strings, grids, arrays, and tuples is what we need.

## Useful Python constructs

### Logic / Sets / Hackers' delights:

```
def bitsoncount(x):
    return bin(x).count("1")

def popcount(x):
    assert 0 <= x < 0x100000000
    x = x - ((x >> 1) & 0x55555555)
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
    return (((x + (x >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24
```

```
def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield ([ss for mask, ss in zip(masks, s) if i & mask], [ss for mask, ss in zip(masks, s) if not i & mask])

```

### Arithmetic:

```
def egcd(a, b):
    if a == 0 : return b,0,1
    g,x1,y1 = egcd(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return g,x,y
```

```
from functools import reduce

def crm(m, a):
    s = 0
    p = reduce(lambda p, b: p*b, m)
    for m_i, a_i in zip(m, a):
        p_i = p // m_i
        s += a_i * egcd(p_i, m_i)[1] * p_i
    return s % p
```

### Grids

Use `yield` and/or `@cache` for generating infinite grids.

```
dir = { 'R':0, 'D':1, 'L':2, 'U':3 }
diri = [ 0, 1, 0, -1 ]
dirj = [ 1, 0, -1, 0 ]

def neighbors4(i,j):
    for d in range(4): yield (i+diri[d], j+dirj[d])
```

```
dir8 = { 'E':0, 'SE':1, 'S':2, 'SW':3, 'W':4, 'NW':5, 'N':6, 'NE':7 }
dir8i = [ 0, 1, 1,  1,  0, -1, -1, -1 ]
dir8j = [ 1, 1, 0, -1, -1, -1,  0,  1 ]

def neighbors8(i,j):
    for d in range(8): yield (i+dir8i[d], j+dir8j[d])
```

```
def transpose(grid):
  return ["".join(list(x)) for x in zip(*grid)]
```

### Algebra

### Intervals

```
def mergeIntervals(arr):
    if len(arr)==0: return arr
    # Sorting based on the increasing order of the start intervals
    arr.sort(key=lambda x: x[0])
    # Stores index of last element in output array
    out = [arr[0]]
    print(out)
    # Traverse all input Intervals starting from second interval
    for i,(u,v) in enumerate(arr[1:]):
        x,y = out[-1]
        # If this is not first Interval and overlaps with the previous one,
        if y >= u:
            # Merge previous and current intervals
            out[-1] = (x,max(v,y))
        else:
            out.append([u,v])
    return out
```
### Graphs

With a graph with a way to provide adjacent nodes:

```
from collections import deque

def bfs(src):  # (src,dst):
    visited = set([src])
    pq = deque()
    pq.append((0,src))
    while pq:
        i,node = pq.popleft()
        for adj in ...:
            if adj in visited: continue
            # if adj == dst: return i+1
            visited.add(adj)
            pq.append((i+1, adj))
    return i # float('inf')
```

With a graph with a way to provide adjacent nodes with cost:

```
import heapq as heap
from collections import defaultdict

def dijkstra(src):
    visited = set(src)
    pq = []
    costs = defaultdict(lambda: float('inf'))
    costs[src] = 0
    heap.heappush(pq, (0, src))
    while pq:
        _, node = heap.heappop(pq)
        visited.add(node)
        for adj,cost in ...:
            if adj in visited:	continue
            newCost = costs[node] + cost
            if costs[adj] > newCost:
                costs[adj] = newCost
                heap.heappush(pq, (newCost, adj))
    return costs
```
