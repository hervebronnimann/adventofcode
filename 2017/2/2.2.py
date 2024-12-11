import itertools

n = [ [ int(x) for x in l.split()] for l in open("input.txt").read().strip().split('\n') ]

# print([list(itertools.permutations(sorted(l),2)) for l in n])
print(sum([[ x//y for x,y in itertools.permutations(sorted(l),2) if (x//y)*y==x][0] for l in n]))
