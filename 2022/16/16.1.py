from collections import defaultdict
from functools import lru_cache


# lines = open("example.txt").read().strip().split('\n');
lines = open("input.txt").read().strip().split('\n');

nodes = [ x.split(' ')[1] for x in lines ]
flow  = [ int(x.split(' ')[5]) for x in lines ]

dest = [ x.split(' ')[10:] for x in lines ]
dest = dict(zip(nodes,dest))

# Compacting the non-zero nodes, by all-pairs

INF = 10000
Dist={}
for x in nodes:
  Dist[(x,x)]=0
  for z in dest[x]:
    Dist[(x,z)]=1
for n in range(len(nodes)):
  Dist2=dict(Dist)
  for x,y1 in Dist.keys():
    for y2,z in Dist.keys():
      if y1!=y2: continue
      if (x,z) in Dist2: Dist2[(x,z)] = min(Dist2[(x,z)],Dist[(x,y1)]+Dist[(y2,z)])
      else: Dist2[(x,z)] = Dist[(x,y1)]+Dist[(y2,z)]
  Dist=Dist2

# now solving problem

Nodes=[]
Flow={}
for n,f in zip(nodes,flow):
  if f!=0: Nodes.append(n); Flow[n]=f

print(Nodes)
print(Dist)

@lru_cache
def explore(minute,node,open_nodes):
  if minute<=1 or len(open_nodes)==len(Nodes): return 0
  ans = 0
  for x in Nodes:
    if x != node and x not in open_nodes:
      ans = max(ans,explore(minute-1-Dist[(node,x)],x,open_nodes.union({node})))
  return (minute-1)*Flow[node] + ans

ans=0
for x in Nodes:
  ans=max(ans,explore(30-Dist[('AA',x)],x,frozenset()))
print(ans)
