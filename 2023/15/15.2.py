input = open("input.txt",'r').read().strip().split(',')

def HASH(x: str):
    res = 0;
    for c in x: res += ord(c); res *= 17; res %= 256
    return res

Boxes = [ list() for _ in range(256) ]

for x in input:
    if x[-1] == '-':
        label = x[:len(x)-1]
        box = HASH(label)
        for z,i in Boxes[box]:
            if z==label: 
               Boxes[box].remove( (z,i) )
    else:
        label,n = x.split('=')
        box = HASH(label); n = int(n)
        found = False
        for i,(z,_) in enumerate(Boxes[box]):
            if z==label:
                Boxes[box][i] = (label,n)
                found = True; break
        if not found:
            Boxes[box].append( (label,n) )

print(sum([sum([(b+1) * (i+1) * n for i,(_,n) in enumerate(box)]) for b,box in enumerate(Boxes)]))
