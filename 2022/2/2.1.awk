BEGIN { score = 0; wins = 0; draws = 0; }
/A X/ { score += 1; draws += 1 }
/A Y/ { score += 2; wins += 1 }
/A Z/ { score += 3; }
/B X/ { score += 1; }
/B Y/ { score += 2; draws += 1 }
/B Z/ { score += 3; wins += 1 }
/C X/ { score += 1; wins += 1 } 
/C Y/ { score += 2; } 
/C Z/ { score += 3; draws += 1 }
END { print score + draws * 3 + wins * 6 }
