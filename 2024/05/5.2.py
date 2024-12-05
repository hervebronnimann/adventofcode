text = open("input.txt",'r').read().strip().split('\n')
rules = set([ tuple(t.split('|'))  for t in text if '|' in t ])
pages = [ t.split(',')  for t in text if ',' in t ]

def good(p):
    swapped = False
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            if (p[j],p[i]) in rules:
                p[i],p[j] = p[j],p[i]
                swapped = True
    return int(p[len(p)//2]) if swapped else 0

print(sum([good(p) for p in pages]))

