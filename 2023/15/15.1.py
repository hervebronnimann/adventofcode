input = open("input.txt",'r').read().strip().split(',')

def HASH(x: str):
    '''Determine the ASCII code for the current character of the string.
Increase the current value by the ASCII code you just determined.
Set the current value to itself multiplied by 17.
Set the current value to the remainder of dividing itself by 256.'''
    res = 0;
    for c in x:
        res += ord(c); res *= 17; res %= 256
    return res

for x in [ 'ab', 'qp', 'cm', 'ot', 'pc' ]:
  print(x,HASH(x))

print(sum([HASH(x) for x in input]))
