A clumsy first attempt:

```bash
sort -n 1.txt > 1.sort.txt
awk '{print 2020 - $1;}' 1.sort.txt | sort -n > 1.comp.txt
vimdiff 1.*.txt
```

Then a cleaner code in c++:

```c++
#include <fstream>
#include <iostream>
#include <unordered_set>

int main() {
  int x;
  std::ifstream input("1.txt");
  std::unordered_set<int> s;
  if (!input) {
    std::cerr << "Couldn't open 1.txt" << std::endl;
    return -1;
  }
  while (input >> x) {
    int y = 2020 - x;
    if (s.find(y) != s.end()) {
      std::cout << x << " * " << y << " = " << x*y << std::endl;
      return 0;
    }
    s.insert(x);
  }
  std::cerr << "Couldn't find pair summing up to 2020 in 1.txt" << std::endl;
  return -1;
}
```

And the winning one-liner: 

```awk
awk 'NR==FNR { lines[2020-$0]=1; next } $0 in lines' "1.txt" "1.txt"
```

Unfortunately, for the second question (triples) this doesn't work any more.
The simplest answer is to extend the c++ code:

```c++
#include <fstream>
#include <iostream>
#include <unordered_set>
#include <unordered_map>

int main() {
  int x;
  std::ifstream input("2.txt");
  std::unordered_set<int> s1;
  std::unordered_map<int,int> s2;
  if (!input) {
    std::cerr << "Couldn't open 1.txt" << std::endl;
    return -1;
  }
  while (input >> x) {
    for (int z : s1) s2[x+z] = x*z;  // add map of sum to product of two previous numbers
    int y = 2020 - x, z1 = -1, z2 = -1;
    if (s2.find(y) != s2.end()) {
      for (int z : s1) {
	if (s1.find(y-z) != s1.end()) {
          z1 = z; z2 = y - z1; break;
	}
      }
      std::cout << x << " * " << z1 << " * " << z2 << " = " << x*z1*z2 << std::endl;
      return 0;
    }
    s1.insert(x);
  }
  std::cerr << "Couldn't find triple summing up to 2020 in 1.txt" << std::endl;
  return -1;
}
```

From there we can also work out the awk for part 1 and part 2.

```awk
{ if (2020 - $0 in sofar) print $0 " * " (2020-$0) " = " $0 * (2020-$0); sofar[$0] = 1; }
```

```awk
{ ## sofar1 contains all nunmbers so far, sofar2 contains all sums of pairs of numbers so far
  if (2020-$0 in sofar2) 
    for (i in sofar1) {
      if (2020-$0-i in sofar1)
        print $0 " * " i " * " (2020-$0-i) " = " $0 * i * (2020-$0-i);
    }
  for (i in sofar1) { sofar2[$0+i] = 1; }
  sofar1[$0] = 1;
}
```
