#include "input.h"
#include <iostream>
#include <string>
#include <map>
#include <set>

int main() {
  map<string,string> orbit;
  for (const auto& edge : input) {
    if (orbit.find(edge.second) != orbit.cend()) {
    }
    orbit[edge.second] = edge.first;
  }
  orbit["COM"] = "ORIGIN";
  orbit["ORIGIN"] = "ORIGIN";
  string current = "YOU";
  map<string,int> you;
  int transfers = 0;
  while (current != orbit[current]) {
    current = orbit[current];
    if (current == "SAN") {
      cout << "Direct orbital " << transfers-1 << endl;
      return 0;
    }
    you[current] = ++transfers;
  }
  vector<string> santa;
  current = "SAN";
  while (current != orbit[current]) {
    current = orbit[current];
    santa.push_back(current);
    if (you.find(current) != you.cend()) {
      cout << "Common orbital " << current << " after " << santa.size() << " at depth " << you[current] << endl;
      cout << santa.size() +  you[current] - 2 << endl;
      return 0;
    }
  }
  std::cout << "No common orbital" << std::endl;
  return 0;
}
