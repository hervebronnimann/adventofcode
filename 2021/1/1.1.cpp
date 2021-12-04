#include <cstdio>
int main() {
  int lineno=0, n=0, x, prev;
  while (scanf("%d", &x)>0) {
    if (lineno > 0 && x > prev) ++n;
    ++lineno; prev = x;
  }
  printf("%d\n", n);
}
