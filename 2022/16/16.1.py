from collections import defaultdict

lines = open("example.txt").read().strip().split('\n');
# lines = open("input.txt").read().strip().split('\n');

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

Dist2={}
for x,y in Dist:
  if x=='AA' or x in Nodes:
    if y in Nodes:
      Dist2[(x,y)]=Dist[(x,y)]
print(Nodes)
print(Dist2)

# Recursive search - explodes and does not even finish on the example...

def explore(minute,node,ans,open_nodes):
  if minute<=0:
    return ans
  if node in Nodes and node not in open_nodes:
    ans=max(ans,explore(minute-1,node,ans+(minute-1)*Flow[node],open_nodes+[node]))
  if len(open_nodes)<len(Nodes):
    for x in Nodes:
      if x != node: ans = max(ans,explore(minute-Dist[(node,x)],x,ans,open_nodes))
  return ans

print(explore(30,'AA',0,[]))
