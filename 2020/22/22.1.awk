function min(x,y) { return x<y? x : y; }
function max(x,y) { return x>y? x : y; }
BEGIN { m1 = 1; m2 = 1; n1 = 0; n2 = 0; player = 0; }
/^Player/ { ++player; next;}
/^[0-9]+$/ { print "Player " player " gets " $1; if (player == 1) deck1[++n1] = $1; else deck2[++n2] = $1; }
END {
  while (m1 <= n1 && m2 <= n2) {
    print "-- Round " ++round " --"
    deck = "Player 1's deck: "
    for (i=m1; i<=n1; ++i) deck = deck " " deck1[i];
    print deck
    deck = "Player 2's deck: "
    for (i=m2; i<=n2; ++i) deck = deck " " deck2[i];
    print deck
    print "Player 1 plays: " deck1[m1];
    print "Player 2 plays: " deck2[m2];
    if (deck1[m1] > deck2[m2]) {
      print "Player 1 wins the round"
      deck1[++n1] = deck1[m1++]; deck1[++n1] = deck2[m2++];
    } else {
      print "Player 2 wins the round"
      deck2[++n2] = deck2[m2++]; deck2[++n2] = deck1[m1++];
    }
  }
  score = 0; k = 0;
  while (m1 <= n1) { score += deck1[n1--] * ++k; }
  while (m2 <= n2) { score += deck2[n2--] * ++k; }
  print score;
}
