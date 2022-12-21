# X= dict(list(map(lambda x:x.split(': '), open("example.txt").read().strip().split('\n'))))
X= dict(list(map(lambda x:x.split(': '), open("input.txt").read().strip().split('\n'))))
print(X)
N = len(X)

val = dict([(x,int(y)) for x,y in X.items() if y.isnumeric()])
print(val)

def ev(x):
  if x in val: return val[x]
  y,op,z=X[x].split(' ')
  y=ev(y)
  z=ev(z)
  if op=='+': return y+z
  if op=='-': return y-z
  if op=='*': return y*z
  if op=='/': return y/z
  print(f'Unknown op {op}')
  return 0

print(ev('root'))
