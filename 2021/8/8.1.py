output=[]
with open('input.txt') as f:
  for line in f:
    output.append(line.split('|')[1].split())

n=0
for x in output:
  for s in x:
    if len(s) in [2,3,4,7]: n += 1
print(n)
