from collections import defaultdict

def mix(x,y): return x ^ y
def prune(x): return x % 16777216
def secret(x):
    x = prune(mix(x * 64, x))
    x = prune(mix(x // 32, x))
    x = prune(mix(x * 2048, x))
    return x

def payoff(x,n):
    c1,c2,c3,c4 = 0,0,0,0
    result = defaultdict(int)
    for i in range(n):
        z = secret(x)
        c1,c2,c3,c4 = c2,c3,c4,z%10-x%10
        if i >= 3 and (c1,c2,c3,c4) not in result:
            result[(c1,c2,c3,c4)] = z%10
        x = z
    return result

payoffs = defaultdict(int)
for x in open('input.txt').read().strip().split('\n'):
    for s,b in payoff(int(x),2000).items():
        payoffs[s] += b
        # if s == (-2,1,-1,3): print(f"Monkey {x}: buys {b} bananas")

print(max(payoffs.values()))
