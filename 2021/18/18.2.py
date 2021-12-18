class Node:

  def __init__(self,val=0,left=None,right=None,up=None):
    self.val=val; self.left=left; self.right=right; self.up=up

  def clone(self):
    if self.is_leaf(): return Node(self.val)
    l=self.left.clone(); r=self.right.clone()
    n=Node(self.val,l,r); l.up=n; r.up=n
    return n

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
    return True
 
  def split(self):
    """ If a terminal node is greater than 10, replace by two nodes"""
    if not self.is_leaf() or self.val < 10: return False
    v=self.val; p=self.val//2; q=self.val-p
    self.val=0; self.left=Node(p,up=self); self.right=Node(q,up=self)
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


def reduce(node):
  """ Find a node to explode, or to split, but not both in the same traversal. """
  while True:
    if reduce_helper(node,0,False): continue
    if reduce_helper(node,0,True): continue
    break;
  return node

def add(n1,n2):
  n=Node(val=0,left=n1,right=n2,up=None); n1.up=n; n2.up=n
  return n

def parse(str):
  if str[0]!='[':
    comma=str.find(','); bracket=str.find(']')
    end=min(comma,bracket) if comma>=0 and bracket>=0 else comma if comma>=0 else bracket
    return Node(val=int(str[:end])), str[end+1:]
  p,str = parse(str[1:])
  q,str = parse(str)
  return add(p,q), str[1:]


def solve(filename):
  print("SOLVING ", filename)
  input = []
  with open(filename) as f:
    input = [parse(l.strip())[0] for l in f]
  max_mag = 0
  for i in range(len(input)):
    for j in range(len(input)):
      n = reduce(add(input[i].clone(),input[j].clone()))
      # print('Add %d and %d (%s %s) gives magnitude %d' % (i, j, input[i].to_string(), input[j].to_string(), n.magnitude()))
      max_mag=max(max_mag,n.magnitude())
  print(max_mag)

solve("example1.txt")
solve("example2.txt")
solve("example3.txt")
solve("example4.txt")
solve("example5.txt")

solve("input.txt")
