#include <fstream>
#include <iostream>
#include <unordered_set>
#include <unordered_map>

int main() {
  int x;
  std::ifstream input("2.txt");
  std::unordered_set<int> s1;
  std::unordered_map<int,int> s2;
  if (!input) {
    std::cerr << "Couldn't open 1.txt" << std::endl;
    return -1;
  }
  while (input >> x) {
    for (int z : s1) s2[x+z] = x*z;  // add map of sum to product of two previous numbers
    int y = 2020 - x, z1 = -1, z2 = -1;
    if (s2.find(y) != s2.end()) {
      for (int z : s1) {
	if (s1.find(y-z) != s1.end()) {
          z1 = z; z2 = y - z1; break;
	}
      }
      std::cout << x << " * " << z1 << " * " << z2 << " = " << x*z1*z2 << std::endl;
      return 0;
    }
    s1.insert(x);
  }
  std::cerr << "Couldn't find triple summing up to 2020 in 1.txt" << std::endl;
  return -1;
}
