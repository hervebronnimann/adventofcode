m = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def digitize_forward(s : str):
  if len(s) == 0: return s
  for x in m:
    if s.startswith(x):
      return m[x] + digitize_forward(str(s[len(x):]))
  return s[0]+digitize_forward(s[1:])

def digitize_backward(s : str):
  if len(s) == 0: return s
  for x in m:
    if s.endswith(x):
      return digitize_backward(str(s[:len(s)-len(x)-1])) + m[x]
  return digitize_backward(s[:len(s)-1])+s[-1]

def calib(s : str):
  df = "".join(filter(lambda x : x.isdigit(), digitize_forward(s)))
  db = "".join(filter(lambda x : x.isdigit(), digitize_backward(s)))
  print(s,df[0]+db[-1])
  return 10*int(df[0]) + int(db[-1])

v = 0
with open("input.txt",'r') as f:
  for s in f:
    s = s.strip()
    v += calib(s)
print(v)
