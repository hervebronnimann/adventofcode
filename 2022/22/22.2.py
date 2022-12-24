from collections import defaultdict
import re

# lines = open("example.txt").read().split('\n\n')
lines = open("input.txt").read().split('\n\n')
grid=lines[0].split('\n')
print('\n'.join([ '***' + x + '***' for x in grid]))

# HERE WE HAVE SOME KNOWLEDGE THAT ONLY WORKS FOR THE INPUT: IT LOOKS LIKE THIS
#
#            1...12....2
#        (4L).   ..    .(5R)
#        (4L).   ..    .(5R)
#            1...12....2
#            3...3 (3R)
#        (4T).   .(2B)  
#        (4T).   .(2B)
#       (3L) 3...3
#       4...45...5
#   (1L).   ..   .(2R)
#   (1L).   ..   .(2R)
#       4...45...5
#       6...6 (6R)
#       .   .(6R)
#       .   .(5B)
#       6...6
#
# So it folds like this with the neighbors inverted and going to T(op) B(ottom) L(eft) or R(ight)

inst=re.split('(\d+)', lines[1].strip())
inst.remove('')
inst.remove('')
print(inst)

def rot(dir,dx,dy):
  return (-dy,dx) if dir=='R' else (dy,-dx)

def adv(grid,N,x,y,dx,dy):
  if dy==0:
    if x+dx>=0 and x+dx<len(grid[y]) and grid[y][x+dx]!=' ':
      return (x+dx,y,dx,dy)
    if y<N and dx==-1: # 1, connects to 4 (left)
      assert 0<=y and x==N, f'Position ({x},{y}) direction ({dx},{dy})'
      y=3*N-1-y; x=0; dx=1
    elif y<N and dx==1: # 2, connects to 5 (right)
      assert 0<=y and x==3*N-1, f'Position ({x},{y}) direction ({dx},{dy})'
      y=3*N-1-y; x=2*N-1; dx=-1
    elif y<2*N and dx==-1: # 3, connects to 4 (top)
      assert N<=y and x==N, f'Position ({x},{y}) direction ({dx},{dy})'
      x=y-N; y=2*N; dx,dy=0,1
    elif y<2*N and dx==1: # 3, connects to 2 (bottom)
      assert N<=y and x==2*N-1, f'Position ({x},{y}) direction ({dx},{dy})'
      x=y+N; y=N-1; dx,dy=0,-1
    elif y<3*N and dx==-1: # 4, connects to 1 (left)
      assert 2*N<=y and x==0, f'Position ({x},{y}) direction ({dx},{dy})'
      x+=N; y=N-1; dx=1
    elif y<3*N and dx==1: # 5, connects to 2 (right)
      assert 2*N<=y and x==2*N-1, f'Position ({x},{y}) direction ({dx},{dy})'
      y=3*N-1-y; x+=N; dx=-1
    elif y<4*N and dx==-1: # 6, connects to 1 (top)
      assert 3*N<=y and x==0, f'Position ({x},{y}) direction ({dx},{dy})'
      x=y-2*N; y=0; dx,dy=0,1
    elif y<4*N and dx==1: # 6, connects to 5 (bottom)
      assert 3*N<=y and x==N-1, f'Position ({x},{y}) direction ({dx},{dy})'
      x=y-2*N; y=3*N-1; dx,dy=0,-1
    else:
      assert 0<=y<=4*N, f'Position ({x},{y}) direction ({dx},{dy})'
    return (x,y,dx,dy)
  elif dx==0:
    if y+dy>=0 and y+dy<len(grid) and x<len(grid[y+dy]) and grid[y+dy][x]!=' ':
      return (x,y+dy,dx,dy)
    if x<N and dy==-1: # 4, connects to 3 (left)
      assert 0<=x and y==2*N, f'Position ({x},{y}) direction ({dx},{dy})'
      y=x+N; x=N; dx,dy=1,0
    elif x<N and dy==1: # 6, connects to 2 (top)
      assert 0<=x and y==4*N-1, f'Position ({x},{y}) direction ({dx},{dy})'
      x=x+2*N; y=0; dy=1
    elif x<2*N and dy==-1: # 1, connects to 6 (left)
      assert N<=x and y==0, f'Position ({x},{y}) direction ({dx},{dy})'
      y=x+2*N; x=0; dx,dy=1,0
    elif x<2*N and dy==1: # 5, connects to 6 (right)
      assert N<=x and y==3*N-1, f'Position ({x},{y}) direction ({dx},{dy})'
      y=x+2*N; x=N-1; dx,dy=-1,0
    elif x<3*N and dy==-1: # 2, connects to 6 (bottom)
      assert 2*N<=x and y==0, f'Position ({x},{y}) direction ({dx},{dy})'
      x=x-2*N; y=4*N-1; dy=-1
    elif x<3*N and dy==1: # 2, connects to 3 (right)
      assert 2*N<=x and y==N-1, f'Position ({x},{y}) direction ({dx},{dy})'
      y=x-N; x=2*N-1; dx,dy=-1,0
    else:
      assert 0<=x<=3*N, f'Position ({x},{y}) direction ({dx},{dy})'
    return (x,y,dx,dy)
  else:
    assert dx==0 or dy==0

x,y,dx,dy = 0,0,1,0
while x+dx<len(grid[y]) and grid[y][x]==' ': x+=dx
N=x
print(x,y,N)

for i in inst:
  if i=='R' or i=='L':
    # print(f'Rotate {i}')
    dx,dy=rot(i,dx,dy)
  elif i.isnumeric():
    for _ in range(int(i)):
       x2,y2,dx2,dy2=adv(grid,N,x,y,dx,dy)
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
