function reverse(x) { y=""; for(j=length(x);j>0;--j) y=y substr(x,j,1); return y; } 
function ccw(n) { return n==4 ? 1 : n+1; }

/^Tile/ { ++ntiles; current = $2; r = 0; }
/^[.#]+$/ {
  row[++r] = $0; LEN = length($0);
  if (r == 1) side[1,current] = $0;
}
/^$/ {
  # Keep tile borders clockwise, 1=top, 2=right, 3=bottom(reverse), 4=left(reverse)
  side[3,current] = reverse(row[r]);
  side[2,current] = ""; side[4,current] = "";
  for (i=1;i<=r;++i) {
    side[2,current] = side[2,current] substr(row[i],LEN,1);
    side[4,current] = side[4,current] substr(row[r-i+1],1,1);
  }
  delete row; r = 0;
  # Insert tile borders into map
  for (i=1; i<=4; ++i) {
    x = side[i,current]; mapid[x,++mapn[x]] = current; maps[x,mapn[x]] = i;
    print "Tile " current " side " i " " x " matching " reverse(x)
  }
}
END {
  print "Tiles " ntiles " borders " sqrt(ntiles)*4
  # Find border tiles, keep count by id, corners will have count==2, others count==1
  for (x in mapn) {
    rx = reverse(x);
    if (mapn[x] == 1 && !(rx in mapn)) {
      print "Found border " x " side " maps[x,1] " id " mapid[x,1];
      ++bordern[mapid[x,1]];
    }
    if (mapn[x] > 2 || rx in mapn && mapn[rx] > 2) {
      # This will be important to know for Part 2.
      print "Multiple matches for " x " " mapn[x];
    }
  }
  res = 1;
  for (id in bordern) {
    if (bordern[id] == 2) {
      print "Found corner " id; res *= id;
    }
  }
  print res;
}
