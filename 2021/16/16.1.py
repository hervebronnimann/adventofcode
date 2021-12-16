from functools import reduce

hex = {
  '0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111',
  '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
}

def htob(str): return reduce(lambda x,y: x+hex[y], str, '')
def btod(str): return reduce(lambda x,y: 2*x+int(y), str, 0)

def decode_packet(str,cur):
  ver = str[cur:cur+3]; cur += 3
  typ = str[cur:cur+3]; cur += 3
  # print('version:%s(%d) type:%s(%d) cur:%d' % (ver,btod(ver),typ,btod(typ), cur))
  res = btod(ver)
  if typ=='100':
    while str[cur]=='1': cur += 5
    cur += 5
    # print('value cur:%d' % cur)
  else:
    len_typeID = 'len' if str[cur]=='0' else 'num'
    xlen = 16 if str[cur]=='0' else 12
    nlen = btod(str[cur+1:cur+xlen])
    # print('subpacket %s:%s(%d) cur:%d' % (len_typeID,str[cur+1:cur+xlen],nlen, cur))
    cur += xlen
    if len_typeID == 'len':
      nend = cur + nlen
      while cur < nend:
        cur,r = decode_packet(str,cur)
        res += r
    else:
      for i in range(nlen):
        cur,r = decode_packet(str,cur)
        res += r
  return cur,res
  
def solve(filename):
  with open(filename) as f:
    print('SOLVED:  %d for %s' % (decode_packet(htob(next(f).strip()),0)[1], filename))

solve('example0.txt')
solve('example1.txt')
solve('example2.txt')
solve('example3.txt')
solve('example4.txt')
solve('example5.txt')
solve('example6.txt')
solve('input.txt')
