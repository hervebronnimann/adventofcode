input = open("input.txt",'r').read().strip().split('\n')

def parse(row:str):
    node,s,u,v,_ = row.split()
    _,x,y = node.split('-')
    x,y = int(x[1:]),int(y[1:])
    return x,y,int(s[:-1]),int(u[:-1]),int(v[:-1])

input = [ parse(row) for row in input if row.startswith('/dev')]

def depict(node):
    if node[2]>500: return '#'
    if node[3]==0: return '_'
    if node[0]==37 and node[1]==0: return 'G'
    if node[0]==0 and node[1]==0: return '*'
    if node[2]<70: return 'X'
    return '.'

xMax = max([node[0] for node in input])
cap = [node[3] for node in input if node[0]==xMax and node[1]==0][0]
x0,y0 = [(node[0],node[1]) for node in input if node[3]==0][0]
minSize = min([node[2] for node in input])
maxUsed = max([node[3] for node in input if node[2]<500])
minLarge = min([node[0] for node in input if node[2]>=500])
yLarge = min([node[1] for node in input if node[2]>=500])
print(f"Capacity to move from access is {cap}")
print(f"Every node other than '#' has size at least {minSize} and used at most {maxUsed}")
print("Grid looks like:")
for y in range(28):
    print(''.join([depict(node) for node in input if node[1]==y]))
print(f"Initially '_' is at {(x0,y0)} and access at (37,0).")
print(f"Row of '#' starts at {(minLarge,yLarge)}.")
print(f"Path is left to col {minLarge-1} ({x0-minLarge+1} steps), then up {y0} steps")
print(f"then right next to G in column {xMax-1} ({xMax-minLarge} steps)")
print(f"then {xMax-1} repeats of 5 steps around G shifting left to _")
print(f"and a final step to bring G to (0,0), for a total of {x0-minLarge+1 + y0 + xMax-minLarge + 5*(xMax-1) + 1} steps")
