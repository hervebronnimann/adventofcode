m = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def first(s : str):
  if len(s) == 0: return s
  if s[0].isdigit(): return s[0]
  for x in m:
    if s.startswith(x): return m[x]
  return first(s[1:])

def last(s : str):
  if len(s) == 0: return s
  if s[-1].isdigit(): return s[-1]
  for x in m: 
    if s.endswith(x): return m[x]
  return last(s[:len(s)-1])

def calib(s : str):
  return 10*int(first(s)) + int(last(s))

v = 0
with open("input.txt",'r') as f:
  for s in f:
    s = s.strip()
    v += calib(s)
print(v)
