from functools import reduce

hex = {
  '0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111',
  '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111' 
}

def htob(str): return reduce(lambda x,y: x+hex[y], str, '')
def btod(str): return reduce(lambda x,y: 2*x+int(y), str, 0)
def prod(a): return reduce(lambda x,y: x*y, a, 1)

def decode_packet(str,cur=0):
  ver = str[cur:cur+3]; cur += 3
  typ = str[cur:cur+3]; cur += 3
  # print('version:%s(%d) type:%s(%d) cur:%d' % (ver,btod(ver),typ,btod(typ), cur))
  if typ == '100':
    value = btod(str[cur+1:cur+5])
    while str[cur]=='1':
      cur += 5
      value = value*16 + btod(str[cur+1:cur+5])
    # print('value(%d)' % value)
    return cur+5,value
  len_typeID = 'len' if str[cur]=='0' else 'num'
  xlen = 16 if str[cur]=='0' else 12
  nlen = btod(str[cur+1:cur+xlen])
  # print('subpacket %s:%s(%d) cur:%d' % (len_typeID, str[cur+1:cur+xlen], nlen, cur+xlen))
  cur += xlen
  stack=[]
  if len_typeID == 'len':
    nend = cur + nlen
    while cur < nend:
      cur,res = decode_packet(str,cur)
      stack.append(res)
  else:
    for i in range(nlen):
      cur,res = decode_packet(str,cur)
      stack.append(res)
  if typ == '000': return cur, sum(stack)
  if typ == '001': return cur, prod(stack)
  if typ == '010': return cur, min(stack)
  if typ == '011': return cur, max(stack)
  if typ == '101': return cur, 1 if stack[0]>stack[1] else 0
  if typ == '110': return cur, 1 if stack[0]<stack[1] else 0
  if typ == '111': return cur, 1 if stack[0]==stack[1] else 0
  print('ERROR')
  return -1,-1
  
def solve_string(str,filename=str):
  print("SOLVED:  %d for %s" % (decode_packet(htob(str))[1], filename))

def solve(filename):
  with open(filename) as f:
    solve_string(next(f).strip(),filename)

solve_string('C200B40A82')                  # finds the sum of 1 and 2, resulting in the value 3.
solve_string('04005AC33890')                # finds the product of 6 and 9, resulting in the value 54.
solve_string('880086C3E88112')              # finds the minimum of 7, 8, and 9, resulting in the value 7.
solve_string('CE00C43D881120')              # finds the maximum of 7, 8, and 9, resulting in the value 9.
solve_string('D8005AC2A8F0')                # produces 1, because 5 is less than 15.
solve_string('F600BC2D8F')                  # produces 0, because 5 is not greater than 15.
solve_string('9C005AC2F8F0')                # produces 0, because 5 is not equal to 15.
solve_string('9C0141080250320F1802104A08')  # produces 1, because 1 + 3 = 2 * 2.
solve('input.txt')
