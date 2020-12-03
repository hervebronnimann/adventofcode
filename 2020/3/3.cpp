#include <fstream>
#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> trees;

bool loadTrees(const char* filename)
{
  std::ifstream input(filename);
  if (!input) {
    return false;
  }
  std::string line; int len = 0, k = 0;
  while (std::getline(input, line)) {
    ++k;
    if (len == 0) len = line.length();
    if (line.length() != len) {
      std::cout << "Wrong length! " << line.length() << " len " << len << " line " << k << std::endl;
      return false;
    }
    trees.push_back(line);
  }
  return true;
}

int numTrees(int right, int down)
{
  int n = 0, pos = 0, k = 0, len = 0;
  for (auto& line : trees) {
    if (len == 0) len = line.length();
    if ((k%down) == 0) {
      if (line[pos] == '#') ++n;
      pos += right; pos = pos % len;
    }
    ++k;
  }
  std::cout << "numTrees(" << right << "," << down << ") = " << n << std::endl;
  return n;
}

int main(int argc, char **argv) {
  auto filename = argc > 1 ? argv[1] : "trees.txt";
  if (!loadTrees(filename)) {
    std::cerr << "Couldn't open " << filename << std::endl;
    return -1;
  }
  int n = 1;
  n *= numTrees(1, 1);
  n *= numTrees(3, 1);  // this is first half
  n *= numTrees(5, 1);
  n *= numTrees(7, 1);
  n *= numTrees(1, 2);
  std::cerr << "Solution: " << n << std::endl;
  return -1;
}
