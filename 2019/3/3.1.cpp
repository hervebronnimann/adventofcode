#include "input.h"
#include <algorithm>
#include <iostream>
#include <iterator>
#include <set>
#include <utility>

  using xy = std::pair<int,int>;
  using set_xy = std::set<xy>;

void trace(const strArray& i, set_xy& s)
{
  auto x=0, y=0;
  s.insert(std::make_pair(0,0));
  auto it = i.cbegin();
  while (*it) {
    switch (**it) {
    case 'D': {
      auto y1 = y + atoi(*it + 1);
      while (y != y1) { y++; s.insert(std::make_pair(x,y)); }
    } break;
    case 'U': {
      auto y1 = y - atoi(*it + 1);
      while (y != y1) { y--; s.insert(std::make_pair(x,y)); }
    } break;
    case 'R': {
      auto x1 = x + atoi(*it + 1);
      while (x != x1) { x++; s.insert(std::make_pair(x,y)); }
    } break;
    case 'L': {
      auto x1 = x - atoi(*it + 1);
      while (x != x1) { x--; s.insert(std::make_pair(x,y)); }
    } break;
    default: std::cerr << "Ooops\n"; exit(1);
    }
    ++it;
  }
}
int main() {
  set_xy pos1, pos2, inter;
  trace(instructions[0], pos1);
  trace(instructions[1], pos2);
  std::set_intersection(pos1.cbegin(), pos1.cend(), pos2.cbegin(), pos2.cend(), std::inserter(inter, inter.begin()));
  int res = 999999999;
  for (auto p : inter) {
    if (p.first == 0 && p.second == 0) continue;
    std::cout << p.first << "," << p.second << std::endl;
    res = std::min(std::abs(p.first)+std::abs(p.second), res);
  }
  std::cout << res;
  return 0;
}
