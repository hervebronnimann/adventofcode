import sys
from copy import deepcopy

sys.setrecursionlimit(10000)

input = open("input.txt",'r').read().strip().split('\n')
n = len(input); m = len(input[0])

g = {}
for i in range(n):
    for j in range(m):
       g[(i,j)] = set()

def dirchar(i,j):
    if (i,j)==(0,1): return '>'
    elif (i,j)==(0,-1): return '<'
    elif (i,j)==(-1,0): return '^'
    elif (i,j)==(1,0): return 'v'
    else: return '.'

def printgrid(g):
    x = []
    for l in input: x.append(list(l))
    for i,j in g.keys():
        if x[i][j]=='.':
            if (0,1) in g[(i,j)]: x[i][j] = '>'
            elif (0,-1) in g[(i,j)]: x[i][j] = '<'
            elif (-1,0) in g[(i,j)]: x[i][j] = '^'
            elif (1,0) in g[(i,j)]: x[i][j] = 'v'
    # print("\n".join(["".join(y) for y in x]))

def cast(g,i,j,di,dj):
    if i < 0 or i>=n: return
    if j < 0 or j>=m: return
    cycle = (di,dj) in g[(i,j)]
    g[(i,j)].add((di,dj))
    print(f'Visiting {i},{j}: {dirchar(di,dj)}')
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

cast(g,0,0,0,1)
#printgrid(g)
res = 0
for i,j in g.keys():
    if len(g[(i,j)]) > 0: res += 1
print(res)
