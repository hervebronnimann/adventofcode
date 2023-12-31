input = open("input.txt",'r').read().strip()

def lendecode2(s:str):
    i,res = 0,0
    while i<len(s):
        if s[i]=='(':
            j = i+1
            while s[j]!=')': j += 1
            x,n = s[i+1:j].split('x')
            x=int(x); n = int(n)
            res += lendecode2(s[j+1:j+1+x]) * n
            i = j+1+x
        else:
            res += 1
            i += 1
    return res

print(lendecode2('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'))

print(lendecode2(input))
