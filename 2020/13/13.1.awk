BEGIN { n = 0; }
{ 
  if (n != 0) {
    ans = 0; ansk = 0;
    split($1,id,",");
    for (i in id) {
      if (id[i] == "x") continue;
      k = id[i]*(1 + int((n-1)/id[i])) - n;
      print "Bus id " id[i] " departing in " k;
      if (ans == 0 || k < ansk) { ans = id[i]; ansk = k; }
    }
  }
  if (n == 0) { n = $1; print "Departing at " n; }
}
END { print ansk * ans; }
