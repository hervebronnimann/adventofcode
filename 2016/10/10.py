from collections import defaultdict
from collections import deque

input = open("input.txt",'r').read().strip().split('\n')

bot = defaultdict(lambda: [])
low = defaultdict(lambda: [])
high = defaultdict(lambda: [])
output = defaultdict(lambda: [])

for row in input:
    x = row.split()
    if row.startswith('value'):
        bot[x[5]].append(int(x[1]))
    else:
        low[x[1]] = (x[6],x[5]=='bot')
        high[x[1]] = (x[11], x[10]=='bot')

for b in bot:
    if len(bot[b])>=2: print(f"Start with bot {b}"); break

q = deque([b])
while q:
    b = q.popleft()
    lh = sorted(bot[b])
    lb,lo = low[b]
    hb,ho = high[b]
    if lh[0]==17 and lh[1]==61: print("Part 1:", b)
    if lo:
        bot[lb].append(lh[0])
        if len(bot[lb])>=2: q.append(lb)
    else:
        output[lb].append(lh[0])
    if ho:
        bot[hb].append(lh[1])
        if len(bot[hb])>=2: q.append(hb)
    else:
        output[hb].append(lh[1])
# print(bot)
print("Part 2:",output['0'][0]*output['1'][0]*output['2'][0])
