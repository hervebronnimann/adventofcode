from collections import defaultdict
import re

# lines = open("example.txt").read().split('\n\n')
lines = open("input.txt").read().split('\n\n')
grid=lines[0].split('\n')
print('\n'.join([ '***' + x + '***' for x in grid]))

inst=re.split('(\d+)', lines[1].strip())
inst.remove('')
inst.remove('')
print(inst)

def rot(dir,dx,dy):
  return (-dy,dx) if dir=='R' else (dy,-dx)

def adv(grid,x,dx,y,dy):
  if dy==0:
    if x+dx>=0 and x+dx<len(grid[y]) and grid[y][x+dx]!=' ':
      return (x+dx,y)
    while x-dx>=0 and x-dx<len(grid[y]) and grid[y][x-dx]!=' ':
      x -= dx
    return (x,y)
  elif dx==0:
    if y+dy>=0 and y+dy<len(grid) and x<len(grid[y+dy]) and grid[y+dy][x]!=' ':
      return (x,y+dy)
    while y-dy>=0 and y-dy<len(grid) and x<len(grid[y-dy]) and grid[y-dy][x]!=' ':
      y -= dy
    return (x,y)
  else:
    print(f"OOOPS {dx} {dy}")
    exit(-1)

x,y,dx,dy = 0,0,1,0
while x+dx<len(grid[y]) and grid[y][x]==' ': x+=dx
print(x,y)

for i in inst:
  if i=='R' or i=='L':
    # print(f'Rotate {i}')
    dx,dy=rot(i,dx,dy)
  elif i.isnumeric():
    for _ in range(int(i)):
       x2,y2=adv(grid,x,dx,y,dy)
       if grid[y2][x2]=='#':
         # print(f'Stop {(x,y)}')
         break
       x,y=x2,y2
       # print(f'Advance {(x,y)}')
  else:
    print("OOOPS INST")
    exit(-1)

dir = 0 if dx==1 else 1 if dy==1 else 2 if dx==-1 else 3
print(1000*(y+1)+4*(x+1)+dir)
