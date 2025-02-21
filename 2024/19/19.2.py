from functools import cache

input = open('input.txt').read().strip().split('\n')
patterns = sorted(input[0].split(', '))

@cache
def feasible(design):
    if len(design) == 0: return 1
    return sum([feasible(design[len(p):]) for p in patterns if design[0:len(p)] == p])

print(sum([feasible(design) for design in input[2:]]))
