#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <cstdio>

int main(int argc, char **argv) {
  bool verbose{argc > 1};
  int x, y; char z; std::string line; char s[512];
  std::ifstream input("pwd.txt");
  if (!input) {
    std::cerr << "Couldn't open pwd.txt" << std::endl;
    return -1;
  }
  int n = 0;
  while (std::getline(input, line)) {
    if (sscanf(line.c_str(), "%d-%d %c: %s", &x, &y, &z, s) != 4) continue;
    int len = strlen(s);
    int m = std::count(s, s+len, z);
    bool valid{m >= x && m <= y};
    if (valid) ++n;
    if (verbose)
      std::cout << "Password '" << s << "' " << (valid ? "valid" : "invalid")
                << " according to policy " << x << "-" << y << " " << z << std::endl;
  }
  std::cerr << n << "" << std::endl;
  return -1;
}
