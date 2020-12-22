function min(x,y) { return x<y? x : y; }
function max(x,y) { return x>y? x : y; }
BEGIN { m1 = 1; m2 = 1; n1 = 0; n2 = 0; player = 0; }
/^Player/ { ++player; next;}
/^[0-9]+$/ { if (player == 1) deck1[++n1] = $1; else deck2[++n2] = $1; }
function play_game(game,round,m1,n1,m2,n2) {
  print "=== Game " game " ===\n"
  while (m1 <= n1 && m2 <= n2) {
    print "-- Round " ++round " (Game " game ") --"
    d1 = "Player 1's deck: "; for (i=m1; i<=n1; ++i) d1 = d1 (i>m1?", ":"") deck1[i]; print d1;
    d2 = "Player 2's deck: "; for (i=m2; i<=n2; ++i) d2 = d2 (i>m2?", ":"") deck2[i]; print d2;
    if ((game,d1) in decks1 && (game,d2) in decks2 && decks1[game,d1] == decks2[game,d2]) {
      print "Previous decks encountered, automatic win for player 1!"
      return 1;
    } else {
      decks1[game,d1] == round;
      decks2[game,d2] == round;
      deck = "Player 2's deck: "
        print "Player 1 plays: " deck1[m1];
      print "Player 2 plays: " deck2[m2];
      if (deck1[m1] <= n1-m1 && deck2[m2] <= n2-m2) {
        print "Playing a sub-game to determine the winner...\n";
        # Note that m1+1+deck1[m1]-1 <= n1 && m2+1+deck2[m2]-1 <= n2
        m3 = n1 + 1; n3 = m3-1; for (i=0; i<deck1[m1]; ++i) deck1[++n3]=deck1[m1+1+i];
        m4 = n2 + 1; n4 = m4-1; for (i=0; i<deck2[m2]; ++i) deck2[++n4]=deck2[m2+1+i];
        winner = play_game(++ngame,0,m3,n3,m4,n4);
        print "...anyway, back to game " game "."
      } else {
        winner = deck1[m1] > deck2[m2] ? 1 : 2;
      }
    }

    if (winner==1) {
      print "Player 1 wins round " round " of game " game "!\n"
      deck1[++n1] = deck1[m1++]; deck1[++n1] = deck2[m2++];
    } else {
      print "Player 2 wins round " round " of game " game "!\n"
      deck2[++n2] = deck2[m2++]; deck2[++n2] = deck1[m1++];
    }
  }
  lastn1=n1;lastn2=n2;lastm1=m1;lastm2=m2; # can't pass as result;
  print "The winner of game " game " is player " winner "!\n";
  return winner;
}
END {
  ngame = 1; play_game(ngame,0,m1,n1,m2,n2);
  n1=lastn1;n2=lastn2;m1=lastm1;m2=lastm2;
  score = 0; k = 0;
  print "\n== Post-game results =="
  d1 = "Player 1's deck: "; for (i=m1; i<=n1; ++i) d1 = d1 (i>m1?", ":"") deck1[i]; print d1;
  while (m1 <= n1) { score += deck1[n1--] * ++k; }
  d2 = "Player 2's deck: "; for (i=m2; i<=n2; ++i) d2 = d2 (i>m2?", ":"") deck2[i]; print d2;
  while (m2 <= n2) { score += deck2[n2--] * ++k; }
  print score;
}
