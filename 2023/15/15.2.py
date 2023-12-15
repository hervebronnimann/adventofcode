input = open("input.txt",'r').read().strip().split(',')

def HASH(x: str):
    res = 0;
    for c in x:
        res += ord(c); res *= 17; res %= 256
    return res

# print(sum([HASH(x) for x in input]))

Boxes = []
for i in range(256):
    Boxes.append(list())

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
        # print(label, box, Boxes[box])
        found = False
        for i,(z,m) in enumerate(Boxes[box]):
            if z==label:
                Boxes[box][i] = (label,n)
                found = True
                break
        if not found:
            Boxes[box].append( (label,n) )
    # print(x,[(i,b) for i,b in enumerate(Boxes) if len(b)>0])

res = 0
for b,box in enumerate(Boxes):
  for  i,(_,n) in enumerate(box):
    res += (b+1) * (i+1) * n
print(res)
