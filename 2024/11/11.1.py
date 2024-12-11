import math

input=[ 6, 11, 33023, 4134, 564, 0, 8922422, 688775 ]

def evolve(x):
    if x == 0:
        return [1]
    elif int(math.log10(x)) % 2 == 1:
        p10 = math.pow(10,int(math.log10(x))//2 + 1)
        return [x // p10, x % p10 ]
    else:
        return [x * 2024]

for i in range(25):
    r = []
    for x in input:
        r = r + evolve(x)
    input = r
    #print(input)
print(len(input))
