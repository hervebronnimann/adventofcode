
{ sum+=$1; weight[NR]=$1; } 
END {
  if (sum%3!=0) print "Impossible (sum="sum")";
  sum /= 3; print "Sum: " sum;
  # Dynamic programming: figure out how many ways to make up sum
  # n[i,k,q] = number of ways to sum up to i with exactly q records among 1..k
  n[0,0,0]=1;
  for (i=1; i<=sum; ++i)
  for (k=1; k<=NR; ++k)
  for (q=0; q<=NR; ++q) {
    j = weight[k];
    n[i,k,q]=n[i-j,k-1,q-1]+n[i,k-1,q];
    if (i==sum && n[i-j,k-1,q-1]>0) { p[q] = p[q] " " j"["q"]:"n[i-j,k-1,q-1] }
  }
  for (q=1; q<=NR; ++q) {
    if (n[sum,NR,q] == 0) continue;
    print "With "q": "n[sum,NR,q] " ways, using" p[q];
  }
# # now that we've done that, and we think the numbers reasonable, figure out the subsets themselves
# # this of course blows up...
# m[0,0]="0";
# for (i=1; i<=sum; ++i)
# for (k=1; k<=NR; ++k) {
#   j = weight[k];
#   m[i,k]=m[i,k-1];
#   if (n[i-j,k-1]>0) {
#     split(m[i-j,k-1],s,";");
#     p=""; for (q=1;q<=length(s);++q) p = p ";" j","s[q];
#     m[i,k]=m[i,k] p;
#   }
# }
# print m[sum,NR];
}
