#include <fstream>
#include <iostream>
#include <string>

int numTrees(int right, int down)
{
  std::string line; char s[512];
  std::ifstream input("trees.txt");
  if (!input) {
    std::cerr << "Couldn't open trees.txt" << std::endl;
    return -1;
  }
  int n = 0, pos = 0, k = 0, len = 0;
  while (std::getline(input, line)) {
    if (len == 0) len = line.length();
    if ((k%down) == 0) {
      if (line[pos] == '#') ++n;
      pos += right; pos = pos % len;
    }
    ++k;
    if (line.length() != len) {
      std::cout << "Wrong length! " << line.length() << " len " << len << " line " << k << std::endl;
      return -1;
    }
  }
  std::cout << "numTrees(" << right << "," << down << ") = " << n << std::endl;
  return n;
}

int main(int argc, char **argv) {
  int n = 1;
  n *= numTrees(1, 1);
  n *= numTrees(3, 1);
  n *= numTrees(5, 1);
  n *= numTrees(7, 1);
  n *= numTrees(1, 2);
  std::cerr << n << "" << std::endl;
  return -1;
}
