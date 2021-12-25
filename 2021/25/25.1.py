trench=[]
with open('input.txt') as f:
  for l in f:
    trench.append(list(l.strip()))

def print_trench(trench):
  for l in trench:
    print(''.join(l))

m=len(trench); n=len(trench[0])
print(m,n)
# print('Initial state:')
# print_trench(trench)

def shift_left(trench):
  s=[]
  for i in range(m):
    for j in range(n):
      if trench[i][j]!='>': continue
      if trench[i][(j+1)%n]=='.': s.append((i,j))
  for i,j in s:
    trench[i][j]='.'; trench[i][(j+1)%n]='>'
  return len(s)

def shift_down(trench):
  s=[]
  for i in range(m):
    for j in range(n):
      if trench[i][j]!='v': continue
      if trench[(i+1)%m][j]=='.': s.append((i,j))
  for i,j in s:
    trench[i][j]='.'; trench[(i+1)%m][j]='v'
  return len(s)

t=0
while True:
  t=t+1
  lmoves=shift_left(trench)
  dmoves=shift_down(trench)
  # print('\nAfter %d step%s:' % (t, '' if t==1 else 's'))
  # print_trench(trench)
  if lmoves+dmoves==0: break;

print(t)
