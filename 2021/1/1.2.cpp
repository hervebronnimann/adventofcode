#include <cstdio>
int main() {
  int lineno=0, n=0, x[4];
  while (scanf("%d", &x[lineno%4])>0) {
    if (lineno > 3 && x[lineno%4] > x[(lineno+3)%4]) ++n;
    ++lineno;
  }
  printf("%d\n", n);
}
