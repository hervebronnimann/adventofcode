from itertools import permutations

input = open("input.txt",'r').read().strip().split('\n')
target = 'fbgdceah'

def scramble(pwd):
    pwd = list(pwd)
    for row in input:
        # print(''.join(pwd), "  === ",row)
        x = row.split()
        if row.startswith('move'):
            src,dst=int(x[2]),int(x[5])
            x = pwd.pop(src)
            pwd.insert(dst,x)
        elif row.startswith('reverse'):
            src,dst=int(x[2]),int(x[4])
            suffix = pwd[dst+1:] if dst<len(pwd) else []
            pwd = pwd[0:src] + pwd[src:dst+1][::-1] + suffix
        elif row.startswith('swap letter'):
            src,dst=pwd.index(x[2]),pwd.index(x[5])
            u,v = pwd[src],pwd[dst]
            pwd[src]=v
            pwd[dst]=u
        elif row.startswith('swap position'):
            src,dst=int(x[2]),int(x[5])
            u,v = pwd[src],pwd[dst]
            pwd[src]=v
            pwd[dst]=u
        elif row.startswith('rotate based'):
            idx=pwd.index(x[6])
            n = (idx+1+(1 if idx>=4 else 0)) % len(pwd)
            pwd = pwd[-n:] + pwd[0:-n] if n>0 else pwd
        elif row.startswith('rotate left'):
            n=int(x[2])
            pwd = pwd[n:] + pwd[0:n]
        elif row.startswith('rotate right'):
            n=int(x[2])
            pwd = pwd[-n:] + pwd[0:-n] if n>0 else pwd
    return pwd

for pwd in permutations(list(target)):
    # print(pwd)
    if ''.join(scramble(pwd)) == target:
        print(''.join(pwd))
