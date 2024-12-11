n = [ [ int(x) for x in l.split()] for l in open("input.txt").read().strip().split('\n') ]

print(sum([ max(l) - min(l) for l in n ]))
