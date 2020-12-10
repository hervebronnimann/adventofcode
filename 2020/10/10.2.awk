BEGIN { dp[0] = 1; }
{ dp[$1] = dp[$1-1] + dp[$1-2] + dp[$1-3]; max = $1; }
END { print dp[max]; }

