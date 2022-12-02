BEGIN { score = 0; wins = 0; draws = 0; }
/A X/ { score += 3; }
/A Y/ { score += 1; draws += 1 }
/A Z/ { score += 2; wins += 1 }
/B X/ { score += 1; }
/B Y/ { score += 2; draws += 1 }
/B Z/ { score += 3; wins += 1 }
/C X/ { score += 2; } 
/C Y/ { score += 3; draws += 1 } 
/C Z/ { score += 1; wins += 1 }
END { print score + draws * 3 + wins * 6 }
