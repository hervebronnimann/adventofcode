A clumsy first attempt:

    sort -n 1.txt > 1.sort.txt
    awk '{print 2020 - $1;}' 1.sort.txt | sort -n > 1.comp.txt
    vimdiff 1.*.txt

Then a cleaner code in c++:

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

And the one-liner: 

    awk 'NR==FNR { lines[2020-$0]=1; next } $0 in lines' "1.txt" "1.txt"
