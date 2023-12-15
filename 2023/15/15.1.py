input = open("input.txt",'r').read().strip().split(',')

def HASH(x: str):
    res = 0;
    for c in x: res += ord(c); res *= 17; res %= 256
    return res

print(sum([HASH(x) for x in input]))
