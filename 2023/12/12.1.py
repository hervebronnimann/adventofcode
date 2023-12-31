from functools import cache

input = open("input.txt",'r').read().strip().split('\n')

def n0(x:str,n:list):
  if len(n) == 0: return 1 if '#' not in x else 0
  elif len(x) == 0: return 0  # because len(n)>0
  elif len(x) < n[0]: return 0
  elif len(x) == n[0]: return 1 if '.' not in x and len(n)== 1 else 0
  elif x[0] == '.': return n0(x[1:],n)
  elif x[0] == '#':
    if '.' not in x[0:n[0]] and x[n[0]] in "?.":
      return n0(x[n[0]+1:],n[1:])
    return 0
  elif x[0]=='?':
    return n0(x[1:],n) + n0("#"+x[1:],n)
  return 0


def num(x:str):
  s,n = x.split()
  n = [ int(x) for x in n.split(',')]
  return n0(s,n)

print(sum([num(x) for x in input]))
