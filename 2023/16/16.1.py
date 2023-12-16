import sys
sys.setrecursionlimit(10000)

input = open("input.txt",'r').read().strip().split('\n')
n = len(input); m = len(input[0])

g = {}
for i in range(n):
    for j in range(m):
       g[(i,j)] = set()

def cast(i,j,di,dj):
    if i < 0 or i>=n: return
    if j < 0 or j>=m: return
    cycle = (di,dj) in g[(i,j)]
    g[(i,j)].add((di,dj))
    if input[i][j]=='\\':
       cast(i+dj,j+di,dj,di)
    elif input[i][j]=='/':
       cast(i-dj,j-di,-dj,-di)
    elif input[i][j]=='|' and di==0:
       cast(i-1,j,-1,0)
       cast(i+1,j,1,0)
    elif input[i][j]=='-' and dj==0:
       cast(i,j-1,0,-1)
       cast(i,j+1,0,1)
    elif not cycle:
       cast(i+di,j+dj,di,dj)

cast(0,0,0,1)
print(sum([len(g[(i,j)]) > 0 for i,j in g.keys()]))
