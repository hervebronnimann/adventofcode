#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <regex>
#include <string>
#include <vector>

std::map<std::string, std::map<std::string, int>> graph;

bool loadRules(const char* filename)
{
  std::ifstream input(filename);
  if (!input) {
    return false;
  }
  std::string line;
  std::regex rule("([a-z ]*) bags contain (.*)");
  std::regex dep("([0-9]*) ([a-z]* [a-z]*) bag[s,. ]*(.*)");
  std::smatch m;
  while (std::getline(input, line)) {
    if (!std::regex_match(line, m, rule) || m.size() < 3) {
      std::cout << "could not load \"" << line << "\" matches: "<< m.size() << std::endl;
      return line.empty();
    }
    std::string color(m[1].first, m[1].second);
    std::string deps(m[2].first, m[2].second);
    while (std::regex_match(deps, m, dep) && m.size() == 4) {
      int k = std::atoi(std::string(m[1].first, m[1].second).c_str());
      std::string c = std::string(m[2].first, m[2].second);
      deps.assign(m[3].first, m[3].second);
      graph[color][c] = k;
      std::cout << color << " contains " << k << " " << c << std::endl;
    }
  }
  return true;
}

void compute(const std::string& node, std::map<std::string, int>& w)
{
 w[node] = 1;
 for (auto& edge : graph[node]) {
   compute(edge.first, w);
   w[node] += w[edge.first] * edge.second;
 }
}

int main(int argc, const char **argv)
{
  std::string filename = argc > 1 ? argv[1] : "rules.txt";
  if (!loadRules(filename.c_str())) {
    return -1;
  }
  std::map<std::string, int> w;
  for (auto& n : graph) { compute(n.first, w); }
  std::cout << "Number of bags in shiny gold bag: " << w["shiny gold"]-1 << std::endl;
  return 0;
}
