max = 0
sum = 0
with open("input.txt",'r') as f:
  for line in f:
    line = line.strip()
    if line == '':
      max = sum if sum > max else max
      sum = 0
    else:
      sum += int(line)
print(max)
