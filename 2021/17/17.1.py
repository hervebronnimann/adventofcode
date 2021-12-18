tx1=70;
tx2=96;
ty1=-179;
ty2=-124

def within(x,y): return tx1<=x and x<=tx2 and ty1<=y and y<=ty2

def trajectory(vx,vy):
  t=[]; t.append((0,0))
  x,y = 0,0
  while x<=tx2 and y>=ty2 and not within(x,y):
    x += vx; y += vy
    vx = vx-1 if vx > 0 else vx+1 if vx<0 else 0; vy -= 1
    t.append((x,y))
  return within(x,y), t

maxy=0
for vx in range(1,tx1+1):
  for vy in range(1,1000):
    w,t = trajectory(vx,vy)
    if w:
      maxy1,maxy=maxy,max(maxy,max(map(lambda v: v[1],t)))
      if maxy>maxy1: print(maxy1)

print(maxy)
