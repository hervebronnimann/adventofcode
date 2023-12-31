input = open("input.txt",'r').read().strip()

def decode(s:str):
    i,res = 0,''
    while i<len(s):
        if s[i]=='(':
            j = i+1
            while s[j]!=')': j += 1
            x,n = s[i+1:j].split('x')
            x=int(x); n = int(n)
            res += s[j+1:j+1+x] * n
            i = j+1+x
        else:
            res += s[i]
            i += 1
    return res

print(decode('A(1x5)BC'))
print(decode('(3x3)XYZ'))
print(decode('A(2x2)BCD(2x2)EFG'))
print(decode('(6x1)(1x3)A'))
print(decode('X(8x2)(3x3)ABCY'))
print(decode(input))
print(len(decode(input)))
