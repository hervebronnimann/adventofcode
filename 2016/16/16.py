
def dragon(a):
    invert = {'0':'1','1':'0'}
    b = "".join([invert[x] for x in a[::-1]])
    return a + '0' + b

def checksum(a):
    check = {'00':'1', '11':'1', '01':'0', '10':'0'}
    a = "".join([check[a[i:i+2]] for i in range(0,len(a),2)])
    while len(a)%2==0:
        a = "".join([check[a[i:i+2]] for i in range(0,len(a),2)])
    return a

# n,a = 20,'10000'
n,a = 272,'01110110101001000',
while len(a)<n:
    a = dragon(a)
print("Part 1:", checksum(a[:n]))

n,a = 35651584,'01110110101001000',
while len(a)<n:
    a = dragon(a)
print("Part 2:", checksum(a[:n]))
