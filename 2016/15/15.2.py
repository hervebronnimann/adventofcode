from functools import reduce

def egcd(a, b):
    if a == 0 : return b,0,1
    g,x1,y1 = egcd(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return g,x,y

def crm(m, a):
    s = 0
    p = reduce(lambda p, b: p*b, m)
    for m_i, a_i in zip(m, a):
        p_i = p // m_i
        s += a_i * egcd(p_i, m_i)[1] * p_i
    return s % p

# Input:
n,p = [13,17,19,7,5,3,11],[10,15,17,1,0,1,0]

a = [ (3*ni-pi-i-1)%ni for i,(ni,pi) in enumerate(zip(n,p)) ]
print(a)
x = crm(n,a)
print([(pi+i)%ni for i,(ni,pi) in enumerate(zip(n,p))])
print([(pi+x+i+1)%ni for i,(ni,pi) in enumerate(zip(n,p))])
print(x)
