grids = open('input.txt').read().strip().split('\n\n')

def is_lock(g): return g[0][0] == '#'#

def parse(g):
    n,m,c = len(g),len(g[0]),g[-1][0]
    result = []
    for j in range(m):
        k = [g[i][j] for i in range(n)].index(c)
        result.append(k-1 if c == '.' else n-1-k)
    return n,tuple(result)

def overlap(n,k,l):
    return max(map(sum,zip(k,l))) > n-2

n = -1
locks = []
keys = []
for l in grids:
    g = l.split('\n')
    lock = is_lock(g)
    n,g = parse(g)
    if lock:
        locks.append(g)
    else:
        keys.append(g)
print(n)
print(locks)
print(keys)

result = 0
for k in keys:
    for l in locks:
        if not overlap(n,k,l):
            result += 1
print(result)
