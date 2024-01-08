input = open("input.txt",'r').read().strip().split('\n')

def parse(row:str):
    node,s,u,v,_ = row.split()
    _,x,y = node.split('-')
    x,y = int(x[1:]),int(y[1:])
    return x,y,int(s[:-1]),int(u[:-1]),int(v[:-1])

input = [ parse(row) for row in input if row.startswith('/dev')]

L = []
for i,n1 in enumerate(input):
    for j,n2 in enumerate(input):
        if i==j: continue
        if n1[3]>0 and n1[3]<=n2[4]:
            L.append((n1,n2))
print(len(L),[(n1,n2) for (n1,n2) in L if n2[3]!=0])
