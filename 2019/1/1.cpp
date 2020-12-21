#include "input.h"
#include <iostream>

int main() {
  int sum = 0;
  for (auto x : input) {
    sum += (x/3)-2;
  }
  std::cout << sum << std::endl;
  return 0;
}
