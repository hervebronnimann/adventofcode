input = open("input.txt",'r').read().strip().split('\n')

def shift_horiz(x:str, dir:bool):
    y = x.split("#")
    for i,z in enumerate(y):
        if dir:
            y[i] = 'O'*z.count('O') + '.'*z.count('.')
        else:
            y[i] = '.'*z.count('.') + 'O'*z.count('O')
    return '#'.join(y)

def transpose(input:list):
    return ["".join(list(x)) for x in zip(*input)]

def shift(input:list,cycle:int):
    dir = cycle%4 in [0,1]
    if cycle%2==0:
        input = transpose(input)
    for i,x in enumerate(input):
      input[i] = shift_horiz(x,dir)
    if cycle%2==0:
        input = transpose(input)
    return input

def weight(input:list):
    return sum([(i+1)*x.count('O') for i,x in enumerate(input[-1::-1])])

cycle = 0
m = {}
while "\n".join(input) not in m:
    m["\n".join(input)] = cycle
    input = shift(input, cycle)
    cycle += 1

if (cycle - m["\n".join(input)])%4 != 0:
    print("Cycle is not a multiple of 4")
    exit(-1)

period = cycle - m["\n".join(input)]
nperiod = (4000000000-cycle) // period

cycle += nperiod * period
while cycle < 4000000000:
    m["\n".join(input)] = cycle
    input = shift(input, cycle)
    cycle += 1
print(weight(input))
