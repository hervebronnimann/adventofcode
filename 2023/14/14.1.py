input = open("input.txt",'r').read().strip().split('\n')

def gravity(x:str):
  y = x.split("#")
  for i,z in enumerate(y):
    y[i] = 'O'*z.count('O') + '.'*z.count('.')
  return '#'.join(y)

def transpose(input):
  return ["".join(list(x)) for x in zip(*input)]

def weight(input):
    return sum([(i+1)*x.count('O') for i,x in enumerate(input[-1::-1])])

input = transpose(input)
for i,x in enumerate(input):
    input[i] = gravity(x)
input = transpose(input)

print(weight(input))
