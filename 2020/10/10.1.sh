sort -n jolt.txt | awk '{ print $1 - prev; prev = $1;}' | sort -n | uniq -c
