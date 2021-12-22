from collections import defaultdict

def sort_axis(s):
  ''' For a set s, return a sequence of intervals [(a1,a2),(a2,a3),...,(a{n-1},an)]. '''
  s=sorted(s)
  ret=[]; last=None
  for x in s:
    if last: ret.append((last,x))
    last=x
  return ret

def sub_axis(s,x1,x2):
  ''' Return a sequence of intervals [(x1,a1),(a1,a2),...,(an,x2)] where each a{i} in s. '''
  ret=[]
  for a1,a2 in s:
    # if x2<=a1: ret.append((x1,x2)); return ret
    # if a1<=x1 and x1<a2: ret.append((x1,a2)); x1=a2
    if x2==a1: ret.append((x1,x2)); return ret
    if x1<a2: ret.append((x1,a2)); x1=a2
  ret.append((x1,x2)); return ret

with open("input.txt") as f:
  axis=[set() for i in range(0,3)]
  cubes=[]
  ''' Parse the input. '''
  for l in f:
    s,x1,x2,y1,y2,z1,z2=[int(n) for n in l.strip().split()]
    cubes.append((s,x1,x2+1,y1,y2+1,z1,z2+1))
    axis[0].add(x1); axis[0].add(x2+1)
    axis[1].add(y1); axis[1].add(y2+1)
    axis[2].add(z1); axis[2].add(z2+1)
  ''' Sort each axis into a subdivision. '''
  axis[0]=sort_axis(axis[0])
  axis[1]=sort_axis(axis[1])
  axis[2]=sort_axis(axis[2])
  ''' Turn on or off the grid. '''
  grid=set()
  for s,x1,x2,y1,y2,z1,z2 in cubes:
    a0=sub_axis(axis[0],x1,x2)
    a1=sub_axis(axis[1],y1,y2)
    a2=sub_axis(axis[2],z1,z2)
    for x1,x2 in a0:
      for y1,y2 in a1:
        for z1,z2 in a2:
          if s: grid.add((x1,x2,y1,y2,z1,z2))
          else: grid.discard((x1,x2,y1,y2,z1,z2))
  sum=0
  for x1,x2,y1,y2,z1,z2 in grid:
    sum += (x2-x1)*(y2-y1)*(z2-z1)
  print(sum)
