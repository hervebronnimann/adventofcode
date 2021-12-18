class Node:

  def __init__(self,val=0,left=None,right=None,up=None):
    self.val=val; self.left=left; self.right=right; self.up=up

  def root(self):
    p = self
    while p.up: p = p.up
    return p

  def is_leaf(self): return self.left==None and self.right==None

  def magnitude(self):
    if self.is_leaf(): return self.val
    return 3*self.left.magnitude() + 2*self.right.magnitude()

  def to_string(self):
    if self.is_leaf(): return str(self.val)
    return '[{},{}]'.format(self.left.to_string(), self.right.to_string())

  def prev_node(self):
    p=self; q=p.up;
    while q and p==q.left: p=q; q=p.up
    if not q: return None
    p=q.left
    while p.right: p=p.right
    return p

  def next_node(self):
    p=self; q=p.up;
    while q and p==q.right: p=q; q=p.up
    if not q: return None
    p=q.right
    while p.left: p=p.left
    return p

  def explode(self):
    """ Explode a node replaces it by 0, if its two children are both terminal"""
    if self.is_leaf() or not self.left.is_leaf() or not self.right.is_leaf(): return False
    str=self.to_string()
    p=self.prev_node(); q=self.next_node()
    if p: p.val += self.left.val
    if q: q.val += self.right.val
    self.val=0; self.left=None; self.right=None
    # print('Explode %s results in %s' % (str, self.root().to_string()))
    return True
 
  def split(self):
    """ If a terminal node is greater than 10, replace by two nodes"""
    if not self.is_leaf() or self.val < 10: return False
    v=self.val; p=self.val//2; q=self.val-p
    self.val=0; self.left=Node(p,up=self); self.right=Node(q,up=self)
    # print('Split %d results in      %s' % (v, self.root().to_string()))
    return True

  def reduce(self,depth,split=True):
    if split and self.split(): return True
    if not split and depth>=4 and self.explode(): return True
    return False


def reduce_helper(node,depth,split=True):
  """ Perform a traversal, applying either split or reduce, and returning as soon as one succeeds. """
  if node.reduce(depth,split): return True
  if node.left:
    if reduce_helper(node.left,depth+1,split): return True
  if node.right:
    if reduce_helper(node.right,depth+1,split): return True
  return False


def reduce(tree):
  """ Either split, or explode but not both in the same traversal. """
  while True:
    if reduce_helper(tree,0,False): continue
    if reduce_helper(tree,0,True): continue
    break;
  return tree

def add(n1,n2):
  n=Node(val=0,left=n1,right=n2,up=None); n1.up=n; n2.up=n
  return n

def parse(str):
  # print("Recursively parse: %s" %str)
  if str[0]!='[':
    comma=str.find(','); bracket=str.find(']')
    end=min(comma,bracket) if comma>=0 and bracket>=0 else comma if comma>=0 else bracket
    # print("Parsed %s and remains %s" % (str[:end],str[end+1:]))
    return Node(val=int(str[:end])), str[end+1:]
  p,str = parse(str[1:])   # str now starts with ','
  q,str = parse(str)       # str now starts with ']'
  return add(p,q), str[1:] # skip the final ']'

## THIS ONE DEMANDS DEBUGGING - FROM SIMPLEST TO LARGEST EXAMPLES

n1=parse("[[[[4,3],4],4],[7,[[8,4],9]]]")[0]
n2=parse("[1,1]")[0]
print("Add example: %s + %s -> %s"% (n1.to_string(), n2.to_string(), reduce(add(n1,n2)).to_string()))

mags = {
  "[[1,2],[[3,4],5]] ":  143,
  "[[[[0,7],4],[[7,8],[6,0]]],[8,1]] ":  1384,
  "[[[[1,1],[2,2]],[3,3]],[4,4]] ":  445,
  "[[[[3,0],[5,3]],[4,4]],[5,5]] ":  791,
  "[[[[5,0],[7,4]],[5,5]],[6,6]] ":  1137,
  "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]] ":  3488
}
for s,m in mags.items():
  n = parse(s)[0]
  print("Mag example (should be %d): %s -> %d" % (m, n.to_string(), n.magnitude()))


def solve(filename):
  print("SOLVING ", filename)
  result=None
  with open(filename) as f:
    for l in f:
      n,_ = parse(l.strip())
      print("New snailfish: "+n.to_string())
      result = reduce(add(result,n)) if result else n
      print("Sum so far:    %s (mag:%d)" % (result.to_string(), result.magnitude()))

solve("example1.txt")
solve("example2.txt")
solve("example3.txt")
solve("example4.txt")
solve("example5.txt")

solve("input.txt")
