from functools import cache
input = open('input.txt').read().strip().split('\n')
patterns = sorted(input[0].split(', '))
print(patterns)

@cache
def feasible(design):
    if len(design) == 0: return 1
    for p in patterns:
        if design[0:len(p)] == p and feasible(design[len(p):]) == 1: return 1
    return 0


print(sum([feasible(design) for design in input[2:]]))
