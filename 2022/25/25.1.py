example=0
lines=open("example.txt" if example else "input.txt").read().strip().split('\n')

digit={'=':-2,'-':-1,'0':0,'1':1,'2':2}
inv={-2:'=',-1:'-',0:'0',1:'1',2:'2'}
def conv5(x): return list(reversed([digit[d] for d in x]))
def cinv5(x): return str(reversed([inv[d] for d in x]))

def dec5(x):
  x = [digit[d] for d in x]
  r,p = 0,1
  while len(x)>0:
    r += p*x[-1]
    p *= 5
    x.pop()
  return r

def inv5(x):
  r = ''
  while x!=0:
    d=(x+2)%5-2
    r=inv[d]+r
    x=(x-d)//5
  return r

def add5(x,y):
  if len(x)<len(y): x += [0]*(len(y)-len(x))
  if len(y)<len(x): y += [0]*(len(x)-len(y))
  c,r=0,[]
  for a,b in zip(x,y):
    m=(a+b+c+2)%5-2
    c=(a+b+c-m)//5
    r.append(m)
  if c!=0:
    r.append(c)
  while r[-1]==0: r.pop()
  return r

r=0
for x in lines:
  print((x,dec5(x)))
  r += dec5(x)
  print((r,inv5(r),dec5(inv5(r))))
