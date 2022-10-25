from collections import defaultdict

def sub_axis(s,x1,x2):
  ''' Return a sequence of intervals [(x1,a1),(a1,a2),...,(an,x2)] where each a{i} in s. '''
  ret=[]
  for a1,a2 in s:
    # if x2<=a1: ret.append((x1,x2)); return ret
    # if a1<=x1 and x1<a2: ret.append((x1,a2)); x1=a2
    if x2==a1: ret.append((x1,x2)); return ret
    if x1<a2: ret.append((x1,a2)); x1=a2
  ret.append((x1,x2)); return ret

def split_grid_x(g,u,v):
  g0=list(g); ret={u,v}
  for x1,x2,y1,y2,z1,z2 in g0:
    if v<x1 or x2<=u: continue
    if x1<u and v<x2:
      g.remove((x1,x2,y1,y2,z1,z2))
      g.add((x1,u,y1,y2,z1,z2)); g.add((u,v,y1,y2,z1,z2)); g.add((v,x2,y1,y2,z1,z2))
    elif x1<u:  # but then x2<=v
      g.remove((x1,x2,y1,y2,z1,z2))
      g.add((x1,u,y1,y2,z1,z2)); g.add((u,x2,y1,y2,z1,z2)); ret.add(x2)
    elif v<x2:  # but then u<=x1
      g.remove((x1,x2,y1,y2,z1,z2))
      g.add((x1,v,y1,y2,z1,z2)); g.add((v,x2,y1,y2,z1,z2)); ret.add(x1)
    else: # but then u<=x1 and x2<=v
      ret.add(x1); ret.add(x2)
  return g,sorted(ret)


def split_grid_y(g,u,v):
  g0=list(g); ret={u,v}
  for x1,x2,y1,y2,z1,z2 in g0:
    if v<y1 or y2<=u: continue
    if y1<u and v<y2:
      g.remove((x1,x2,y1,y2,z1,z2))
      g.add((x1,x2,y1,u,z1,z2)); g.add((x1,x2,u,v,z1,z2)); g.add((x1,x2,v,y2,z1,z2))
    elif y1<u:  # but then y2<=v
      g.remove((x1,x2,y1,y2,z1,z2))
      g.add((x1,x2,y1,u,z1,z2)); g.add((x1,x2,u,y2,z1,z2)); ret.add(y2)
    elif v<y2:  # but then u<=y1                   
      g.remove((x1,x2,y1,y2,z1,z2))
      g.add((x1,x2,y1,v,z1,z2)); g.add((x1,x2,v,y2,z1,z2)); ret.add(y1)
    else: # but then u<=y1 and y2<=v
      ret.add(y1); ret.add(y2)
  return g,sorted(ret)

def split_grid_z(g,u,v):
  g0=list(g); ret={u,v}
  for x1,x2,y1,y2,z1,z2 in g0:
    if v<z1 or z2<=u: continue
    if z1<u and v<z2:
      g.remove((x1,x2,y1,y2,z1,z2))
      g.add((x1,x2,y1,y2,z1,u)); g.add((x1,x2,y1,y2,u,v)); g.add((x1,x2,y1,y2,v,z2))
    elif z1<u:  # but then z2<=v
      g.remove((x1,x2,y1,y2,z1,z2))
      g.add((x1,x1,y1,y2,z1,u)); g.add((x1,x2,y1,y2,u,z2)); ret.add(z2)
    elif v<z2:  # but then u<=z1                         
      g.remove((x1,x2,y1,y2,z1,z2))
      g.add((x1,x2,y1,y2,z1,v)); g.add((x1,x2,y1,y2,v,z2)); ret.add(z1)
    else: # but then u<=z1 and z2<=v
      ret.add(z1); ret.add(z2)
  return g,sorted(ret)

with open("example2.txt") as f:
  axis=[set() for i in range(0,3)]
  cubes=[]
  ''' Parse the input. '''
  for l in f:
    s,x1,x2,y1,y2,z1,z2=[int(n) for n in l.strip().split()]
    cubes.append((s,x1,x2+1,y1,y2+1,z1,z2+1))
    axis[0].add(x1); axis[0].add(x2+1)
    axis[1].add(y1); axis[1].add(y2+1)
    axis[2].add(z1); axis[2].add(z2+1)
  ''' Sort each axis into a sorted subdivision. '''
  axis[0]=sorted(axis[0])
  axis[1]=sorted(axis[1])
  axis[2]=sorted(axis[2])
  ''' Turn on or off the dynamic grid (i.e. set of non-overlapping cubes all turned to 1). '''
  grid=set()
  for s,x1,x2,y1,y2,z1,z2 in cubes:
    grid,a0=split_grid_x(grid,x1,x2)
    grid,a1=split_grid_y(grid,y1,y2)
    grid,a2=split_grid_z(grid,z1,z2)
    for x1,x2 in zip(a0,a0[1:]):
      for y1,y2 in zip(a1,a1[1:]):
        for z1,z2 in zip(a2,a2[1:]):
          if s: grid.add((x1,x2,y1,y2,z1,z2))
          else: grid.discard((x1,x2,y1,y2,z1,z2))
  sum=0
  for x1,x2,y1,y2,z1,z2 in grid:
    sum += (x2-x1)*(y2-y1)*(z2-z1)
  print(sum)
