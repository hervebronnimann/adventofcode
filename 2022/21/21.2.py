# X= dict(list(map(lambda x:x.split(': '), open("example.txt").read().strip().split('\n'))))
X= dict(list(map(lambda x:x.split(': '), open("input.txt").read().strip().split('\n'))))
val = dict([(x,int(y)) for x,y in X.items() if y.isnumeric()])

def plus(y,z):
  if isinstance(y,tuple): return (y[0]+z*y[2],y[1]+z*y[3],y[2],y[3])
  if isinstance(z,tuple): return plus(z,y)
  return y+z

def minus1(z): return (-z[0],-z[1],z[2],z[3]) if isinstance(z,tuple) else -z
def minus(y,z): return plus(y,minus1(z))

def times(y,z):
  if isinstance(y,tuple): return (y[0]*z,y[1]*z,y[2],y[3])
  if isinstance(z,tuple): return times(z,y)
  return y*z

def recip(z): return (z[2],z[3],z[0],z[1]) if isinstance(z,tuple) else 1/z
def div(y,z): return times(y,recip(z))

def ev(x):
  if x=='humn': return (1,0,0,1) # human is represented by (a,b,c,d) where value is (h*a+b)/(h*c+d) 
  if x in val: return val[x]
  y,op,z=X[x].split(' ')
  y=ev(y)
  z=ev(z)
  if op=='+': return plus(y,z)
  if op=='-': return minus(y,z)
  if op=='*': return times(y,z)
  if op=='/': return div(y,z)
  print(f'Unknown op {op}')

r=X['root'].split(' ')
x=ev(r[0]); y=ev(r[2])
if isinstance(y,tuple): x,y=y,x
print(x)
print(y)
print((y*x[3]-x[1])/(x[0]-y*x[2]))

