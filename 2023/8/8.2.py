input = open("input.txt",'r').read().strip().split('\n')
# input = [ x.split(" ") for x in open("input.txt",'r').read().strip().split('\n') ]

left = {}
right = {}
start = set()
end = set()
for x in input[2:]:
  x,l,r = x.split()
  left[x] = l
  right[x] = r
  if x[2]=='A': start.add(x)
  if x[2]=='Z': end.add(x)

ins = input[0]

pos = list(start)
reached = False
steps = 0
while not reached:
  for p in ins:
    newpos = []
    Reached = True
    steps += 1
    for x in pos:
      y = left[x] if p == "L" else right[x]
      if y not in end: reached = False
      newpos.append(y)
    pos = newpos

print(steps)
