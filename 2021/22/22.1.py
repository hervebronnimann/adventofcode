from collections import defaultdict

grid=defaultdict(int)
with open("input.txt") as f:
  for l in f:
    s,x1,x2,y1,y2,z1,z2=[int(n) for n in l.strip().split()]
    if x1<-50 or x2>50: continue
    if y1<-50 or y2>50: continue
    if z1<-50 or z2>50: continue
    for x in range(x1,x2+1):
      for y in range(y1,y2+1):
        for z in range(z1,z2+1):
          grid[(x,y,z)] = s
  print(sum(grid.values()))
