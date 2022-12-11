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

# PARSE

monkey = 0
items = []
ops = []
div = []
dest_true = []
dest_false = []

def parse(x):
  if x == 'old + old': return lambda x: x + x
  if x == 'old * old': return lambda x: x * x
  if 'old + ' in x: return lambda x,y=int(x.split(' ')[2]): x + y
  if ' + old' in x: return lambda y,x=int(x.split(' ')[0]): x + y
  if 'old * ' in x: return lambda x,y=int(x.split(' ')[2]): x + y
  if ' * old' in x: return lambda y,x=int(x.split(' ')[0]): x + y
  raise(Exception(f"Can't parse {x}"))

for x in lines:
  if 'items:' in x: items.append(list(map(int,x.split(': ')[1].split(', '))))
  elif 'Operation:' in x: ops.append(parse(x.split('new = ')[1]))
  elif 'Test' in x: div.append(int(x.split('by ')[1]))
  elif 'If true:' in x: dest_true.append(int(x.split('monkey ')[1]))
  elif 'If false:' in x: dest_false.append(int(x.split('monkey ')[1]))

print(items)
print(div)
print(dest_true)
print(dest_false)

# PLAY 20 ROUNDS

N = len(items)
inspections = [0 for i in range(len(items))]
verbose = True

for round in range(20):

  for monkey in range(N):
    for item in items[monkey]:
      item = ops[monkey](item) // 3
      if item % div[monkey] == 0:
        items[dest_true[monkey]].append(item)
      else:
        items[dest_false[monkey]].append(item)
    inspections[monkey] += len(items[monkey])
    items[monkey] = []

  if verbose:
    print(f'After round {round+1}')
    for monkey in range(len(items)):
      print(f'  Monkey {monkey}: {", ".join(map(str,items[monkey]))}')

inspections = sorted(inspections,reverse=True)
print(inspections[0]*inspections[1])
