function eval_op(i, j, res) {
  ### evaluate $i..$j-1 with an operator $j and res
  if (j <= i) return res;
  if ($j == "*") {
    # print "RECURSE_OP_MULT "i":" $i " "j-1":" $(j-1) " * " res;
    return(eval_mult(i, j-1) * res);
  }
  if ($j == "+") {
    # print "RECURSE_OP_PLUS "i":" $i " "j-1":" $(j-1) " + " res;
    return(eval_plus(i, j-1, res));
  }
  # print "ERROR_OP " $0 " " i " " j " " res
}
function eval_plus(i, j, res) {
  ### evaluate $i..$j-1 at the plus-level precendence, with possibly a trailing "+ res"
  if ($j ~ /[0-9]+/) {
    # print "RECURSE_PLUS_CST "i":" $i " "j":" $j " res:" res;
    return eval_op(i, j-1, $j + res);
  }
  if ($j == ")") {
    level=1; for (k=j-1; level>0; --k) { if ($k == ")") ++level; if ($k == "(") --level; }
    # print "RECURSE_PLUS "i":" $i " "j":" $j " " k+1 " res:" res;
    return eval_op(i,k,eval_mult(k+2,j-1) + res);  
  }
  # print "ERROR_PLUS " $0;
  return res;  
}
function eval_mult(i, j) {
  ### evaluate $i..$j-1 at the top-level precedence
  if ($j ~ /[0-9]+/) {
    # print "RECURSE_MULT_CST "i":" $i " "j":" $j;
    return prec ? eval_op(i, j-1, $j) : eval_op(i, j-1, $j);
  }
  if ($j == ")") {
    level=1; for (k=j-1; level>0; --k) { if ($k == ")") ++level; if ($k == "(") --level; }
    # print "RECURSE_MULT "i":" $i " "j":" $j " " k+1;
    return eval_op(i,k,eval_mult(k+2,j-1));  
  }
  # print "ERROR " $0;
  return res;  
}
{
  # print "LINE: " $0
  split($0, tok, " ")
  # print "LINE: " $0 " res:" eval_mult(1, length(tok));
  sum += eval_mult(1, length(tok));
}
END { print sum; }
