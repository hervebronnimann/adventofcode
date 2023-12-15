#include "input.h"
#include <algorithm>
#include <iostream>
#include <iterator>
#include <map>
#include <utility>

  using xy = std::pair<int,int>;
  using set_xy = std::map<xy,int>;

void trace(const strArray& i, set_xy& s)
{
  auto x=0, y=0, n=-1;
  s[std::make_pair(0,0)] = ++n;
  auto it = i.cbegin();
  while (*it) {
    switch (**it) {
    case 'D': {
      auto y1 = y + atoi(*it + 1);
      while (y != y1) { y++; s.try_emplace(std::make_pair(x,y),++n); }
    } break;
    case 'U': {
      auto y1 = y - atoi(*it + 1);
      while (y != y1) { y--; s.try_emplace(std::make_pair(x,y),++n); }
    } break;
    case 'R': {
      auto x1 = x + atoi(*it + 1);
      while (x != x1) { x++; s.try_emplace(std::make_pair(x,y),++n); }
    } break;
    case 'L': {
      auto x1 = x - atoi(*it + 1);
      while (x != x1) { x--; s.try_emplace(std::make_pair(x,y),++n); }
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
  int res = 999999999;
  for (auto& p : pos1) {
    if (p.first.first == 0 && p.first.second == 0) continue;
    if (pos2.find(p.first) != pos2.cend()) {
      std::cout << p.first.first << "," << p.first.second << std::endl;
      res = std::min(p.second + pos2[p.first], res);
    }
  }
  std::cout << res;
  return 0;
}
