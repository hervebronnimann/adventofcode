from collections import defaultdict
from functools import lru_cache

# lines = open("example.txt").read().strip()
lines = open("input.txt").read().strip()
print(lines)

# rocks are indexed by their bottom,left corner
rocks=[x.split('\n') for x in [
'####',
'.#.\n###\n.#.',
'###\n..#\n..#',
'#\n#\n#\n#',
'##\n##',
] ]

# rocks are indexed by their bottom,left corner
nrocks=len(rocks)
rockdims=[(len(x),len(x[0])) for x in rocks] # [(1,4),(3,3),(3,3),(4,1),(2,2)]

# Prefill grid for 2022 pieces, top empty row is 1 initially
# use sentinels! Each rock appears at column 6 on rop top+3
grid = [  list('####.......####') for _ in range(20000)]
grid[0] = list('###############')
top=1

# Rock position is bottom,left corner
def overlap(r,x,y,draw=False):
  for u in range(len(r)):
    for v in range(len(r[u])):
      if r[u][v]=='#':
        if draw: grid[y+u][x+v]=r[u][v]
	elif grid[y+u][x+v]!='.': return True
  return False

r,j=0,0
for i in range(2022):
  rock,x,y = rocks[r],6,top+3
  if overlap(rock,x,y): print('ERROR')
  # print(f'>>>>> STEP {r}: falls at {x},{y}')
  while True:
    d = 1 if lines[j]=='>' else -1
    if not overlap(rock,x+d,y):
      # print(f'  STEP {r}: Move {lines[j]}')
      x += d
    j = (j+1) % len(lines)
    if overlap(rock,x,y-1): break
    y -= 1
    # print(f'  STEP {r}: falls to {x},{y}')
  overlap(rock,x,y,draw=True)
  top = max(top,y+len(rock))
  r = (r+1) % len(rocks)
  # print('\n'.join( ''.join(x[4:11]) for x in reversed(grid[1:top+2])))

print(top-1)
