from collections import defaultdict
import math

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
            d = math.gcd(i1-i0,j1-j0)
            for k in range(n+m):
                if not valid(i1+k*(i1-i0)//d,j1+k*(j1-j0)//d): break
                antinodes.add((i1+k*(i1-i0)//d,j1+k*(j1-j0)//d))
            for k in range(n+m):
                if not valid(i0+k*(i0-i1)//d,j0+k*(j0-j1)//d): break
                antinodes.add((i0+k*(i0-i1)//d,j0+k*(j0-j1)//d))

print(len([ (x,y) for x,y in antinodes if valid(x,y)]))
