function bin(nz,x) {
  ret = 0; m = 1; split(x, chars, "");
  for (n = length(x); n > 0; m*= 2) {
    if (chars[n--] == nz) ret += m;
  }
  return ret;
}
BEGIN { minId = 128*8+8; maxId = 0; totId = 0; }
{ row = bin("B",substr($0,1,7)); col = bin("R",substr($0,8,3));
  id = row*8+col; print row, col, id;
  if (id > maxId) maxId = id; if (id < minId) minId = id;
     ## FOR PART 2
  if (row > 11 && row < 111) totId += id;
}
END { print "MinId: ", minId, " MaxId: ", maxId;  ## 89 (row 11, col 1) and 888 (row 111 col 0)
        ## FOR PART 2: round to 0 and 7 resp. mod 8
      print "TotalId: ", totId;
      minId += 7; maxId -= 1;
      print "YourId: ", (maxId-minId+1)*(maxId+minId)/2 - totId;
}
