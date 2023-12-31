import hashlib

# input = 'abc'
input = 'ugkcyxxp'

pwd,x = [' ']*8,0
while ' ' in pwd:
    h = hashlib.md5((input+str(x)).encode('utf-8')).hexdigest()
    if h.startswith('00000') and h[5] in '01234567':
        if pwd[int(h[5])] == ' ': pwd[int(h[5])] = h[6]
        print(''.join(pwd))
    x += 1
print(''.join(pwd))
