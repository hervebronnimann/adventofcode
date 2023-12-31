input = open("input.txt",'r').read().strip().split('\n')
input = [ row.strip().split() for row in input ]
input = [ (int(u),int(v),int(w)) for u,v,w in input ]
# print(input)

res = 0
for u,v,w in input:
    res += 1 if u+v>w and u+w>v and v+w>u else 0
print(res)
