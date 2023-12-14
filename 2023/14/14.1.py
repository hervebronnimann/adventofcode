input = open("example.txt",'r').read().strip().split('\n')
input = open("input.txt",'r').read().strip().split('\n')
m = len(input); n = len(input[0])

def gravity(x:str):
  y = x.split("#")
  for i,z in enumerate(y):
    y[i] = 'O'*z.count('O') + '.'*z.count('.')
  return '#'.join(y)

def transpose(input):
  return ["".join(list(x)) for x in zip(*input)]

input = transpose(input)
for i,x in enumerate(input):
    input[i] = gravity(x)
input = transpose(input)
print(input)

res = 0
for i,x in enumerate(input[-1::-1]):
    res += (i+1)*x.count('O')
print(res)
