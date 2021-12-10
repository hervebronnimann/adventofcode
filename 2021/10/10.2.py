match={ '(': ')', '[': ']', '{': '}', '<': '>' }
rmatch={ ')': '(', ']': '[', '}': '{', '>': '<' }
points={ ')': 1, ']': 2, '}': 3, '>': 4 }

def parse(line,complete=False):
  """ Returns stack of unmatched opening chars, or '' if parse is not a success. """
  stack=[]
  for x in line:
    if x in match.keys():
      stack.append(x)
    elif x in rmatch.keys():
      if len(stack)==0: return []
      if rmatch[x]!=stack[len(stack)-1]: return []
      stack.pop()
    else: return []
  return stack

def score(s):
  res=0
  while len(s)>0: res = res*5+points[match[s[-1]]]; s.pop()
  return res

with open("input.txt") as f:
  result=[]
  for line in f:
    s=parse(line.rstrip('\n'))
    if len(s)>0:
      result.append(score(s))
  result.sort()
  print(result[len(result)//2])
