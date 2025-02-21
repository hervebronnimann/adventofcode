
def mix(x,y): return x ^ y
def prune(x): return x % 16777216
def secret(x):
    x = prune(mix(x * 64, x))
    x = prune(mix(x // 32, x))
    x = prune(mix(x * 2048, x))
    return x

def nth(x,n):
    for i in range(n): x = secret(x)
    return x

result = 0
for x in open('input.txt').read().strip().split('\n'):
    result += nth(int(x),2000)
print(result)
