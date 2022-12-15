from collections import defaultdict

# lines = open("example.txt").read().strip().split('\n'); y = 10
lines = open("input.txt").read().strip().split('\n'); y = 2000000

S = [ (int(x.split(' ')[3]),int(x.split(' ')[5])) for x in lines ]
B = [ (int(x.split(' ')[11]),int(x.split(' ')[13])) for x in lines ]

def manh(x,y):
  return abs(x[0]-y[0])+abs(x[1]-y[1])

X = []
for s,b in zip(S,B):
  d = manh(s,b)
  if abs(s[1]-y) <= d:
    D = d-abs(s[1]-y)
    X.append((s[0]-D,+1))
    X.append((s[0]+D+1,-1))

for b in set(B):
  if b[1]==y:
    X.append((b[0],0))

X = sorted(X,key=lambda x:(x[0],-x[1]))
print(X)

i = 0
sx,n=0,0
for x in X:
  if x[1]==0 and i>0:
    n -= 1; continue
  if i==0: sx=x[0]
  i += x[1]
  if i==0: n += x[0]-sx
  

print(n)
