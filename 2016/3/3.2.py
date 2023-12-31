input = open("input.txt",'r').read().strip().split('\n')
input = [ row.strip().split() for row in input ]
input = [ (int(u),int(v),int(w)) for u,v,w in input ]

def transpose(r1,r2,r3):
    u1,v1,w1 = r1
    u2,v2,w2 = r2
    u3,v3,w3 = r3
    return [(u1,u2,u3),(v1,v2,v3),(w1,w2,w3)]

input = sum([transpose(input[n],input[n+1],input[n+2]) for n in range(0,len(input),3)], [])
# print(input)

res = 0
for u,v,w in input:
    res += 1 if u+v>w and u+w>v and v+w>u else 0
print(res)
