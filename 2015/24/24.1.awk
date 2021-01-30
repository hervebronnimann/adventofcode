function min(x,y) { return x<y ? x : y; }
function compute_qe(s) {
  qe = 1;
  split(s,c," "); for (i in c) qe *= c[i];
  return qe;
}
function compute(i,k,s) {
  delete m; delete w; delete c;
  split(s,c," "); for (i in c) w[c[i]] = 1;
  m[0,0]=1;
  for (i=0; i<=sum; ++i)
  for (k=1; k<=NR; ++k) {
    m[i,k]=m[i,k-1];
    if (!(weight[k] in w)) m[i,k] += m[i-weight[k],k-1];
    # else if (m[i-weight[k],k-1] > 0) print "--skipping " m[i-weight[k],k-1] " because " weight[k] " is in " s;
  }
  return m[sum,NR];
}
function find_rec(i,k,q,s) {
  if (q==0) {
    t=compute(1,1,s); qe=compute_qe(s); min_qe=min(qe,min_qe);
    if (t>=0) print "Using " s " : " t " qe:" compute_qe(s) " " (qe==min_qe ? "***" : "");
    return;
  }
  for (l=1; l<=k; ++l)
    if (n[i-weight[l],l-1,q-1]>0)
      find_rec(i-weight[l],l-1,q-1,s" "weight[l]);
}
{ sum+=$1; weight[NR]=$1; } 
END {
  if (sum%3!=0) print "Impossible (sum="sum")";
  sum /= 3; print "Sum: " sum;
  # Dynamic programming: figure out how many ways to make up sum
  # n[i,k,q] = number of ways to sum up to i with exactly q records among 1..k
  n[0,0,0]=1;
  for (i=0; i<=sum; ++i)
  for (k=1; k<=NR; ++k)
  for (q=0; q<=NR; ++q) {
    j = weight[k];
    n[i,k,q]=n[i-j,k-1,q-1]+n[i,k-1,q];
    if (i==sum && n[i-j,k-1,q-1]>0) { p[q] = p[q] " " j"["q"]:"n[i-j,k-1,q-1] }
  }
  for (q=1; q<=NR; ++q) {
    min_qe = 9.999999E123;
    if (n[sum,NR,q] == 0) continue;
    print "With "q": "n[sum,NR,q] " ways, using" p[q];
    if (q<=6) {
      find_rec(sum,NR,q,"");
      print "With "q": "n[sum,NR,q] " ways, using" p[q] " min_qe:" min_qe;
    }
  }
}
