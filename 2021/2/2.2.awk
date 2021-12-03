/^forward/ { x+=$2; z+=$2*y }
/^down/ { y+=$2; }
/^up/ { y-=$2; }
END {print x * z}
