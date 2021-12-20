from functools import reduce

def btod(str): return reduce(lambda x,y: 2*x+int(y), str, 0)
def atos(array): return reduce(lambda x,y: x+y, array, '')

def neighbor(s,i,j):
  def helper(i,j):
    m=len(s); n=len(s[0])
    if i<=1 or i>=m+2: return '...'
    if j==0:   return '..'+s[i-2][0:1]
    if j==1:   return '.'+s[i-2][0:2]
    if j==n+2: return s[i-2][n-2:n]+'.'
    if j==n+3: return s[i-2][n-1:n]+'..'
    return s[i-2][j-2:j+1]
  t=helper(i,j)+helper(i+1,j)+helper(i+2,j)
  return t.replace('.','0').replace('#','1')

def p(s):
  print('   ------')
  for l in s: print(l)
  print('   ------')

def decode(s,pattern):
  m=len(s)+4; n=len(s[0])+4
  o=[[pattern[btod(neighbor(s,i,j))] for j in range(n)] for i in range(m)]
  return [atos(o[i]) for i in range(m)] 

def solve(filename):
  s=[]
  with open(filename) as f:
    pattern=next(f).strip()
    next(f)
    for l in f:
      s.append(l.strip())
    p(s)
    s=decode(s,pattern); p(s)
    s=decode(s,pattern); p(s)
    count=reduce(lambda x,y: x+y.count('#'), s, 0)
    print('SOLVED: %d for %s' % (count, filename))

solve('example.txt')
solve('input.txt')
