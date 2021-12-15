dots={}
with open("input.txt") as f:
  for l in f:
    if l=='\n': break
    x=l.rstrip('\n').split(',')
    dots[tuple(map(int,x))]=1
  iter=0
  for l in f:
    iter += 1
    x=l.rstrip('\n').split(' ')[-1].split('=')
    t=int(x[1])
    if x[0]=='x':
      for i,j in dots.keys():
        if i>t: del dots[(i,j)]; dots[(2*t-i,j)]=1
    if x[0]=='y':
      for i,j in dots.keys():
        if j>t: del dots[(i,j)]; dots[(i,2*t-j)]=1
    print("Iter: %d dots:%d" % (iter,len(dots)))

x,y = zip(*dots.keys())
for l in [[('#' if (i,j) in dots.keys() else '.')
           for i in range(max(x)+1)]
           for j in range(max(y)+1)]:
  print("".join(l))
