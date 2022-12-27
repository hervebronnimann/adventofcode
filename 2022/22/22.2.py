from collections import defaultdict
import re

example = 0
lines = open("example.txt" if example else "input.txt").read().split('\n\n')
grid=lines[0].split('\n')
# print('\n'.join([ '***' + x + '***' for x in grid]))
grid=[list(x) for x in grid]

# HERE WE HAVE SOME KNOWLEDGE THAT ONLY WORKS FOR THE INPUT: IT LOOKS LIKE THIS
#
#                              1111122222
#                              1111122222
#         1111                 1111122222
#         1111                 1111122222
#         1111                 33333
#         1111                 33333
# 222233334444                 33333
# 222233334444                 33333
# 222233334444            4444455555
# 222233334444            4444455555
#         55556666        4444455555
#         55556666        4444455555
#         55556666        66666
#         55556666        66666
#                         66666
#                         66666
#
# So it folds like this with the neighbors inverted and going to T(op) B(ottom) L(eft) or R(ight)
# Explanation:
# - N: side length of each cube
# - Edge: each face is rotated clockwise,right,bottom,left,top
# - M: map of 2D cube corners (top,left)
# - edge(c,d): corner of cube c at beginning/end of edge d (d>0 or d<0), with direction of edge (2d) and along edge (d>0 or d<0)
# - fold(edge1,edge2): how the 2D edges fold along each other

N=0
corresp={}
def fold(N,edge1,edge2):
  x1,y1,dx1,dy1,du1,dv1=edge1
  x2,y2,dx2,dy2,du2,dv2=edge2
  for i in range(N):
    corresp[(x1+i*du1,y1+i*dv1,dx1,dy1)] = (x2+i*du2,y2+i*dv2,-dx2,-dy2)
    corresp[(x2+i*du2,y2+i*dv2,dx2,dy2)] = (x1+i*du1,y1+i*dv1,-dx1,-dy1)

right,bottom,left,top=1,2,3,4
dirs={right:(1,0), bottom:(0,1), left:(-1,0), top:(0,-1)}
cdirs={right:'>', bottom:'v', left:'<', top:'^'}

def edge(N,M,c,d):
  x,y = M[c]
  dx,dy=dirs[abs(d)]
  x = x*N+(N-1 if abs(d) in [right,bottom] else 0)
  y = y*N+(N-1 if abs(d) in [bottom,left] else 0)
  du,dv=dirs[abs(d)%4+1]
  if d<0:
    x,y = x+du*(N-1), y+dv*(N-1)
    du,dv = -du,-dv
  return x,y,dx,dy,du,dv

if example:
  N=4
  M={1:(2,0),2:(0,1),3:(1,1),4:(2,1),5:(2,2),6:(3,2)}
  fold(N,edge(N,M,1,left),edge(N,M,3,-top))
  fold(N,edge(N,M,1,right),edge(N,M,6,-right))
  fold(N,edge(N,M,4,right),edge(N,M,6,-top))
  fold(N,edge(N,M,2,top),edge(N,M,1,-top))
  fold(N,edge(N,M,3,bottom),edge(N,M,5,-left))
  fold(N,edge(N,M,5,bottom),edge(N,M,2,-bottom))
  fold(N,edge(N,M,2,left),edge(N,M,6,-bottom))
else:
  N=50
  M={1:(1,0),2:(2,0),3:(1,1),4:(0,2),5:(1,2),6:(0,3)}
  fold(N,edge(N,M,1,left),edge(N,M,4,-left))
  fold(N,edge(N,M,2,right),edge(N,M,5,-right))
  fold(N,edge(N,M,2,bottom),edge(N,M,3,-right))
  fold(N,edge(N,M,3,left),edge(N,M,4,-top))
  fold(N,edge(N,M,5,bottom),edge(N,M,6,-right))
  fold(N,edge(N,M,6,left),edge(N,M,1,-top))
  fold(N,edge(N,M,6,bottom),edge(N,M,2,-top))
# print(corresp)

# NOW THE ENGINE FOR MOVING ON THE CUBE, AS BEFORE

inst=re.split('(\d+)', lines[1].strip())
inst.remove('')
inst.remove('')
# print(inst)

def rot(dir,dx,dy):
  return (-dy,dx) if dir=='R' else (dy,-dx)

def adv(grid,N,x,y,dx,dy):
  if x+dx>=0 and y+dy>=0 and y+dy<len(grid) and x+dx<len(grid[y+dy]) and grid[y+dy][x+dx]!=' ':
      return (x+dx,y+dy,dx,dy)
  else:
    return corresp[(x,y,dx,dy)]

# Advance to first position, and apply each instruction

x,y,d,dx,dy = 0,0,right,1,0
while x+dx<len(grid[y]) and grid[y][x]==' ': x+=dx
grid[y][x]='X'
# print(f'Starting at {(x,y)} cube side {N}')

for i in inst:
  if i=='R' or i=='L':
    # print(f'Rotate {i}')
    dx,dy = rot(i,dx,dy)
    d = (d%4+1 if i=='R' else (d+2)%4+1)
    grid[y][x]=cdirs[d]
  elif i.isnumeric():
    for _ in range(int(i)):
       x2,y2,dx2,dy2=adv(grid,N,x,y,dx,dy)
       if grid[y2][x2]=='#':
         # print(f'Stop {(x,y)}')
         break
       x,y,dx,dy=x2,y2,dx2,dy2
       for d1 in dirs: d = d1 if dirs[d1]==(dx,dy) else d
       grid[y][x]=cdirs[d]
       # print(f'Advance {(x,y)} dir {(dx,dy)}')
       # print('\n'.join([ '***' + ''.join(x) + '***' for x in grid]))
  else:
    assert False, f'BAD INSTRUCTION {i}'   

dir = 0 if dx==1 else 1 if dy==1 else 2 if dx==-1 else 3
grid[y][x]='Y'
print('\n'.join([ '***' + ''.join(x) + '***' for x in grid]))
print(1000*(y+1)+4*(x+1)+dir)
