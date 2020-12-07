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

int main(int argc, const char **argv)
{
  std::string filename = argc > 1 ? argv[1] : "rules.txt";
  if (!loadRules(filename.c_str())) {
    return -1;
  }
  auto trans = graph;
  int k = graph.size();
  while (k > 0) {
    auto t2 = trans; k = 0;
    for (auto& edges: t2) {
      auto& node = edges.first;
      for (auto& edges2: edges.second) {
        auto& node2 = edges2.first;
        for (auto& edge2 : graph[node2]) {
          if (trans[node][edge2.first] == 0) {
            trans[node][edge2.first] = edge2.second; ++k;
          }
        }
      }
    }
  }
  int n = 0;
  for (auto& edge: trans) {
    if (edge.second.find("shiny gold") != edge.second.end()) {
      std::cout << edge.first << " is ancestor of shiny gold\n";
      ++n;
    }
  }
  std::cout << "Ancestors of shiny gold: " << n << std::endl;
  return 0;
}
