{ ## sofar1 contains all nunmbers so far, sofar2 contains all sums of pairs of numbers so far
  if (2020-$0 in sofar2) 
    for (i in sofar1) {
      if (2020-$0-i in sofar1)
        print $0 " * " i " * " (2020-$0-i) " = " $0 * i * (2020-$0-i);
    }
  for (i in sofar1) { sofar2[$0+i] = 1; }
  sofar1[$0] = 1;
}
