import re

input = open("input.txt",'r').read().strip().split('\n')

def has_bab(x,bab):
    for y in re.findall('\[([^[]*)\]', x):
        if bab in y: return True
    return False

def has_aba(x):
    depth = 0
    for i in range(len(x)-2):
        if x[i]=='[': depth +=1; continue
        if x[i]==']': depth -=1; continue
        if depth>0: continue
        if x[i]==x[i+1]: continue
        if x[i]==x[i+2]:
            if has_bab(x,x[i+1]+x[i]+x[i+1]): return True
    return False

def supports_ssl(x):
    return has_aba(x)

# print(supports_tls('abba[mnop]qrst'))
# print(supports_tls('abcd[bddb]xyyx'))
# print(supports_tls('aaaa[qwer]tyui'))
# print(supports_tls('ioxxoj[asdfgh]zxcvbn'))

res = 0
for row in input:
    if supports_ssl(row): res += 1
print(res)
