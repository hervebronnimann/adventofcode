function min(x,y) { return x<y ? x : y; }
function area(l,w,h) { a1=l*w; a2=l*h; a3=w*h; return 2*a1 + 2*a2 + 2*a3 + min(a1,min(a2,a3)); }
{ split($0,s,"x"); sum += area(s[1],s[2],s[3]); }
END{ print sum; }
