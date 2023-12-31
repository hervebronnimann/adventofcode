import hashlib

# input = 'abc'
input = 'ugkcyxxp'

pwd,x = '',0
while len(pwd)<8:
    h = hashlib.md5((input+str(x)).encode('utf-8')).hexdigest()
    if h.startswith('00000'): pwd += h[5]
    x += 1
print(pwd)
