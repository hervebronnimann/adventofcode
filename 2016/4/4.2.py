from collections import Counter
import re

input = open("input.txt",'r').read().strip().split('\n')

def parse(x:str):
    x = re.sub('[-[\]]+', ' ',x).strip().split()
    # elements in Counter with the same count are ordered by appearance
    # so sort them alphabetically, before passing to counter.
    return (Counter(sorted("".join(x[:-2]))),"-".join(x[:-2]),int(x[-2]),x[-1])

def rot(n,s):
    if s=='-': return ' '
    return chr((ord(s[0])-ord('a') + n)%26 + ord('a'))

def rotate(n,s):
    return ''.join([rot(n,x) for x in s])

def decode(x:str):
    c,s,id,code = parse(x)
    if code == ''.join([k for k,_ in c.most_common(5)]):
        return id, rotate(id,s)
    return 0,""

# print(rotate(343, 'qzmt-zixmtkozy-ivhz'))
res = None
for row in input:
    id,name = decode(row)
    if 'pole' in name: res = (id,name)
    if name: print(id,name)
print("The names are so hilarious, this program displays them all, and finds the answer:")
print(res)
