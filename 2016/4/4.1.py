from collections import Counter
import re

input = open("input.txt",'r').read().strip().split('\n')

def parse(x:str):
    x = re.sub('[-[\]]+', ' ',x).strip().split()
    # elements in Counter with the same count are ordered by appearance
    # so sort them alphabetically, before passing to counter.
    return (Counter(sorted("".join(x[:-2]))),int(x[-2]),x[-1])

def decode(x:str):
    c,id,code = parse(x)
    if code == ''.join([k for k,_ in c.most_common(5)]): return id
    return 0

res = 0
for row in input:
    res += decode(row)
print(res)
