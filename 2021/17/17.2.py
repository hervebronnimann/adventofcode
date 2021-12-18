# tx1=20; tx2=30; ty1=-10; ty2=-5
tx1=70; tx2=96; ty1=-179; ty2=-124

def within(x,y): return tx1<=x and x<=tx2 and ty1<=y and y<=ty2

def trajectory(vx,vy):
  x,y = 0,0
  # print("Vx,vy: %d,%d" % (vx,vy))
  while x<=tx2 and y>=ty1 and not within(x,y):
    x += vx; y += vy
    # print("  -> x,y: %d,%d" % (x,y))
    vx = vx-1 if vx > 0 else vx+1 if vx<0 else 0; vy -= 1
  # if within(x,y): print("  -> HIT %d,%d" % (x,y))
  return within(x,y)

count=0
for vx in range(1,tx2+2):
  for vy in range(2*ty1,2*vx+2*tx2):
    if trajectory(vx,vy): count += 1

print(count)
