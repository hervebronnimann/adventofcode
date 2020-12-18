function eval_op(i, j, res) {
  if (j <= i) return res;
  if ($j == "+") return eval(i, j-1) + res;
  if ($j == "*") return eval(i, j-1) * res;
  print "ERROR_OP " $0 " " i " " j " " res
}
function eval(i, j) {
  if ($j ~ /[0-9]+/) return eval_op(i, j-1, $j);
  if ($j == ")") {
    level=1; for (k=j-1; level>0; --k) { if ($k == ")") ++level; if ($k == "(") --level; }
    return eval_op(i, k, eval(k+2,j-1)); 
  }
  print "ERRORP " $0 " " i " " j
}
{
  sum += eval(1, NF);
}
END { print sum; }
