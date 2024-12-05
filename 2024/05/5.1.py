text = open("input.txt",'r').read().strip().split('\n')
rules = [ tuple(t.split('|'))  for t in text if '|' in t ]
pages = [ t.split(',')  for t in text if ',' in t ]

def good(p):
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            if (p[j],p[i]) in rules: return 0
    return int(p[len(p)//2])

print(sum([good(p) for p in pages]))

