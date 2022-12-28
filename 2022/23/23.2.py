example=1
lines=open("example.txt" if example else "input.txt").read().strip().split('\n')

i=0
elves=set()
for x in lines:
  for j in range(len(x)):
    if x[j]=='#': elves.add((j,i))
  i+=1

def print_elves(elves):
  xmin=min([x for x,_ in elves])
  xmax=max([x for x,_ in elves])
  ymin=min([y for _,y in elves])
  ymax=max([y for _,y in elves])
  s = '\n'.join([''.join(['#' if (x,y) in elves else '.' for x in range(xmin,xmax+1)]) for y in range(ymin,ymax+1)])
  return s

def alone(e,x,y):
  for dx in [-1,0,1]:
    for dy in [-1,0,1]:
      if dx==0 and dy==0: continue
      if (x+dx,y+dy) in e: return False
  return True

def dir(e,x,y,dx,dy):
  if dx==0:
    return not((x-1,y+dy) in e or (x,y+dy) in e or (x+1,y+dy) in e)
  if dy==0:
    return not((x+dx,y-1) in e or (x+dx,y) in e or (x+dx,y+1) in e)
  assert dx==0 or dy==0

def propose(e,x,y,dirs):
  if alone(e,x,y):
    return x,y
  for dx,dy in dirs:
    if dir(e,x,y,dx,dy):
      return x+dx,y+dy
  return x,y

if example==1: print(f'Initial round 1:\n{print_elves(elves)}\n')
dirs = [(0,-1),(0,1),(-1,0),(1,0)]

N=0
while True:
  E=dict([((x,y),propose(elves,x,y,dirs)) for x,y in elves])
  C=dict()
  for p in E.values():
    if p not in C: C[p]=0
    C[p]+=1
  keep_going=False
  elves2=set()
  dirs2=dirs[1:]+[dirs[0]]
  for e,p in E.items():
    p = e if C[p]>1 else p
    if p!=e: keep_going=True
    elves2.add(p)
  elves=elves2 
  dirs=dirs2
  N+=1
  s = print_elves(elves)
  if example==1: print(f'After round {N+1}:\n{s}\n')
  if not keep_going:
    print('Two consecutive identical grids, stop.')
    break

print(N)

