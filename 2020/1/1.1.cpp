#include <fstream>
#include <iostream>
#include <unordered_set>

int main() {
  int x;
  std::ifstream input("1.txt");
  std::unordered_set<int> s;
  if (!input) {
    std::cerr << "Couldn't open 1.txt" << std::endl;
    return -1;
  }
  while (input >> x) {
    int y = 2020 - x;
    if (s.find(y) != s.end()) {
      std::cout << x << " * " << y << " = " << x*y << std::endl;
      return 0;
    }
    s.insert(x);
  }
  std::cerr << "Couldn't find pair summing up to 2020 in 1.txt" << std::endl;
  return -1;
}
