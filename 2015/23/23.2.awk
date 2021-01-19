{ code[NR]=$1; arg1[NR]=$2; if ($1 ~ /^ji/) arg2[NR]=$3; }
END {
  i=1; reg["a"]=1;
  while (i>0 && i<= NR) {
    if (verbose) print "Line: "i" a:"reg["a"]" b:"reg["b"]" Executing: "code[i]" "arg1[i]" "arg2[i];
    if (code[i] == "hlf") reg[arg1[i]] /= 2;
    if (code[i] == "tpl") reg[arg1[i]] *= 3;
    if (code[i] == "inc") ++reg[arg1[i]];
    if (code[i] == "jmp") i += arg1[i]-1;
    if (code[i] == "jie") if (reg[arg1[i]]%2 == 0) i += arg2[i]-1;
    if (code[i] == "jio") if (reg[arg1[i]] == 1) i += arg2[i]-1;
    ++i;
  }
  print reg["b"];
}
