#include "input.h"
#include <iostream>
#include <string>
#include <map>
#include <set>

int main() {
  map<string,set<string>> closure;
  for (const auto& edge : input) {
    closure[edge.first].insert(edge.second);
  }
  bool new_edge = true;
  while (new_edge) {
    new_edge = false;
    for (const auto& edge : input) {
      for (auto node : closure[edge.second]) {
        if (closure[edge.first].insert(node).second) {
          // cout << "Adding " << edge.second << ")" << node << " to " << edge.first << endl;
          new_edge = true;
        }
      }
    }
  }
  auto result{0};
	for (const auto& nodeset : closure) {
     result += nodeset.second.size();
  }
  std::cout << result << std::endl;
  return 0;
}
