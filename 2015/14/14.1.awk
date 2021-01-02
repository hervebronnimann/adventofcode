function min(x,y) { return x<y?x:y; }
BEGIN { race = 2503; }
{ speed = $4; run = $7; rest = $14;
  runs = int(race / (run + rest));
  rem = race - runs * (run + rest);
  dist = speed * (run * runs + min(rem,run));
  print $1 " ran " dist " mad up of " runs " times " run " seconds at top speed " speed " km/s, followed by " rest " seconds rest each, and " min(rem,run) " seconds at top speed(plus maybe rest)"
}
