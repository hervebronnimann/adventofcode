input = [
'swap position 4 with position 0',
'swap letter d with letter b',
'reverse positions 0 through 4',
'rotate left 1',
'move position 1 to position 4',
'move position 3 to position 0',
'rotate based on position of letter b',
'rotate based on position of letter d',
]
input = open("input.txt",'r').read().strip().split('\n')

pwd=list('abcde')
pwd=list('abcdefgh')

for row in input:
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
        suffix = pwd[-n:] if n>0 else []
        pwd = suffix + pwd[0:-n]
    elif row.startswith('rotate left'):
        n=int(x[2])
        pwd = pwd[n:] + pwd[0:n]
    elif row.startswith('rotate right'):
        n=int(x[2])
        suffix = pwd[-n:] if n>0 else []
        pwd = suffix + pwd[0:-n]

print(''.join(pwd))
