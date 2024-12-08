from collections import defaultdict

grid = [ list(x) for x in open("input.txt",'r').read().strip().split('\n') ]

nodes = defaultdict(list)
for i,l in enumerate(grid):
    for j,x in enumerate(l):
        if x != '.': nodes[x].append((i,j))

n = len(grid)
m = len(grid[0])
def valid(i,j): return i >= 0 and i < n and j >= 0 and j < m

antinodes = set()
for x,l in nodes.items():
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            i0,j0 = l[i]
            i1,j1 = l[j]
            antinodes.add((2*i1-i0,2*j1-j0))
            antinodes.add((2*i0-i1,2*j0-j1))

print(len([ (x,y) for x,y in antinodes if valid(x,y)]))
