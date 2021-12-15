dots=[]
with open("input.txt") as f:
  for l in f:
    if l=='\n': break
    dots.append(map(int,l.strip().split(',')))
  for l in f:
    dir,t = l.strip().replace('=',' ').split()[-2:]
    for xy in dots:
      if dir=='x' and xy[0]>t: xy[0]=2*int(t)-xy[0]
      if dir=='y' and xy[1]>t: xy[1]=2*int(t)-xy[1]

x,y = zip(*dots)
grid = set(zip(x,y))
for l in [[('#' if (i,j) in grid else ' ')
           for i in range(max(x)+1)]
           for j in range(max(y)+1)]:
  print("".join(l))
