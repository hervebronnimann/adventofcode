from itertools import accumulate

lines = """
addx 1
noop
addx 2
noop
addx 3
addx 3
addx 1
addx 5
addx 1
noop
noop
addx 4
noop
noop
addx -9
addx 16
addx -1
noop
addx 5
addx -2
addx 4
addx -35
addx 2
addx 28
noop
addx -23
addx 3
addx -2
addx 2
addx 5
addx -8
addx 19
addx -8
addx 2
addx 5
addx 5
addx -14
addx 12
addx 2
addx 5
addx 2
addx -13
addx -23
noop
addx 1
addx 5
addx -1
addx 2
addx 4
addx -9
addx 10
noop
addx 6
addx -11
addx 12
addx 5
addx -25
addx 30
addx -2
addx 2
addx -5
addx 12
addx -37
noop
noop
noop
addx 24
addx -17
noop
addx 33
addx -32
addx 3
addx 1
noop
addx 6
addx -13
addx 17
noop
noop
noop
addx 12
addx -4
addx -2
addx 2
addx 3
addx 4
addx -35
addx -2
noop
addx 20
addx -13
addx -2
addx 5
addx 2
addx 23
addx -18
addx -2
addx 17
addx -10
addx 17
noop
addx -12
addx 3
addx -2
addx 2
noop
addx 3
addx 2
noop
addx -13
addx -20
noop
addx 1
addx 2
addx 5
addx 2
addx 5
noop
noop
noop
noop
noop
addx 1
addx 2
addx -18
noop
addx 26
addx -1
addx 6
noop
noop
noop
addx 4
addx 1
noop
noop
noop
noop
""".strip().split('\n');

Vs = [1] + [ 0 if c=='noop' else int(c.split(' ')[1]) for c in lines]
Vs = list(accumulate(Vs))
Xs = [1] + sum([[v] if c=='noop' else [v,v] for c,v in zip(lines,Vs)], [])
CRT=[[ '##' if abs(j-Xs[i*40+j+1])<=1 else '  ' for j in range(40)] for i in range(6)]
print('\n'.join([''.join(l) for l in CRT]))

# EHPZPJGL
