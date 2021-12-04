NR==1 { split($0,draws,","); }
NF==0 { ++nboard; row=1 }
NR>1 && NF>0 { for (i=1;i<=NF; ++i) board[nboard,row,i] = $i; ++row }
function end(b,x) {
  if (won[b]) return;
  sum = 0
  for (i=1;i<=5;++i)
  for (j=1;j<=5;++j)
    sum += board[b,i,j]
  print "Win board " b " with " sum*x
  won[b] = 1
}
END {
  for (k=1; k<=length(draws); ++k) {
    x = draws[k]
    print "Drawing " x
    for (b=1;b<=nboard; ++b) {
      for (i=1;i<=5;++i) {
        for (j=1;j<=5;++j) {
          if (board[b,i,j]==x) {
            ++board[b,i,0]
            ++board[b,0,j]
            board[b,i,j]=" "
          }
        }
      }
      for (j=1;j<=5;++j)
        if (board[b,0,j]==5) end(b,x);
      for (i=1;i<=5;++i)
        if (board[b,i,0]==5) end(b,x)
    }
  }
}
