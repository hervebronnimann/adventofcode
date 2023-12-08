input = open("input.txt",'r').read().strip().split('\n')
# input = [ x.split(" ") for x in open("input.txt",'r').read().strip().split('\n') ]

left = {}
right = {}
for x in input[2:]:
  x,l,r = x.split()
  left[x] = l
  right[x] = r

ins = input[0]

pos = "AAA"; steps = 0
while pos != "ZZZ":
  for p in ins:
    pos = left[pos] if p == "L" else right[pos]
    steps += 1
    if pos == "ZZZ": break

print(steps)
