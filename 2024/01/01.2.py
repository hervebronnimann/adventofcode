l1 = []
l2 = []
with open("input.txt",'r') as f:
  for s in f:
    l1.append(int(s.split()[0]))
    l2.append(int(s.split()[1]))

print(sum([x*l2.count(x) for x in l1]))
