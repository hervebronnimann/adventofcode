#include "input.h"
#include <iostream>
#include <string>
#include <vector>

int run(int positions[], int noun, int verb) {
  std::vector<int> p(positions, positions+size);
  p[1]=noun; p[2]=verb;
  for (int i=0; i < size; ++i) {
    auto code=p[i];
    if (code==1) {
      if (size<=i+3) return -1;
      auto j=p[++i], k=p[++i], l=p[++i];
      if (j>=size || k>=size || l>=size) return -1;
      p[l] = p[j] + p[k];
    } else if (code==2) {
      if (size<=i+3) return -1;
      auto j=p[++i], k=p[++i], l=p[++i];
      if (j>=size || k>=size || l>=size) return -1;
      p[l] = p[j] * p[k];
    } else if (code==99) {
      break;
    } else {
      return -1;
    }
  }
  return p[0];
}

int main() {
  for (int n=0; n<100; ++n)
  for (int v=0; v<100; ++v) {
    if (run(positions, n, v) == 19690720)
      std::cout << n*100+v << std::endl;
  }
  return 0;
}

