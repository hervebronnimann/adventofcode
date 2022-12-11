from math import prod

lines = """
Monkey 0:
  Starting items: 53, 89, 62, 57, 74, 51, 83, 97
  Operation: new = old * 3
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 5

Monkey 1:
  Starting items: 85, 94, 97, 92, 56
  Operation: new = old + 2
  Test: divisible by 19
    If true: throw to monkey 5
    If false: throw to monkey 2

Monkey 2:
  Starting items: 86, 82, 82
  Operation: new = old + 1
  Test: divisible by 11
    If true: throw to monkey 3
    If false: throw to monkey 4

Monkey 3:
  Starting items: 94, 68
  Operation: new = old + 5
  Test: divisible by 17
    If true: throw to monkey 7
    If false: throw to monkey 6

Monkey 4:
  Starting items: 83, 62, 74, 58, 96, 68, 85
  Operation: new = old + 4
  Test: divisible by 3
    If true: throw to monkey 3
    If false: throw to monkey 6

Monkey 5:
  Starting items: 50, 68, 95, 82
  Operation: new = old + 8
  Test: divisible by 7
    If true: throw to monkey 2
    If false: throw to monkey 4

Monkey 6:
  Starting items: 75
  Operation: new = old * 7
  Test: divisible by 5
    If true: throw to monkey 7
    If false: throw to monkey 0

Monkey 7:
  Starting items: 92, 52, 85, 89, 68, 82
  Operation: new = old * old
  Test: divisible by 2
    If true: throw to monkey 0
    If false: throw to monkey 1
""".strip().split('\n');

# PARSE THE INPUT [GOSH]

op={
'new = old * 19': lambda x:x*19,
'new = old + 6': lambda x:x+6,
'new = old + 3': lambda x:x+3,
'new = old * 3': lambda x:x*3,
'new = old + 2': lambda x:x+2,
'new = old + 1': lambda x:x+1,
'new = old + 5': lambda x:x+5,
'new = old + 4': lambda x:x+4,
'new = old + 8': lambda x:x+8,
'new = old * 7': lambda x:x*7,
'new = old * old': lambda x:x*x,
}

monkey = 0
items = []
ops = []
div = []
dest_true = []
dest_false = []

for l in lines:
  l = l.strip()
  if 'Monkey' in l: monkey = int(l.split(' ')[1][:-1])
  elif 'items' in l:
    items.append(list(map(int,l.split(': ')[1].split(', ')))); print(items[-1])
  elif 'Operation' in l: ops.append(op[l.split(': ')[1]])
  elif 'Test' in l: div.append(int(l.split(' ')[3]))
  elif 'true:' in l: dest_true.append(int(l.split(' ')[5]))
  elif 'false:' in l: dest_false.append(int(l.split(' ')[5]))
  else:
    monkey += 1
    if len(l)>0: print(f'parse error {l}')

print(items)
print(div)
print(dest_true)
print(dest_false)

inspections = [0 for i in range(len(items))]
M = prod(div)

for round in range(10000):

  for monkey in range(len(items)):
    for item in items[monkey]:
      inspections[monkey] += 1
      # item = ops[monkey](item) // 3
      item = ops[monkey](item) % M
      if item % div[monkey] == 0:
        items[dest_true[monkey]].append(item)
      else:
        items[dest_false[monkey]].append(item)
    items[monkey] = []

  # print(f'After round {round+1}')
  # for monkey in range(len(items)):
  # print(f'  Monkey {monkey}: {", ".join(map(str,items[monkey]))}')

inspections = sorted(inspections,reverse=True)
print(inspections[0]*inspections[1])
