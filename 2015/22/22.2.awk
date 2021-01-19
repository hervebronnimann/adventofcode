function push(s,x) { queue[s,qp]=x; }
function pop(s) { return queue[s,qp]; }
function max(x,y) { return x>y?x:y; }
function play_turn(player,h,a,m,bh,ms) { # hit, mana, boss hit, mana spent
  if (bh <= 0) {
    if (verbose) print "This kills the boss, and you win.";
    if (ms < best) { print "Best score so far: " ms; best = ms; }
    return;
  }
  # effects
  for (s in t) {
    if (t[s]>0) {
      --t[s]; m += mana[s]; a+=arm[s]; bh -= dam[s];
      if (verbose) {
        if (dam[s]>0) print s " deals " dam[s] " damage; its timer is now " t[s];
        else if (arm[s]>0) print s"'s timer is now " t[s];
        else if (mana[s]>0) print s " provides "mana[s]" mana; its timer is now "t[s];
        if (t[s]==0) print s " wears off."
      }
    }
    if (bh <= 0) {
      if (verbose) print "This kills the boss, and you win.";
      if (ms < best) { print "Best score so far: " ms; best = ms; }
      return;
    }
  }
  # boss turn
  if (player == 0) {
    if (verbose) {
      print "-- Boss turn -- ("qp")";
      print "- Player has "h" hit points, "a" armor, "m" mana";
      print "- Boss has "bh" hit points";
      d=bdam; if (a>0) d=d " - " a " = " max(1,bdam-a);
      print "Boss attacks for "d" damage";
    }
    h -= max(1,bdam-a);
    if (verbose && h<=0) print "This kills you, and the boss wins.";
    if (h <= 0) return; else play_turn(1,h,0,m,bh,ms);
    return;
  }
  # player turn
  if (verbose) {
    print "-- Player turn -- ("qp+1")";
    print "- Player has "h" hit points, "a" armor, "m" mana";
    print "- Boss has "bh" hit points";
  }
  # early termination, unless there is infinite recursion due to mana being regenerated
  if (--h <= 0) {
    if (verbose) print "You lose a point for your turn, this kills you, and the boss wins.";
    return;
  }
  if (ms > best) { 
    if (verbose) print "Exceeded best score already, stopping recursion...";
    return;
  }
  # You cannot cast a spell that would start an effect which is already active. However, effects can be started on the same turn they end.
  for (i=1; i<=5; ++i) {
    s = spell[i];
    if (t[s] > 0) continue;
    if (m < cost[s]) continue;
    ++qp; push("idx",i); push("spell",s); for (x in t) push(x,t[x]);
    if (turn[s]==0) {
      if (dam[s]>0) hh=", dealing "dam[s]" damage"
      if (heal[s]>0) hh=hh ", and healing "heal[s]" hit points"
      if (verbose) print "Player casts " s hh " [turn " qp "]";
      bh-=dam[s]; h+=heal[s];
    } else {
      if (verbose) print "Player casts " s " [turn " qp "]";
      t[s]=turn[s];
    }
    play_turn(0,h,0,m-cost[s],bh,ms+cost[s]);
    if (verbose) print "Player backtracking at turn " qp;
    i=pop("idx"); s=pop("spell"); for (x in t) t[x] = pop(x); --qp;
    if (turn[s]==0) { bh+=dam[s]; h-=heal[s]; }
  }
}
BEGIN {
  phit=50; pmana=500; best=9999999;
  s="Missile";  spell[1]=s; cost[s]=53; dam[s]=4; turn[s]=0;
  s="Drain";    spell[2]=s; cost[s]=73; dam[s]=2; heal[s]=2; turn[s]=0;
  s="Shield";   spell[3]=s; cost[s]=113; turn[s]=6; arm[s]=7;
  s="Poison";   spell[4]=s; cost[s]=173; turn[s]=6; dam[s]=3;
  s="Recharge"; spell[5]=s; cost[s]=229; turn[s]=5; mana[s]=101;
}
/^Hit:/    { bhit = $2; }
/^Damage:/ { bdam = $2; }
END {
  play_turn(1,phit,0,pmana,bhit,0);
  print best; #TODO play winning game...
}
