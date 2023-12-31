import re

input = open("input.txt",'r').read().strip().split('\n')

def has_abba(x):
    for i in range(len(x)-2):
        if x[i]==x[i+1]: continue
        y = x[i]+x[i+1]+x[i+1]+x[i]
        if '[' in y or ']' in y: continue
        if y in x: return True
    return False

def supports_tls(x):
    for y in re.findall('\[([^[]*)\]', x):
        if has_abba(y): return False
    return has_abba(x)

# print(supports_tls('abba[mnop]qrst'))
# print(supports_tls('abcd[bddb]xyyx'))
# print(supports_tls('aaaa[qwer]tyui'))
# print(supports_tls('ioxxoj[asdfgh]zxcvbn'))

res = 0
for row in input:
    if supports_tls(row): res += 1
print(res)
