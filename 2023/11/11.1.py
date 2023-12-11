input = open("example.txt",'r').read().strip().split('\n')
input = open("input.txt",'r').read().strip().split('\n')
m = len(input); n = len(input[0])

def dup_row(input):
  input2 = []
  for i, x in enumerate(input):
    input2.append(x)
    if x == '.'*len(x): input2.append(x)
  return input2

def transpose(input):
  return ["".join(list(x)) for x in zip(*input)]

input = dup_row(input)
input = transpose(input)
input = dup_row(input)
input = transpose(input)
print('\n'.join(input), "\n")

g = []
for i,x in enumerate(input):
  for j,y in enumerate(x):
    if y == '#': g.append((i,j))

res = 0
for i in range(len(g)):
  for j in range(i+1,len(g)):
    res += abs(g[i][0]-g[j][0]) + abs(g[i][1]-g[j][1])
print(res)
