from collections import defaultdict
from functools import lru_cache

def parse(l): x,y,z=l.split(','); return (1+int(x),1+int(y),1+int(z))
lines = list(map(parse, open("example.txt").read().strip().split('\n')))
# lines = list(map(parse, open("input.txt").read().strip().split('\n')))
print(list(lines))

X=max([x+1 for x,_,_ in lines])
Y=max([y+1 for _,y,_ in lines])
Z=max([z+1 for _,_,z in lines])
print((X,Y,Z))

sX = [set([(y,z) for _,y,z in filter(lambda t: t[0]==x0, lines)]) for x0 in range(X+1)]
sY = [set([(x,z) for x,_,z in filter(lambda t: t[1]==y0, lines)]) for y0 in range(Y+1)]
sZ = [set([(x,y) for x,y,_ in filter(lambda t: t[2]==z0, lines)]) for z0 in range(Z+1)]

# dX is the union of sX[i] for i <= x
dX=[set() for _ in range(X+1)]
for x in range(1,X+1): dX[x] = dX[x-1].union(sX[x])
# uX is the union of sX[i] for i >= x
uX=[set() for _ in range(X+2)]
for x in range(X,-1,-1): uX[x] = uX[x+1].union(sX[x])

dY=[set() for _ in range(Y+1)]
for y in range(1,Y+1): dY[y] = dY[y-1].union(sY[y])
uY=[set() for _ in range(Y+2)]
for y in range(Y,-1,-1): uY[y] = uY[y+1].union(sY[y])

dZ=[set() for _ in range(Z+1)]
for z in range(1,Z+1): dZ[z] = dZ[z-1].union(sZ[z])
uZ=[set() for _ in range(Z+2)]
for z in range(Z,-1,-1): uZ[z] = uZ[z+1].union(sZ[z])

ans = 0
for x in range(1,X+1):
  for s in sX[x].difference(sX[x-1]):
    if s not in dX[x-1]: ans += 1
  for s in sX[x-1].difference(sX[x]):
    if s not in uX[x]: ans += 1
for y in range(1,Y+1):
  for s in sY[y].difference(sY[y-1]):
    if s not in dY[y-1]: ans += 1
  for s in sY[y-1].difference(sY[y]):
    if s not in uY[y]: ans += 1
for z in range(1,Z+1):
  for s in sZ[z].difference(sZ[z-1]):
    if s not in dZ[z-1]: ans += 1
  for s in sZ[z-1].difference(sZ[z]):
    if s not in uZ[z]: ans += 1
print(ans)
