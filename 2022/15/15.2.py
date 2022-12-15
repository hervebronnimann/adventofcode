from collections import defaultdict

# lines = open("example.txt").read().strip().split('\n'); maxy = 20
lines = open("input.txt").read().strip().split('\n'); maxy = 4000000

S = [ (int(x.split(' ')[3]),int(x.split(' ')[5])) for x in lines ]
B = [ (int(x.split(' ')[11]),int(x.split(' ')[13])) for x in lines ]
Buniq = set(B)

def manh(x,y):
  return abs(x[0]-y[0])+abs(x[1]-y[1])

def impossible(y):
  X = []
  for s,b in zip(S,B):
    d = manh(s,b)
    if abs(s[1]-y) <= d:
      D = d-abs(s[1]-y)
      X.append((max(0,s[0]-D),+1))
      X.append((min(s[0]+D,maxy)+1,-1))

  Y = []
  for b in Buniq:
    if b[1]==y and b[0]>=0 and b[0]<=maxy:
      Y.append((b[0],0))

  X.extend(Y)
  X = sorted(X,key=lambda x:(x[0],-x[1]))

  i = 0
  posx,sx,n=0,0,0
  for x in X:
    if x[1]==0 and i>0:
      n -= 1; continue
    if i==0:
      sx=x[0]
      if 0<= posx and posx < sx: print(posx)
    i += x[1]
    if i==0:
      n += x[0]-sx; posx = x[0]
    
  return n+len(Y)

for y in range(maxy+1):
  if impossible(y) < maxy+1: print(y)

