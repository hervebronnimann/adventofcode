from itertools import product

def parse(l): x,y,z=l.split(','); return (1+int(x),1+int(y),1+int(z))
lines = set(map(parse, open("input.txt").read().strip().split('\n')))

X=[ max([t[k]+1 for t in lines]) for k in range(3) ]
grid=set(filter(lambda t: t not in lines,[tuple(t) for t in product(range(X[0]+1),range(X[1]+1),range(X[2]+1))]))

n,q,shell=0,[(0,0,0)],set([(0,0,0)])
while n < len(q):
  x,y,z=q[n]
  for dx,dy,dz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
    if (x+dx,y+dy,z+dz) in grid and (x+dx,y+dy,z+dz) not in shell:
      q.append((x+dx,y+dy,z+dz)); shell.add((x+dx,y+dy,z+dz))
  n+=1

dX = [[set([tuple(t[:k]+t[k+1:]) for t in filter(lambda t: t[k]==x, shell)]) for x in range(X[k]+1)] for k in range(3)]
ans = sum([sum([len(dX[k][x].symmetric_difference(dX[k][x-1])) for x in range(1,X[k]+1)]) for k in range(3)])
print(ans)
