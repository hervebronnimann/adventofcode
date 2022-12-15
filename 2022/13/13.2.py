from functools import total_ordering

lines = open('input.txt', 'r').read().strip().split('\n\n');
# lines = open('example.txt', 'r').read().strip().split('\n\n');

def compare(p0,p1):
  if type(p0) is int and type(p1) is list:
    return compare([p0],p1)
  if type(p1) is int and type(p0) is list:
    return compare(p0,[p1])
  if type(p0)==type(p1):
    if type(p0) is int:
      return -1 if p0 < p1 else 1 if p0 > p1 else 0
    if type(p0) is list:
      if len(p0)>0 and len(p1)>0:
        c=compare(p0[0],p1[0])
        if c!=0: return c
        return compare(p0[1:],p1[1:])
      if len(p0)==0 and len(p1)==0: return 0
      if len(p0)==0: return -1
      if len(p1)==0: return 1
      return 0
  else:
    return "WTF"

res=[[2],[6]]
for pair in lines:
  p=pair.split('\n')
  res.extend([eval(p[0]), eval(p[1])])

@total_ordering
class compare_wrapper:
  def __init__(self,x): self.x = x
  def __eq__(self,other): return compare(self.x, other.x)==0
  def __lt__(self,other): return compare(self.x, other.x)==-1

def cmp_to_key(compare): return lambda x: compare_wrapper(x)

res = sorted(res, key=cmp_to_key(compare))
n1=(res.index([2])+1)
n2=(res.index([6])+1)
print(n1*n2)
