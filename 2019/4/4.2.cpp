#include <iostream>

int range0[2] = { 245318, 765747 };

bool validPassword(int i) {
  // It is a six-digit number within the range given in your puzzle input.
  // Two adjacent digits are the same (like 22 in 122345), and exactly two for some digit
  // Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
  int x=i%10;
  bool dup = false;
  int cons=1; // consecutive digits
  while (i>0) {
    i=i/10;
    int y=i%10;
    if (x<y) return false;
    if (x==y) ++cons;
    else {
      dup |= cons==2;
      cons = 1;
    }
    x = y;
  }
  return dup;
}

int main()
{
  // Part 1:
  int count = 0;
  for (int i=range0[0]; i<=range0[1]; ++i) {
    if (validPassword(i)) ++count;
  }
  std::cout << count << std::endl;
  return 0;
}
