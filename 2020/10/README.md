The solution to part 1 is a single shell command:

```bash
sort -n jolt.txt | awk '{ print $1 - prev; prev = $1;}' | sort -n | uniq -c
```

For part 2, a little bit more involved:

```bash
sort -n jolt.txt| awk -f 10.2.awk 
```

where the awk code is:

```awk
BEGIN { dp[0] = 1; }
{ dp[$1] = dp[$1-1] + dp[$1-2] + dp[$1-3]; max = $1; }
END { print dp[max]; }
```
