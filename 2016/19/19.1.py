# Josephus problem

# N = 5
N = 3004953

x = list(range(1,N+1))
n = 0
while len(x)>1:
    # Remove every other element, compute the index of the starting element in the next round
    n,x = (len(x)+n)%2,x[n::2]
print(x[0])

def josephus(x):
    m = 1
    while 2*m<=x: m *= 2
    return 2*(x-m)+1

print(josephus(N))

