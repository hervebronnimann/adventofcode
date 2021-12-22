from functools import reduce

def rsum(a): reduce(lambda x,y: x+rsum(y), a, 0)

with open("input.txt") as f:
  grid=[[[0 for i in range(-50,51)] for j in range(-50,51)] for k in range(-50,51)]
  for l in f:
    s,x1,x2,y1,y2,z1,z2=[int(n) for n in l.strip().split()]
    if x1<-50 or x2>50: continue
    if y1<-50 or y2>50: continue
    if z1<-50 or z2>50: continue
    for x in range(x1,x2+1):
      for y in range(y1,y2+1):
        for z in range(z1,z2+1):
          grid[x+50][y+50][z+50] = s
  sum=0
  for x in range(-50,51):
    for y in range(-50,51):
      for z in range(-50,51):
        sum += grid[x+50][y+50][z+50]
  print(sum)
