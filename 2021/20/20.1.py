from functools import reduce

def btod(str): return reduce(lambda x,y: 2*x+int(y), str, 0)
def atos(array): return reduce(lambda x,y: x+y, array, '')


def p(s):
  print('   ------')
  for l in s: print(l)
  print('   ------')

def pad(s,c,p):
  ''' Add p copies of c on each side of s. '''
  for i in range(len(s)):
     for j in range(p): s[i]=c+s[i]+c
  empty=atos([c for j in range(len(s[0]))])
  for j in range(p):
    s.insert(0, empty); s.append(empty)

def decode(s,m,n,pattern):
  ''' Return a extended (+1 on each side) decoded copy of m*n grid s, according to pattern. '''
  def neighbor(s,i,j):
    i += 1; j += 1
    return (s[i-1][j-1:j+2]+s[i][j-1:j+2]+s[i+1][j-1:j+2]).replace('.','0').replace('#','1')
  return [atos([pattern[btod(neighbor(s,i,j))] for j in range(n+2)]) for i in range(m+2)]

def solve(filename):
  ''' Load pattern and grid from file, and apply decode twice with the appropriate padding in between. '''
  s=[]
  with open(filename) as f:
    pattern=next(f).strip()
    c=pattern[0]
    next(f)
    for l in f: s.append(l.strip())
    # First iteration, padding with '.'
    m=len(s); n=len(s[0])
    pad(s,'.',2); p(s)
    s=decode(s,m,n,pattern)
    # Next iteration, this time padding with c, not '.'
    m=len(s); n=len(s[0])
    pad(s,c,2); p(s)
    s=decode(s,m,n,pattern);
    pad(s,'.',2); p(s)
    count=reduce(lambda x,y: x+y.count('#'), s, 0)
    print('SOLVED: %d for %s' % (count, filename))

solve('example.txt')
solve('input.txt')
