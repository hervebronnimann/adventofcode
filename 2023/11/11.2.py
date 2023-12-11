input = open("example.txt",'r').read().strip().split('\n')
input = open("input.txt",'r').read().strip().split('\n')
m = len(input); n = len(input[0])

def compute_index(input):
  i_index= []; shft = 0
  for i, x in enumerate(input):
    i_index.append(i+shft)
    if x == '.'*len(x): shft += 999999
  return i_index

def transpose(input):
  return ["".join(list(x)) for x in zip(*input)]

idx = compute_index(input)
input = transpose(input)
jdx = compute_index(input)
input = transpose(input)

g = []
for i,x in enumerate(input):
  for j,y in enumerate(x):
    if y == '#': g.append((idx[i],jdx[j]))

res = 0
for i in range(len(g)):
  for j in range(i+1,len(g)):
    res += abs(g[i][0]-g[j][0]) + abs(g[i][1]-g[j][1])
print(res)
