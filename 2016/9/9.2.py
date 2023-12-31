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

def decode2(s:str):
    while '(' in s:
        s = decode(s)
    return s

print(decode2('A(1x5)BC'))
print(decode2('(3x3)XYZ'))
print(decode2('A(2x2)BCD(2x2)EFG'))
print(decode2('(6x1)(1x3)A'))
print(decode2('X(8x2)(3x3)ABCY'))
print(len(decode2('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN')))

print(len(decode2(input)))
