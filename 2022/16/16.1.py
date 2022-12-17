from collections import defaultdict
from functools import lru_cache

# lines = open("example.txt").read().strip().split('\n');
lines = open("input.txt").read().strip().split('\n');

nodes = [ x.split(' ')[1] for x in lines ]
flow  = [ int(x.split(' ')[5]) for x in lines ]

dest = [ x.split(' ')[10:] for x in lines ]
dest = dict(zip(nodes,dest))

# Compacting the non-zero nodes, by all-pairs (Floyd-Warshall)

Dist={}
for x in nodes:
  Dist[(x,x)]=0
  for z in dest[x]: Dist[(x,z)]=1
for n in range(len(nodes)):
  Dist2=dict(Dist)
  for x,y1 in Dist.keys():
    for y2,z in Dist.keys():
      if y1!=y2: continue
      if (x,z) in Dist2: Dist2[(x,z)] = min(Dist2[(x,z)],Dist[(x,y1)]+Dist[(y2,z)])
      else: Dist2[(x,z)] = Dist[(x,y1)]+Dist[(y2,z)]
  if Dist==Dist2: break
  Dist=Dist2

# and indexing with non-zero flow nodes from 1 to N

index=0
Nodes=[]
Index={'AA':0}
Flow={}
for n,f in zip(nodes,flow):
  if f!=0: index += 1; Nodes.append(index); Flow[index]=f; Index[n]=index
print(Nodes)
print(Flow)

IDist = [[0 for _ in range(index+1)] for _ in range(index+1)]
for n1,f1 in zip(nodes,flow):
  if n1!='AA' and f1==0: continue
  for n2,f2 in zip(nodes,flow):
    if n2!='AA' and f2==0: continue
    IDist[Index[n1]][Index[n2]] = Dist[(n1,n2)]
print(IDist)

# now solving problem

# @lru_cache
def explore(minute,node,open_nodes,num_open_nodes):
  if minute<=1 or num_open_nodes==len(Nodes): return 0
  ans = 0
  for x in Nodes:
    if x != node and (2**Nodes.index(x))&open_nodes==0:
      ans = max(ans,explore(minute-1-IDist[node][x],x,open_nodes|(2**Nodes.index(node)),num_open_nodes+1))
  return (minute-1)*Flow[node] + ans

ans=0
for x in Nodes:
  ans=max(ans,explore(30-IDist[0][x],x,0,0))
print(ans)
