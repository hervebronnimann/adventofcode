dots={}
with open("example.txt") as f:
  for l in f:
    if l=='\n': break
    x=l.rstrip('\n').split(',')
    dots[(int(x[0]),int(x[1]))]=1
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


x=[]; y=[]
for i,j in dots.keys():
  x.append(i)
  y.append(j)
xmax=max(x)
ymax=max(y)
print(xmax)
print(ymax)
print(dots)

mat=[['.' for i in range(xmax+1)] for j in range(ymax+1)]
for i,j in dots.keys():
  mat[j][i]='#'
for i in range(ymax+1):
  print("".join(mat[i]))
