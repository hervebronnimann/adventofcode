function eval_op(i, j, res) {
  if (j <= i) return res;
  if ($j == "*") return eval_mult(i, j-1) * res;
  if ($j == "+") return eval_plus(i, j-1, res);
  print "ERROR_OP " $0 " " i " " j " " res
}
function eval_plus(i, j, res) {
  if ($j ~ /[0-9]+/) return eval_op(i, j-1, $j + res);
  if ($j == ")") {
    level=1; for (k=j-1; level>0; --k) { if ($k == ")") ++level; if ($k == "(") --level; }
    return eval_op(i,k,eval_mult(k+2,j-1) + res);  
  }
  print "ERROR_PLUS " $0 " " i " " j " " res
}
function eval_mult(i, j) {
  if ($j ~ /[0-9]+/) return eval_op(i, j-1, $j);
  if ($j == ")") {
    level=1; for (k=j-1; level>0; --k) { if ($k == ")") ++level; if ($k == "(") --level; }
    return eval_op(i,k,eval_mult(k+2,j-1));  
  }
  print "ERROR_MULT " $0 " " i " " j
}
{
  split($0, tok, " ")
  sum += eval_mult(1, length(tok));
}
END { print sum; }
