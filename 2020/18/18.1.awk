function eval_op(i, j, res) {
  ### evaluate $i..$j-1 with an operator $j and res
  if (j <= i) return res;
  if ($j == "+") {
    # print "RECURSE_OP "i":" $i " "j-1":" $(j-1) " + " res;
    return(eval(i, j-1) + res);
  }
  if ($j == "*") {
    # print "RECURSE_OP "i":" $i " "j-1":" $(j-1) " * " res;
    return(eval(i, j-1) * res);
  }
  # print "ERROR_OP " $0 " " i " " j " " res
}
function eval(i, j) {
  if ($j ~ /[0-9]+/) {
    # print "RECURSE_CST "i":" $i " "j":" $j;
    return eval_op(i, j-1, $j);
  }
  if ($j == ")") {
    level=1; for (k=j-1; level>0; --k) { if ($k == ")") ++level; if ($k == "(") --level; }
    # print "RECURSE "i":" $i " "j":" $j " " k+1;
    return eval_op(i, k, eval(k+2,j-1)); 
  }
  # print "ERROR " $0;
  return res;  
}
{
  # print "LINE: " $0 " res:" eval(1, NF);
  sum += eval(1, NF);
}
END { print sum; }
