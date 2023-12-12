from functools import cache

input = open("example.txt",'r').read().strip().split('\n')
input = open("input.txt",'r').read().strip().split('\n')

@cache
def n0(x:str,n:tuple):
  if len(n) == 0: return 1 if '#' not in x else 0
  if len(x) == 0: return 0  # because len(n)>0
  if len(x) < n[0]: return 0
  if len(x) == n[0]: return 1 if '.' not in x and len(n)== 1 else 0
  if x[0] == '.': return n0(x[1:],n)
  if x[0] == '#':
    if '.' not in x[0:n[0]] and x[n[0]] in "?.": return n0(x[n[0]+1:],n[1:])
    return 0
  if x[0]=='?':
    return n0(x[1:],n) + n0("#"+x[1:],n)
  return 0
    

def num(x:str):
  s1,n1 = x.split(" ")
  n1 = [ int(x) for x in n1.split(',')]
  s = s1
  n = n1
  for i in range(4):
    s1 = s1+'?'+s
    n1 = n1+n
  return n0(s1,tuple(n1))

print(sum([num(x) for x in input]))
