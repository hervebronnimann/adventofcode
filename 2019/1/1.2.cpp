#include "input.h"
#include <iostream>

int main() {
  int sum = 0;
  for (auto x : input) {
    auto y = (x/3)-2;
    do { sum += y; y = (y/3)-2; } while (y>0);
  }
  std::cout << sum << std::endl;
  return 0;
}
