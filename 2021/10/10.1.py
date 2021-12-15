match={ '(': ')', '[': ']', '{': '}', '<': '>' }
rmatch={ ')': '(', ']': '[', '}': '{', '>': '<' }
points={ ')': 3, ']': 57, '}': 1197, '>': 25137, '':0 }

def parse(line):
  """ Returns first offending character, or '' if parse is a success. """
  stack=[]; pos=0
  for x in line:
    if x in match.keys():
      stack.append(x)
    elif x in rmatch.keys():
      if len(stack)==0: return x
      if rmatch[x]!=stack[len(stack)-1]: return x
      stack.pop()
    else: return x # illegal char
  return ''

with open("input.txt") as f:
  print sum([points[parse(line.rstrip('\n'))] for line in f])
