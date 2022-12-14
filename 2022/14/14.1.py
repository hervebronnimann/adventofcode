from collections import defaultdict

# lines = open("example.txt").read().strip().split('\n')
lines = open("input.txt").read().strip().split('\n')

M0=500
M1=500
N=0
grid = defaultdict(lambda: '.')
grid[(N,M0)] = '+'

def draw(s,e):
  for i in range(min(s[1],e[1]),max(s[1],e[1])+1):
    for j in range(min(s[0],e[0]),max(s[0],e[0])+1):
      grid[(i,j)]='#'

def pict(N,M0,M1):
  return '\n'.join([''.join([grid[(i,j)] for j in range(M0,M1+1)]) for i in range(N+1)])

def fall(step,N,M0,M1):
  i,j=0,500
  while i <= N:
    i+=1
    if grid[(i,j)]=='.': continue
    if grid[(i,j-1)]=='.': j -= 1; continue
    if grid[(i,j+1)]=='.': j += 1; continue
    grid[(i-1,j)]='o';
    # print(f'Step {step}\n{pict(N,M0,M1)}')
    return True
  return False

for x in lines:
  s = [ tuple(map(int,y.split(','))) for y in x.split(' -> ')]
  N = max(N,max([x[1] for x in s]))
  M0= min(M0,min([x[0] for x in s]))
  M1= max(M1,max([x[0] for x in s]))
  for i in range(1,len(s)): draw(s[i-1],s[i])

step=0
while fall(step,N,M0,M1):
  step += 1
# print(f'Step {step}\n{pict(N,M0,M1)}')
print(step)
