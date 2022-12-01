max = []
sum = 0
with open("input.txt",'r') as f:
  for line in f:
    line = line.strip()
    if line == '':
      max.append(sum)
      sum = 0
    else:
      sum += int(line)
max = sorted(max,reverse=True)
print(max[0]+max[1]+max[2])
