# X= list(map(lambda x: int(x)*811589153, open("example.txt").read().strip().split('\n')))
X= list(map(lambda x: int(x)*811589153, open("input.txt").read().strip().split('\n')))
N = len(X)

X = list(zip(X,range(N)))
# print(X)

def find_n(i,X):
  return list(map(lambda x: x[1],X)).index(i)

def move_n(i,X):
  j = (3*N*811589153+(i+X[i][0])%(N-1))%N
  # print(f'Move {i}({X[i]}) by {X[i][0]} to {j}({X[j]})')
  if j<i:   X=X[0:j]+[X[i]]+X[j:i]+X[i+1:]
  elif i<j: X=X[0:i]+X[i+1:j+1]+[X[i]]+X[j+1:]
  return X

for k in range(10):
  print(f'Round {k}')
  for i in range(N): X=move_n(find_n(i,X),X)
  # print([x[0] for x in X])
i0 = list(map(lambda x: x[0],X)).index(0)
print(X[(i0+1000)%N][0]+X[(i0+2000)%N][0]+X[(i0+3000)%N][0])
