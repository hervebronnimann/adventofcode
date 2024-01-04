from collections import deque
import hashlib
import re

input = 'cuanljph'

hexdigit = "0123456789abcdef"
str5 = { c:"".join([c]*5) for c in hexdigit }

def md5salt(x):
    return hashlib.md5((input+str(x)).encode('utf-8')).hexdigest()

def h3(h):
    # Worse (scans h 16 times):  for c in hexdigit: if str3[c] in h: return c
    x = re.search(r'(.)\1\1', h)
    if not x: return None
    return x.group(0)[0]

def h5(h,c):
    return 1 if str5[c] in h else 0

q = deque([md5salt(x) for x in range(1001)])
qh5 = deque([[h5(h,c) for c in hexdigit] for h in q])
nh5 = { c: sum([x[i] for x in qh5]) for i,c in enumerate(hexdigit) }

pwd,x = [],0
while len(pwd)<64:
    h = q.popleft(); h5x = qh5.popleft()
    for i,c in enumerate(hexdigit): nh5[c] -= h5x[i]
    h3x = h3(h)
    print("Progress:",x,h,h3x,nh5)
    if h3x and nh5[h3x] > 0:
        print(x,h,nh5[h3x])
        pwd.append((x,h,nh5[h3x]))
        if len(pwd)==64: break
    x += 1;
    h = md5salt(x+1000); h5x = [h5(h,c) for c in hexdigit]
    q.append(h); qh5.append(h5x);
    for i,c in enumerate(hexdigit): nh5[c] += h5x[i]

print(x)
