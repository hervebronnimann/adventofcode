#include "input.h"
#include <cstdint>
#include <deque>
#include <iostream>
#include <string>
#include <vector>

struct Amp {

  // Abuse default ctor by using the globals
  std::vector<int> p{positions, positions+size};
  bool done{false};
  std::deque<int> input;
  std::deque<int> output;
  int i{0};

  int run() {
    int inp = -1;
    for (; i < size; ++i) {
      auto code=p[i]%100;
      auto p1mode=(p[i]%1000)/100;
      auto p2mode=(p[i]%10000)/1000;
      if (code==1) {
        if (size<=i+3) return -1;
        auto j=p[++i], k=p[++i], l=p[++i];
        if (j>=size || k>=size || l>=size) return -1;
        p[l] = (p1mode ? j : p[j]) + (p2mode ? k : p[k]);
      } else if (code==2) {
        if (size<=i+3) return -1;
        auto j=p[++i], k=p[++i], l=p[++i];
        if (j>=size || k>=size || l>=size) return -1;
        p[l] = (p1mode ? j : p[j]) * (p2mode ? k : p[k]);
      } else if (code==3) {
        if (size<=i+1) return -1;
        auto j=p[++i];
        if (j>=size) return -1;
        if (!input.empty()) {
          p[j] = input.front();
          input.pop_front();
        } else {
          // Wait until there is more input, then resume()
          break;
        }
      } else if (code==4) {
        if (size<=i+1) return -1;
        auto j=p[++i];
        if (j>=size) return -1;
        output.push_back(p[j]);
      } else if (code==5) {
        if (size<=i+2) return -1;
        auto j=p[++i], k=p[++i];
        if (p1mode ? j : p[j]) { i = (p2mode ? k : p[k]) - 1; }
      } else if (code==6) {
        if (size<=i+2) return -1;
        auto j=p[++i], k=p[++i];
        if (!(p1mode ? j : p[j])) { i = (p2mode ? k : p[k]) - 1; }
      } else if (code==7) {
        auto j=p[++i], k=p[++i], l=p[++i];
        if (j>=size || k>=size || l>=size) return -1;
        p[l] = (p1mode ? j : p[j]) < (p2mode ? k : p[k]) ? 1 : 0;
      } else if (code==8) {
        auto j=p[++i], k=p[++i], l=p[++i];
        if (j>=size || k>=size || l>=size) return -1;
        p[l] = (p1mode ? j : p[j]) == (p2mode ? k : p[k]) ? 1 : 0;
      } else if (code==99) {
        done = true;
        break;
      } else {
        return -1;
      }
    }
    return 0;
  }

  int resume() {
    auto j = p[i];
    if (input.empty()) return -1;
    p[j] = input[0];
    input.pop_front();
    ++i;
    return run();
  }
};

int main() {
  // int amps[] = {5,6,7,8,9};
  int amps[] = {9,8,7,6,5};
  int xmax = INT_MIN;
  do {
    Amp a[5] = {};
    for (int k = 0; k < 5; ++k) {
      a[k].input.push_back(amps[k]);
    }
    a[0].input.push_back(0);
    auto i = 0;
    while (i < 5) {
      a[i].run();
      if (!a[i].done) {
        while (!a[i].output.empty()) {
          a[(i+1)%5].input.push_back(a[i].output.front());
          a[i].output.pop_front();
        }
      }
      i = (i+1)%5;
    }
    while (!a[i].done) {
      a[i].resume();
      if (!a[i].done) {
        while (!a[i].output.empty()) {
          a[(i+1)%5].input.push_back(a[i].output.front());
          a[i].output.pop_front();
        }
      }
      i = (i+1)%5;
    }
    if (i != 4 || a[4].output.size() != 1) {
      std::cout << "Not clean termination" << std::endl;
    }
    if (a[4].output.front() > xmax)
      xmax = a[4].output.front();
  } while ( false ); // std::next_permutation(amps,amps+5) );
  std::cout << xmax << std::endl;
  return 0;
}

