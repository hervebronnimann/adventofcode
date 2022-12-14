from collections import defaultdict

# lines = open("example.txt").read().strip().split('\n')
lines = open("input.txt").read().strip().split('\n')

M0=500
M1=500
N=0
grid = defaultdict(lambda: '.')
grid[(N,M0)] = '+'

def vdraw(j,si,ei):
  if si<ei:
    while si<=ei:
      grid[(si,j)]='#'; si += 1
  else:
    while si>=ei:
      grid[(si,j)]='#'; si -= 1

def hdraw(i,sj,ej):
  if sj<ej:
    while sj<=ej:
      grid[(i,sj)]='#'; sj += 1
  else:
    while sj>=ej:
      grid[(i,sj)]='#'; sj -= 1

def draw(s,e):
  if s[0]==e[0]: vdraw(s[0],s[1],e[1])
  elif s[1]==e[1]: hdraw(s[1],s[0],e[0])
  else:  raise('non horizontal or vertical move')

def pict(N,M0,M1):
  return '\n'.join([''.join([grid[(i,j)] for j in range(M0,M1+1)]) for i in range(N+1)])

def fall(step,N,M0,M1):
  i,j=0,500
  while i <= N:
    i+=1
    if grid[(i,j)]=='.': continue
    if grid[(i,j-1)]=='.': j -= 1; continue
    if grid[(i,j+1)]=='.': j += 1; continue
    grid[(i-1,j)]='o'; M0=min(M0,j); M1=max(M1,j)
    # print(f'Step {step}\n{pict(N+1,M0,M1)}')
    return M0,M1
  grid[(i,j)]='o'; M0=min(M0,j); M1=max(M1,j)
  return M0,M1

for x in lines:
  s = [ tuple(map(int,y.split(','))) for y in x.split(' -> ')]
  N = max(N,max([x[1] for x in s]))
  M0= min(M0,min([x[0] for x in s]))
  M1= max(M1,max([x[0] for x in s]))
  for i in range(1,len(s)): draw(s[i-1],s[i])

step=0
while grid[(0,500)]=='+':
  M0,M1=fall(step,N,M0,M1)
  step += 1
# print(f'Step {step}\n{pict(N+1,M0,M1)}')
print(step)
