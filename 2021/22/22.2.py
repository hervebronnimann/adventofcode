def diff_cube_z_helper(c1,c2):
  x1,x2,y1,y2,z1,z2 = c1
  u1,u2,v1,v2,w1,w2 = c2 
  # Look at y dimension last, guaranteed that x1==u1 and x2==u2, as well as y1==v1 and y2==v2.
  if z1<w1 and w2<z2: return [(x1,x2,y1,y2,z1,w1),(x1,x2,y1,y2,w2,z2)]
  if z1<w1: return [(x1,x2,y1,y2,z1,w1)]
  if w2<z2: return [(x1,x2,y1,y2,w2,z2)]
  # else: w1<=z1 and z2<=w2:
  return []

def diff_cube_y_helper(c1,c2):
  x1,x2,y1,y2,z1,z2 = c1
  u1,u2,v1,v2,w1,w2 = c2 
  # Look at y dimension next, guaranteed that x1==u1 and x2==u2.
  res = []
  if y1<v1 and v2<y2: res = diff_cube_z_helper((x1,x2,v1,v2,z1,z2),c2); res.append((x1,x2,y1,v1,z1,z2)); res.append((x1,x2,v2,y2,z1,z2))
  elif y1<v1: res = diff_cube_z_helper((x1,x2,v1,y2,z1,z2),(x1,x2,v1,v2,w1,w2)); res.append((x1,x2,y1,v1,z1,z2))
  elif v2<y2: res = diff_cube_z_helper((x1,x2,y1,v2,z1,z2),(x1,x2,v1,v2,w1,w2)); res.append((x1,x2,v2,y2,z1,z2))
  else: res = diff_cube_z_helper(c1,(x1,x2,y1,y2,w1,w2))
  return res

def diff_cube_x_helper(c1,c2):
  x1,x2,y1,y2,z1,z2 = c1
  u1,u2,v1,v2,w1,w2 = c2
  # Look at x dimension first:
  res =[]
  if x1<u1 and u2<x2: res = diff_cube_y_helper((u1,u2,y1,y2,z1,z2),c2); res.append((x1,u1,y1,y2,z1,z2)); res.append((u2,x2,y1,y2,z1,z2))
  elif x1<u1: res = diff_cube_y_helper((u1,x2,y1,y2,z1,z2),(u1,x2,v1,v2,w1,w2)); res.append((x1,u1,y1,y2,z1,z2))
  elif u2<x2: res = diff_cube_y_helper((x1,u2,y1,y2,z1,z2),(x1,u2,v1,v2,w1,w2)); res.append((u2,x2,y1,y2,z1,z2))
  else: res = diff_cube_y_helper(c1,(x1,x2,v1,v2,w1,w2))
  return res

def diff_cube(grid,c1,c2):
  ''' Add c1\c2 (extrusion of c2) to grid, as a union (list) of pairwise disjoint cubes. '''
  x1,x2,y1,y2,z1,z2 = c1
  u1,u2,v1,v2,w1,w2 = c2
  # No intersection (separating plane). Thus c1\c2==c1, no modification to grid.
  if u2<=x1 or x2<=u1: return # so that from now on x1<u2 and u1<x2
  if v2<=y1 or y2<=v1: return # so that from now on y1<v2 and v1<y2
  if w2<=z1 or z2<=w1: return # so that from now on z1<w2 and w1<z2
  # we are guaranteed an overlap, so that we can replace c1 by a partition of the difference.
  grid.remove(c1)
  grid.update(diff_cube_x_helper(c1,c2))

with open("input.txt") as f:
  axis=[set() for i in range(0,3)]
  cubes=[]
  ''' Parse the input. '''
  for l in f:
    s,x1,x2,y1,y2,z1,z2=[int(n) for n in l.strip().split()]
    cubes.append(((x1,x2+1,y1,y2+1,z1,z2+1),s))
    axis[0].add(x1); axis[0].add(x2+1)
    axis[1].add(y1); axis[1].add(y2+1)
    axis[2].add(z1); axis[2].add(z2+1)
  ''' Turn on or off the dynamic grid (i.e. set of non-overlapping cubes all turned to 1). '''
  grid=set()
  for c2,s in cubes:
    if s:
      # wanna add c2, but first must remove any portion belonging to c1 in grid.
      g2={c2}
      for c1 in grid:
        for c3 in list(g2):
          diff_cube(g2,c3,c1)
      grid.update(g2)
    else:
      # simpler, remove c2 from every cube in the grid, adding back a partition of the difference.
      for c1 in list(grid):
        diff_cube(grid,c1,c2)
  sum=0
  for x1,x2,y1,y2,z1,z2 in grid:
    sum += (x2-x1)*(y2-y1)*(z2-z1)
  print(sum)
