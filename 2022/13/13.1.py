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

res=0
n=0
for pair in lines:
  n += 1
  p=pair.split('\n')
  p0=eval(p[0])
  p1=eval(p[1])
  c = compare(p0,p1)
  print(f'Found {c} for {p0} < {p1}')
  res += n if c==-1 else 0

print(res)
