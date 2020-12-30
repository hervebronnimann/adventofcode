function not(x) { return 65535 - x; }
function and(x,y) { res = 0; for (i=1;i<65536;i*=2) { if ((x%2==1) && (y%2==1)) res += i; x = int(x/2); y = int(y/2); } return res; }
function or(x,y) { res = 0; for (i=1;i<65536;i*=2) { if ((x%2==1) || (y%2==1)) res += i; x = int(x/2); y = int(y/2); } return res; }
function lshift(x,k) { while (k-- > 0 && x > 0) x = (x*2) % 65536; return x; }
function rshift(x,k) { while (k-- > 0 && x > 0) x = int(x/2); return x; } 
function value(e) { 
  if (e in val) return val[e];
  if (e ~ /^[0-9]+$/) val[e] = e;
  else if (op[e] == "copy") val[e] = value(op1[e]);
  else if (op[e] == "and") val[e] = and(value(op1[e]), value(op2[e]));
  else if (op[e] == "or") val[e] = or(value(op1[e]), value(op2[e]));
  else if (op[e] == "not") val[e] = not(value(op1[e]));
  else if (op[e] == "lshift") val[e] = lshift(value(op1[e]), value(op2[e]));
  else if (op[e] == "rshift") val[e] = rshift(value(op1[e]), value(op2[e]));
  else { print ("WTF!!!"); val[e] = 0; }
  return val[e];
}
/^NOT /   { op[$4] = "not"; op1[$4] = $2; }
/ OR /     { op[$5] = "or"; op1[$5] = $1; op2[$5] = $3; }
/ AND /    { op[$5] = "and"; op1[$5] = $1; op2[$5] = $3; }
/ LSHIFT / { op[$5] = "lshift"; op1[$5] = $1; op2[$5] = $3; }
/ RSHIFT / { op[$5] = "rshift"; op1[$5] = $1; op2[$5] = $3; }
NF==3 && $2 == "->" { op[$3] = "copy"; op1[$3] = $1; }
END { print value("a"); }
# END { for (e in op) print e ": " value(e); }
