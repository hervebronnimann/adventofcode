function bubblesort(a) {
  do {
    _haschanged = 0
    for(_i=1; _i < length(a); ++_i)
      if (a[_i] > a[_i+1]) {
        _t = a[_i]; a[_i] = a[_i+1]; a[_i+1] = _t; _haschanged = 1
      }
  } while ( _haschanged == 1 )
}
function find(x,a) { for (_x in a) if (x==a[_x]) return 1;  return 0 }
function string_join(a) { _str=""; for(_j=1;_j<=length(a);++_j) _str=_str a[_j]; return _str }
function string_sort(x) { split(x,_a,""); bubblesort(_a); return string_join(_a) }
function overlap(x,y) { split(x,_a,""); split(y,_b,""); _n=0; for (_z in _a) _n+=find(_a[_z],_b); return _n }
function rmap(m,x) { for (_t in m) if (m[_t]==x) return _t; return "" }
BEGIN {
  solve1[2]=1; solve1[3]=7; solve1[4]=4; solve1[7]=8 
  print string_sort("abvfghs");
  print string_sort("zxyvtnmlabcd");
  }
{ 
  delete map;
  # Find 1, 4, 7, 8
  for (i=1;i<=10;++i) {
    if (length($i) in solve1) map[string_sort($i)]=solve1[length($i)]
  }
  x1=rmap(map,1); x4=rmap(map,4)
  # Find 2, 3, 5, and 0, 6, 9
  for (i=1;i<=10;++i) {
    if (string_sort($i) in map) continue;
    if (length($i)==5) {
      if (overlap($i,x1)==2)      map[string_sort($i)]=3 
      else if (overlap($i,x4)==2) map[string_sort($i)]=2
      else if (overlap($i,x4)==3) map[string_sort($i)]=5
      else print "Couldn't find symbol " $i " (length 5)"
    } else if (length($i)==6) {
      if (overlap($i,x1)==1)      map[string_sort($i)]=6
      else if (overlap($i,x4)==4) map[string_sort($i)]=9
      else if (overlap($i,x4)==3) map[string_sort($i)]=0
      else print "Couldn't find symbol " $i " (length 6)"
    } else {
      print "Couldn't find symbol " $i " (length " length($i) ")"
    }
  }
  # the result
  n=0
  for (i=12;i<=15;++i) {
    n = n*10 + map[string_sort($i)];
  }
  print n
  result += n;
}
END { print result }
