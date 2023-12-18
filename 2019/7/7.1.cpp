#include "input.h"
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

int run(const int positions[], int size, std::vector<int> input) {
  int inp = -1;
  int output = -1;
  std::vector<int> p(positions, positions+size);
  for (int i=0; i < size; ++i) {
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
      p[j] = input[++inp];
    } else if (code==4) {
      if (size<=i+1) return -1;
      auto j=p[++i];
      if (j>=size) return -1;
      output = p[j];
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
      break;
    } else {
      return -1;
    }
  }
  return output;
}

int main() {
  int amps[] = {0,1,2,3,4};
  int xmax = INT_MIN;
  do {
      auto x = 0;
      for (int i = 0; i < 5; ++i)
        x = run(positions, size, {amps[i], x});
      if (x > xmax) xmax = x;
  } while ( std::next_permutation(amps,amps+5) );
  std::cout << xmax << std::endl;
  return 0;
}

