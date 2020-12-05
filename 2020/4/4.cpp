#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <regex>

std::vector<std::string> passports;

bool loadPassports(const char* filename)
{
  std::ifstream input(filename);
  if (!input) {
    return false;
  }
  std::string line, ppt;
  while (std::getline(input, line)) {
    if (line.empty()) { passports.push_back(ppt); ppt.clear(); } else { ppt += line; ppt += " "; }
  }
  if (!ppt.empty()) passports.push_back(ppt);
  return true;
}

std::string isValid(const std::string& ppt, int check = 0)
{
  static constexpr auto npos = std::string::npos;
  auto p = npos;

  auto validDate = [&](int min, int max) {
    int n;
    if (1 != sscanf(ppt.substr(p+4).c_str(), "%d", &n)) return false;
    if (check < 0) std::cerr << "date:" << n << std::endl;
    if (n < min || n > max) return false;
    return true;
  };

  if ((p = ppt.find("byr:")) == npos) return "missing byr"; // (Birth Year)
  if (check && !validDate(1920, 2002)) return "invalid byr";

  if ((p = ppt.find("iyr:")) == npos) return "missing iyr"; // (Issue Year)
  if (check && !validDate(2010, 2020)) return "invalid iyr";

  if ((p = ppt.find("eyr:")) == npos) return "missing eyr"; // (Expiration Year)
  if (check && !validDate(2020, 2030)) return "invalid eyr";

  if ((p = ppt.find("hgt:")) == npos) return "missing hgt"; // (Height)
  auto validHeight = [&](int minIn, int maxIn, int minCm, int maxCm) {
    static std::string cm = "cm";
    static std::string in = "in";
    int n; char unit[3] = {};
    if (3 != sscanf(ppt.substr(p+4).c_str(), "%d%c%c", &n, &unit[0], &unit[1])) return false;
    if (check < 0) std::cerr << "height:" << n << " " << unit << std::endl;
    if (unit == cm) return (n >= minCm && n <= maxCm);
    if (unit == in) return (n >= minIn && n <= maxIn);
    return false;
  };
  if (check && !validHeight(59, 76, 150, 193)) return "invalid hgt";

  if ((p = ppt.find("hcl:")) == npos) return "missing hcl"; // (Hair Color)
  static const std::regex validColor("^#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f] ");
  if (check && !std::regex_match(ppt.substr(p+4, 8), validColor)) return "invalid hcl <" + ppt.substr(p+4, 8) + ">";

  if ((p = ppt.find("ecl:")) == npos) return "missing ecl"; // (Eye Color)
  auto pp = ppt.substr(p+4, 4);
  if (check && pp != "amb " && pp != "blu " && pp != "brn " && pp != "gry " && pp != "grn " && pp != "hzl " && pp != "oth ") return "invalid ecl";

  if ((p = ppt.find("pid:")) == npos) return "missing pid"; // (Passport ID)
  static const std::regex validPid("^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9] ");
  if (check && !std::regex_match(ppt.substr(p+4, 10), validPid)) return "invalid pid <" + ppt.substr(p+4, 10) + ">";

  return "";
}

int main(int argc, char **argv) {
  int check = argc > 1 ? std::atoi(argv[1]) : 0;
  auto filename = argc > 2 ? argv[2] : "passports.txt";
  if (!loadPassports(filename)) {
    std::cerr << "Couldn't open " << filename << std::endl;
    return -1;
  }
  int n = 0; std::string ret;
  for (auto& ppt : passports) {
    if ((ret = isValid(ppt, check)).empty()) ++n;
    if (check < 0 && !ret.empty()) std::cerr << ret << std::endl;
  }
  std::cout << n << std::endl;
  return -1;
}
