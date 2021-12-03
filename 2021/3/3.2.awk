{ 
  n = NF
  eline[NR] = " " $0
  gline[NR] = " " $0
}
END  {
  p2=2**(n-1);
  for (i=1; i<=n; ++i) {
    for (e in eline) {
      split(eline[e],a," ");
      cnte[i,a[i]] = cnte[i,a[i]]+1;
    }
    if (cnte[i,1]>=cnte[i,0]) { epsilon += p2; eepsilon = eepsilon " 1" } else { eepsilon = eepsilon " 0" }
    for (e in eline) {
      if (substr(eline[e],1,2*i) != eepsilon) { print "OXY", i, "deleting " eline[e]; delete eline[e]; }
    }
    if (length(eline) == 1) for (e in eline) {
      oxygen = epsilon; q2 = p2;
      split(eline[e],a," ");
      for (j=i+1; j<=n; ++j) {
        if (a[j+1] == "1") oxygen += q2;
        q2 /= 2;
      }
      print "Found Oxygen:", eline[e], " value", oxygen;
    }
    for (g in gline) {
      split(gline[g],b," ");
      cntg[i,b[i]] = cntg[i,b[i]]+1;
    }
    if (cntg[i,1]<cntg[i,0]) { gamma += p2; ggamma = ggamma " 1"; } else { ggamma = ggamma " 0"; }
    p2 /= 2;
    for (g in gline) {
      if (substr(gline[g],1,2*i) != ggamma) { print "CO2", i, "deleting " gline[g]; delete gline[g]; }
    }
    if (length(gline) == 1)
      for (g in gline) {
        co2 = gamma; q2 = p2;
        split(gline[g],b," ");
        for (j=i+1; j<=n; ++j) {
          if (b[j+1] == "0") co2 += q2;
          q2 /= 2;
        }
        print "Found CO2:", gline[g], " value", co2;
      }
  }
  print oxygen * co2;
}
