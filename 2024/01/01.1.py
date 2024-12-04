l1 = []
l2 = []
with open("input.txt",'r') as f:
  for s in f:
    l1.append(int(s.split()[0]))
    l2.append(int(s.split()[1]))

l1.sort()
l2.sort()
print(sum([abs(x-y) for x,y in zip(l1,l2)]))
