def calib(s : str):
  d = "".join(filter(lambda x : x.isdigit(), s))
  print(s,d[0]+d[-1])
  return 10*int(d[0]) + int(d[-1])

v = 0
with open("input.txt",'r') as f:
  for s in f:
    s = s.strip()
    v += calib(s)
print(v)
