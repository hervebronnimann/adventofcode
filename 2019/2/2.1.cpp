#include "input.h"
#include <iostream>
#include <string>

int main() {
  positions[1]=12; positions[2]=2;
  for (int i=0; i < size; ++i) {
    auto code=positions[i];
    auto j=positions[++i], k=positions[++i], l=positions[++i];
    if (code==1) {
      positions[l] = positions[j] + positions[k];
    } else if (code==2) {
      positions[l] = positions[j] * positions[k];
    } else if (code==99) {
      break;
    } else {
      exit(1);
    }
  }
  std::cout << positions[0] << std::endl;
  return 0;
}
