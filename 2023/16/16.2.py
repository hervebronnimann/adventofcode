import sys
sys.setrecursionlimit(10000)

input = open("input.txt",'r').read().strip().split('\n')
n = len(input); m = len(input[0])

def create_grid(n,m):
    g = {}
    for i in range(n):
        for j in range(m):
           g[(i,j)] = set()
    return g

def cast(g,i,j,di,dj):
    if i < 0 or i>=n: return
    if j < 0 or j>=m: return
    cycle = (di,dj) in g[(i,j)]
    g[(i,j)].add((di,dj))
    if input[i][j]=='\\':
       cast(g,i+dj,j+di,dj,di)
    elif input[i][j]=='/':
       cast(g,i-dj,j-di,-dj,-di)
    elif input[i][j]=='|' and di==0:
       cast(g,i-1,j,-1,0)
       cast(g,i+1,j,1,0)
    elif input[i][j]=='-' and dj==0:
       cast(g,i,j-1,0,-1)
       cast(g,i,j+1,0,1)
    elif not cycle:
        cast(g,i+di,j+dj,di,dj)

def solve(i,j,di,dj):
    g = create_grid(n,m)
    cast(g,i,j,di,dj)
    return sum([len(g[(i,j)]) > 0 for i,j in g.keys()])

energized = []
for i in range(n):
    energized.append(solve(i,0,0,1))
    energized.append(solve(i,m-1,0,-1))
for j in range(m):
    energized.append(solve(0,j,1,0))
    energized.append(solve(n-1,j,-1,0))
print(max(energized))
