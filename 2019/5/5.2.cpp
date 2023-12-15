#include "input.h"
#include <iostream>
#include <string>
#include <vector>

int run(const int positions[], int size, int input) {
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
      p[j] = input;
    } else if (code==4) {
      if (size<=i+3) return -1;
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
  std::cout << run(positions, size, 5) << std::endl;
  return 0;
}

