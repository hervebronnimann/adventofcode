#include <iostream>
#include <string>
#include <unordered_map>

enum { TOP = 0, BOTTOM = 1, LEFT = 2, RIGHT = 3, NUM_SIDES = 4 };

class Tile {
public:
  Tile(int id, const char*);
  void rotate_right();
  void flip_horiz();
  void flip_vert();
  char& operator()(int i, int j) { return char_[i * n_ + j]; }
  char operator()(int i, int j) const { return char_[i * n_ + j]; }
  std::string col(int i);
  std::string row(int i);
  std::string side(int i);
private:
  int id_;
  int n_;
  std::string char_;
};

Title tiles[] = {
 { 1237, "######..#." "...##.#..#" "....#..#.." ".#.#......" "#..##....." "#.#..#..#." "......#..#" "#.....#..." ".........." "..#.#....." }, 
 { 2113, ".##.####.#" ".##.#.#.##" "#....#...#" "........#." "##.##.#.##" "..#.#....." "#.##....#." ".##......." ".......#.#" "##..##.#.." }, 
 { 3089, "....###..#" "##...#..#." ".....#.#.." "...#.....#" ".........." "#........#" "##.##..#.#" "....###..." "#.#....#.." "#####..#.." }, 
 { 1217, "#..#...###" "#.#......." ".......###" "#........." "....#....#" "#..#....##" "#.......##" "#........#" "#.#..#..#." "##....##.#" }, 
 { 2129, ".###.##.##" "##.......#" "#....#...." "#......#.#" "#..#.#..##" "#.......#." "##....####" "..#.....##" "#........#" "...##.####" }, 
 { 1861, "##.##..#.." "...#.#...#" "#....#...." "......##.#" "...#.....#" ".........#" "##....#..." "##...#...." ".#...#.##." "#.#.###..." }, 
 { 3907, ".#.#.#...#" "........##" "##.......#" "#......#.." "#......##." "..#......#" "#.#..#...." "...#....#." ".......#.." ".#.####.##" },
 { 1549, "##.#......" "....#.#.##" "...#.....#" ".........." "..#......#" "...##....#" ".........." "#.......#." "##...#...#" ".###.##..#" },
 { 2699, "..####...#" ".##.#..###" "..#..##.##" "#.#.#...##" "#.....#..." "#.......##" "###...#..#" ".....#...." "#........#" ".#.###...." },
 { 2593, ".#....#..." "....#.#..." "....##...." "##...#...#" "...#....##" "#...#..#.#" "..##.#..#." "..####...." ".#..#..#.." "...###.##." },
 { 3209, ".#..#....#" ".....#...#" "#........." ".........." "#........." ".....#..#." "#........." "##........" "..#......." "#.#.....##" },
 { 1789, "###..#..#." "#.#..##.##" "#...##...#" "#........." "..#.#....." "..####..##" "#.#..###.." "......####" "#....####." "..##.#..##" },
 { 2111, "#.##.#.###" ".#..#....#" ".#.#..#..." "#.......#." ".......#.." "#......#.#" "#........." ".....#...#" "##.....#.." "..##.#..##" },
 { 3137, ".####..##." "##.##....#" "#....#...." "#........." "..#...#.#." "#.#..##.#." "..#...#..#" "..#..#.#.#" ".......###" "#.##...###" },
 { 1871, "#.####...." "#....#...." "......#..#" "#.......##" "##.#....##" "..#..#...." "#..#...#.." "#.#...#.##" "#.##.....#" ".##.....##" },
 { 3119, "######.##." "..#..##..#" ".......##." "#...#.#..#" "..#...#..." "#..#....#." "#....#...." "#......#.#" "#........." "......#.##" },
 { 1579, ".#.#.#...." "#..#.....#" "###.....#." "..#.#....#" "####......" "#.#......#" ".......#.." "...#.....#" ".#####...#" "#..#....##" },
 { 1249, "#...####.." "#........." "...#.....#" "#......#.#" "....##...." "#..#..##.#" "#..#.....#" "....#.#..." "#.#....#.." ".##...#.#." },
 { 1319, "....#.####" "#.#..#.#.#" "#......#.." "..#.#.#..#" "..#....#.#" "##....#.#." "###...#..." "###......#" "..#..#..##" "..#.#..##." },
 { 1987, ".#...####." "...#...###" "...##...##" "..#..#..#." "##.....#.." "#..#....##" ".#.....#.#" "#......#.." "##......#." "..###...#." },
 { 2963, ".##.#####." "#.##...##." "#..##....." "..#......#" "..##.....#" ".#..#..#.#" ".........." "#...#..##." "...#......" "##..#####." },
 { 1609, "..##..###." ".....#..#." ".....#...." "##....#..." "###..#...#" "##....#..#" "......##.." "..#..###.." "#....#.#.." "...##....#" },
 { 2267, "...#.#..#." "..##....##" "####..#.##" "....#.##.#" "##..#....." "..##.#...." "#.##...###" "#..##.###." ".........." "..#..##..." },
 { 1531, "#.#..##..#" "#........#" "#.....####" "....#...##" "#.....##.#" "#........." "......##.#" ".#.#..#..#" ".........#" "#..#.#.#.#" },
 { 2357, ".......#.." "...#..#..." ".......#.." ".#...#.###" "#.####...#" ".#.#.....#" "#.#.....#." ".###..##.#" "#.#.#...#." "##.#.#####" },
 { 1373, ".#.....###" "..#...##.." "..#......#" "...#...#.#" ".#..#.#..#" "......#..." "#...##..#." "#...#..##." "...#......" "##.#.#...#" },
 { 3373, "...##.#.##" "#........." "....#....#" "#..###...#" "#...#...##" "......#.##" "........#." ".......##." "#..#...#.." ".##..#.#.." },
 { 1831, "...#####.#" "#........#" "#.....#..#" "#.#...###." "...#.##..#" "..##.....#" "..#....#.." "......##.#" "##...#...." "##.###.#.#" },
 { 3607, "#...#.#..." ".#...##.##" ".#.......#" "..####...." "####....#." ".#.#...#.#" "###...##.." "#......#.." "###.#..#.#" "##.##..###" },
 { 3251, "##.#..##.." ".#....##.#" "#.......#." "..#..#..#." "#..##....#" "#...##..##" ".....#..##" "...#...##." "....##...." "#####...##" },
 { 3917, ".##......." ".#..#...#." "....##...#" "#.#..##.##" ".#.#...#.." "..#......." ".....#..#." ".#..#.#..#" "...##..#.#" "##..#...##" },
 { 1489, ".##..##.#." "##...#.#.#" "#.......#." "##.#.....#" ".#...##..#" "..#......." ".#..#....#" "###..#..##" "#..##....." "#######..." },
 { 3253, "#..#..####" "....#..#.." "#.##..#..." ".##....###" "........##" ".........." "#...#....." "##...#...#" "...##....." ".##..##.#." },
 { 2081, ".......##." "#...#....#" "#..#....##" "##....##.." "#.#.###..." ".....#...." "#...###.##" "##..##...." "#........#" ".#...#..#." },
 { 1481, "######..#." "###.#....#" ".....#...#" "#........." "#..#....##" "#........#" ".........." "#...#....#" "#..#.##..." "#####..##." },
 { 2953, "..##.#####" "#.#..#..##" "..#....#.#" "#...#.#..." "#..##....#" "#.#....#.#" ".......#.#" "#..##....." "#.#.....##" "...##..#.#" },
 { 1783, ".#..#.#.##" "#...#....#" "...#......" "#.#.#..#.#" ".........#" "......#..." ".#...#..##" "..#...#.#." "#..#..#..#" "...#..#.##" },
 { 2269, "#.#.##..#." "#.....##.." ".#.......#" "..#..#...#" "....#....." ".........." "##.##....#" ".....#...." "##.....###" ".#.#####.#" },
 { 1277, "..##..#..." "#...#....." ".......#.." "...#......" "....#....#" "..#......." "#......#.." ".#........" "#........." "###.###..." },
 { 2633, "####.#.#.." "......#.#." "........#." "#........." "...#...###" "...#.....#" ".##.#..#.#" ".#........" "#.#......#" ".##.##.#.#" },
 { 3919, "###..###.." "...#......" "...##.#..#" "#...#..#.#" ".........#" "...#.#.#.." "...#.#...." "#....#...#" ".#.###..##" ".#.#.##..." },
 { 1753, "#...##...." "#.....#..." ".........." ".#..#....." "#.......##" "..#......." "......#..#" "#..####..." "....#..#.#" "..#.####.." },
 { 3739, ".##.#.#..#" "###.##.##." "##.###.#.." ".#....#..#" "#...##...." "#..#......" "#....###.#" "..#......." "###....#.#" "...###..#." },
 { 3701, ".####..#.#" "#.....#..." ".#........" ".........#" "...#.#...." "#.#......." "#...#....#" ".###.#.##." "#.#......." "##.##..##." },
 { 3631, "#..#..###." ".........#" "#...##...." ".......#.#" ".....#...." "...#..#..#" "........#." "..#....#.#" "......#..." "##.#..#.#." },
 { 2389, "..#.##...#" "###......." "#..##...##" "#.######.." "..#..##..." ".#...#...#" ".....#...#" "#..#....#." "..#...##.." "#...#..##." },
 { 1123, ".##.#.###." "#........#" "#........." "#.....##.#" "....#....." "....##.#.#" "....#....#" "#.#.#..#.#" "#..#.....#" "#.#..#..#." },
 { 2659, "#.##.#.##." ".#........" "#....#..##" "###..##.##" "#.#.###..#" "#...##...#" "...#...#.." "...#..#..." "..#.#.#..#" "####...#.." },
 { 3709, ".##...#.##" "..#..##..#" "......#.##" "......#..#" "....#....." ".........." "#......#.#" "#....##..#" ".....##..#" "####.##..." },
 { 2887, "######..##" "#........." ".......#.#" "...#.#...." "#....##..." "#...#....#" "...#.#...#" "#....#...#" "##....#..#" "#########." },
 { 1367, "#.####.###" "#......#.#" ".........." "#....#...." ".#......#." "#........." "...#.#.#.." "......#..." "##....#..." ".....##.##" },
 { 2221, "##..#....." "#.....#..." ".........#" "#..#......" "#.#...#..." "###......#" "...#.....#" "#........#" "#.....#..." "..##.###.." },
 { 2621, "##..#.###." ".......###" ".........#" "..#.#...#." ".........." "....#....." "#.##..##.." "......#..#" "....#...#." "##.#.....#" },
 { 2503, "..#.##.##." "......#..." "#.#..#...." "....#....#" "#.....#..." "..#......#" "##...#..#." "#....#..#." "...#......" "#....####." },
 { 3491, "#..#.###.." "#........." "#..#..#..#" "###....###" "#.#.##...." "#........#" "......#..." "##...#...#" "##........" ".#.#.##.##" },
 { 2333, "..##.....#" ".....#..#." "#.#.#..#.#" "##.##...#." "..#.#....." "...#.....#" "..###..#.." "###.....##" "#........#" "##.####.#." },
 { 2399, ".....#.##." "##.....#.#" "##.......#" ".#.#..##.#" "#...##...#" "###.#....#" "#......#.." "##......#." "#.#....#.." ".....#.#.." },
 { 2683, "#.##..##.." ".#....#..#" ".........#" ".......#.#" ".##.#..##." ".....##..#" "#....##..#" "....##.#.#" "...###.###" ".#.##.#.##" },
 { 1741, ".##..#.#.#" ".##....#.." "##..#....." "##...###.." "......#..#" "#.....#..." ".......#.." "#.....#..." "...##..#.#" "#..###.##." },
 { 3539, ".###....##" ".........." ".##.#...#." ".....#...#" ".........#" ".........#" ".......#.." "..#.....#." ".#.#.###.#" "#.#.####.#" },
 { 3929, "##..######" ".#..##.###" "#.##....#." "...##..#.#" "#...#....." "........#." ".....#...#" "#...#.#..#" ".#.#.....#" "..##.#..#." },
 { 3221, "..####..#." "##......#." "..#..#.###" "##........" "....#....#" ".#...#...#" "#.#...#..#" "##....#..#" "##......#." ".#..#..##." },
 { 1117, ".##.##.#.#" "##.....###" "#.#.#.##.." "..#....#.." "##....#..." "...#..##.#" "..#.#.#..#" "...#...#.#" "....##...#" ".###.#..##" },
 { 3163, ".####.#.#." "#........." ".........." "......#..#" "....##.#.." ".#....#..#" ".....####." "#....#.#.." "...#.#..##" "##.#.#...." },
 { 1129, ".....##..." "##......##" "#..#..#..#" "..#....#.." "#.#...#..." "....#.##.." "...#...#.." "#........." "#..#..#.#." "#.#..###.#" },
 { 3079, "###..#.##." "....###..." "##..#....#" "....##...#" "......##.." "....#....#" "#.#.#....." "#...#....#" ".#........" ".##.#.###." },
 { 2039, ".#.#.##..#" "..##......" ".##......." "#........." "....#...##" "#..#.#...#" ".........." "#.....#..#" "####..#..#" ".#..#..##." },
 { 1901, "####.#.##." "#.#...##.." "...#....##" ".........." "#........." "#...##...#" ".........." "##......##" ".#.....#.." ".###.##..." },
 { 2029, "####..##.." "##...#...." ".#....##.#" "..#....##." "#........#" ".........." ".........." "#..#..#..." "#..#....##" "....####.." },
 { 1879, "##..#.##.#" "#...#...##" ".##...#.##" ".#.#.....#" ".##.#..#.#" "#..##....." "#..##...#." "......#.##" "...#..#..#" "#....#..#." },
 { 3347, "###..#..##" ".#..#....#" ".#...#...#" "....#....#" ".#......##" "......##.#" ".....#..##" ".........#" "#......#.." ".####.#..#" },
 { 2417, "####.#..##" "...#.#...." ".#....#..#" ".#........" "#........." ".....#...." "#..##....." "#..#...#.#" "#..#.##..#" "..##..####" },
 { 2897, "...#..#.##" "#.#......." ".........#" "#.#.#..#.." "..#......." ".........#" ".##...#..#" "....#..###" ".###...##." ".#.#.#.#.." },
 { 2837, ".#....###." ".......#.." "......#..#" "#..#..#.##" "#.#.##...#" "#...#....#" "...##.#.#." "#.....#..#" "#.#.....#." "#####.####" },
 { 3001, "##....#..#" "#....#.#.." ".....##..#" ".....##..#" "...#......" "#.....#..#" "#.#...##.#" ".#...#...#" "........#." "###.####.#" },
 { 2153, ".####.##.." "#..#.....#" "..#....#.." "#......#.#" ".........#" ".###.....#" "#.##.....#" "#..#......" "#.#......." ".######..#" },
 { 2749, "..##.###.." "#..#...#.." "..##.....#" "###......." "#..##....." "......#..#" "..#..##..." ".###.....#" "#.#......." "...#..#..#" },
 { 2791, "..##.##.#." ".##.###.#." ".#..#....#" ".##..#.#.#" "#..#....#." "......##.." "#.##.#.#.#" "##...#.##." ".#...#.#.." "...#.#...#" },
 { 2707, "..###...##" ".#....#..." "..#...##.." "#.#......." "....#....#" "#.....#..." ".........#" "##.....###" "#........#" "#.##.#####" },
 { 2969, "..#####..#" ".........." "#.....#..#" "....#.#..#" "...#......" "..##.#...#" "...#.#...." "...#.....#" "..#......." "####..##.#" },
 { 3329, "#.###..#.." "...#....#." "........#." ".........#" "###.#..#.#" ".#.......#" ".........#" ".......#.." "#....##..#" "##.###.#.." },
 { 3989, ".#####.###" "#....#.#.." ".........#" ".........#" "##.#...#.#" "......#..#" "...#.....#" "###......#" ".#.......#" ".###.##.#." },
 { 3583, "..#..#.#.." ".#........" "###...##.." "##.....#.." "##.......#" "#........." "#........." "#...#..#.#" "##.#......" "#........." },
 { 3931, "....#..#.." "#.#.#....." "..#..#..#." ".##...##.#" ".......#.#" ".........#" "....#...##" "......#..#" "#.#....#.." "#.#.#.##.#" },
 { 1493, "####..##.#" ".........." "....#..#.." "##...####." "#........." "#........." ".#.#.....#" "....##...#" "......##.." ".#########" },
 { 1013, "#.###....#" "....####.#" "...#.####." ".......##." ".#..#....#" "#........." "#......#.." "...#...#.." "#.....#..." "#.#.#####." },
 { 2089, ".#...#.##." "..#...#..#" "........#." "...#.#..#." ".....##..#" "#...###..." "#....#.#.." "#....#..#." "#...###..#" "........##" },
 { 1613, "#.#...####" "#.....#..." "#....##..#" "#....#...." ".#....#..." "#........#" "......#.#." "#.....#..." "##...#...#" "....#..##." },
 { 3331, ".#.#.#####" ".....#...#" ".......#.." "##..#...#." "#........#" "......#..#" "..#.#....#" ".......#.." "..#......." "###.###..#" },
 { 3217, "..#.###..." "#.##......" "..#...##.." "...#.##..#" "###...###." "#...#.#.#." "##.#...#.." ".........#" ".....##..." "##.###...." },
 { 3011, "#.##.#...." "....#...##" ".........." "#........#" "#....#...#" "#..#......" ".........." ".........#" "....##...." "##.####..." },
 { 1171, "###..###.#" "..#.....##" "##.#...#.." ".#.......#" ".........." "##.....##." ".##.....##" "..#...####" "##.##..#.#" "#.#.#.#..." },
 { 1933, "#####..#.." "#.#.#.#..." "#.#......." "#.#.#....." ".....#...#" "#.#......." ".........." "...#..#..." ".##....#.." "......#..." },
 { 2141, "#.###...#." "#.....#..." ".........#" ".....#..#." "#.###....." "#..###.#.." ".....#..#." "....#....#" ".#.......#" "...##..##." },
 { 1031, "###...#..#" "#.......#." "##.#..#..#" "##..#....." "#...#....." "##....#..." "#......##." "#........." "......#..#" "....#..##." },
 { 2857, "#.#..#...#" "#........#" "##.#..#.##" "....#.##.." "....#...##" "#...#....." "#..#......" ".......###" "#...####.#" ".#...####." },
 { 3313, ".#......##" "...##....." ".#.##....." "#.#.#....." "#.#..#...." "..#......." "#..#.#...#" "#.#......#" "##...#...." "..###.##.#" },
 { 1303, "#.##.#...." "#.......##" "...#...##." "....##...#" ".....#...#" ".........#" "#..#...#.#" "##...##..." "...#.#.#.." "....##..##" },
 { 3457, "#...#.#..#" ".........#" "#.#..#...#" ".....#.#.." "........##" "...#......" "..##.##..." ".........." "....#....#" "#...#..#.#" },
 { 3643, "##.##..###" "..#.#....#" "..##.....#" "..#......." "#........." "#........." "#.......#." "......#..#" ".#......#." ".###..##.#" },
 { 2803, "#...#..##." "##....#.##" ".#.......#" "#...###..." "#...###..#" "#..#......" ".......#.#" "#.......#." "...##....." "..#..##.##" },
 { 2549, ".#....####" ".#........" ".....###.." ".....#..##" "..#.###..." "......#..." ".........#" ".......##." "#......#.#" "..###.####" },
 { 3571, "#..#.##..." "...#....#." "..##..##.." "....#.##.#" ".#.....#.." ".##...#..." ".##......#" "#.#......#" "......#..." ".#..#..#.." },
 { 1327, "#..###...#" "#....#...#" "#.##...#.#" "#.......#." "#.#...#..#" ".........#" "##........" "....#..#.." ".....#..#." ".#.###..##" },
 { 2833, "##...#..#." "##....#..#" "##.#.....#" ".......#.." "###...#..#" ".........#" "#.#....###" "....##.#.." "..#...#..." "..#.#.#.##" },
 { 1997, "##..#...##" "#...#....." "#.....#..." ".......#.." ".......#.#" "#........." "#......#.." ".........#" "..#.#.#..#" ".###.##..#" },
 { 3673, "..#..###.." ".#..##...." "#.##.....#" ".####..###" "##..#..#.." "#.#.#...##" ".#....#.#." "....#.##.." "#...#....#" "..#.##...." },
 { 3323, ".#...#####" "#..#...#.#" ".........." "#....#...#" ".#........" "#........#" "##......##" "...##...#." "...#.#..##" "#.##.###.#" },
 { 1619, "#..###.###" "#...##...#" ".#........" "#.#.....#." "#.##.....#" "#......#.." ".......#.." "#####.#..#" ".........." "####...#.." },
 { 2477, ".##.##..#." "#.#.#....." "......#..#" "......#.#." "##.##....." ".###.#..#." ".........#" "...#.#...." "#.....#..." "...##.#..." },
 { 3389, "#...#.#.##" "##.#.....#" "......#..#" "#..#.#...#" "#....#..#." "##......##" "....#...##" "#.##..##.." "#........#" "...##.#.##" },
 { 1193, ".##...###." "#...##..#." "###......." "#.#..#...." ".#..#.#..." "#..##....#" "#.#..##..." "####.....#" "#...#..#.." "..##.....#" },
 { 3767, "#...#....." "...#.#..#." "#######..." "...#.#...." "#........." ".#....##.." "#.#......." ".#.#.#..#." "..#.###..#" "....##.#.." },
 { 3191, "#.##...#.." ".........." "......####" "#..#..#..." "....#.#.##" "......#.#." ".....#...." ".#....##.#" "..#..#.#.#" "#...##.#.#" },
 { 3049, "#...#...#." ".#..#....#" "##.#.....#" "...#...##." "#.##.....#" ".....#.#.." "..##..##.." ".........." "#....#.#.#" "#.##.#..#." },
 { 1747, "###....#.." "....#..#.#" ".......#.." "........#." "#..#......" ".......###" "...#.##..." ".....#..##" ".#....#..." ".##..####." },
 { 1429, "...#.#.#.." ".#...#...." ".........." "##........" "#........." "#..#.#...." ".##......." ".#........" ".##.#.#..#" "#####.##.#" },
 { 2909, "#.##.###.." "#..#.....#" "#...#....." ".#..#.##.." "#.#.....#." "#...#...##" "...#...#.." ".##.....##" "##..#..#.#" "#.###..###" },
 { 1973, "#####.#.#." "...#.....#" "#........." "#........#" ".....###.." ".........." ".#.....#.#" ".##..#.##." "##.#..#..." "#.##...#.#" },
 { 3449, ".#.#.#..#." "#...#.#..." "..#.##...." "#...###..." ".....#...#" "#.......#." "##....#.##" "......#..#" "#.......#." "..####...." },
 { 3371, "##.#..#.#." "#...##...#" "##...##..." ".#....#..." "#...##...#" "..#......#" "......#..#" "##.###...#" "#....#...#" ".##....#.." },
 { 1103, "####..#..#" ".......#.." "#......#.#" ".........." ".#....##.." ".#.##...##" "##....##.#" "..#..#.###" ".........." ".#.#...#.#" },
 { 1723, ".#....###." "...#.#...#" "..#.#....." "#####....#" ".#.#......" "....#..#.." "..#......." "..##...#.#" "....###..." "...##.#.#." },
 { 1093, "..##.#.###" ".##......." "#....#...." ".#.....#.." "#.......##" ".........#" ".#......##" "#......#.#" "#..#.#...#" "#.#####.#." },
 { 1321, "#.#.###.#." ".#..##..#." "#.###..#.." "#..##....#" "#.......#." "....#....#" "#....#...#" ".....#...." "#.###....." ".###...##." },
 { 1979, "#####.###." "#.#..#..#." "#.####...." "###.....##" "....#....." "#........." "###.#..#.#" "..##...###" "#.......##" "..#......." },
 { 2677, "##..#.##.#" "#.##.....#" "#..#...#.#" "..#.#.#..#" "##.#..#..#" ".....#..#." "#...#...##" "...#...###" "##.#...#.." ".###..##.." },
 { 1553, ".#...###.." ".........#" "###......." "##..#...#." "..#...##.#" "..##......" ".##......." "...#..#..." "#....##..." "#####.#..." },
 { 3187, "###..#..#." "#.....#..." ".....#..##" "#.....#..#" "..#......#" "##...#...." "......##.#" "......#..." "#.#..#...." "########.#" },
 { 2243, "##.####..." "..#.#.#..#" "#..#......" ".........#" "....#...##" "#........." "#......#.#" "....#....#" "......#.##" "##.#....#." },
 { 1423, "..#..##..#" "..#....#.#" "#.#.....##" "##.......#" ".#..#..#.." "......##.." "##...##..." ".....##..#" "...#.#.#.#" "##...###.." },
 { 3319, "##.##.#.#." "#.......#." "....#....." "###....###" "........#." "###......." ".#.....##." "#...#....#" "..#......." ".##...####" },
 { 3343, ".#...#####" ".........." ".###...#.#" ".##......." ".........." "##....####" "#......#.#" "#.#.###..#" "..#......." ".#####..#." },
 { 2789, "##....####" ".##......." "#......#.#" ".#.##....." "#......#.#" "#........#" "##......#." ".#...##..." "#.....##.#" "...###.#.." },
 { 3623, "##..#..#.#" "#.....#.#." "##.....#.#" ".#...##..#" ".#.......#" "..#...#..#" ".#..#..##." "###..#.###" ".#.##.#..#" ".#.##.#.#." },
 { 1439, ".#..#.#.#." "....#....." ".........#" "#..#......" "##..#....#" "#.#.#.##.." "##.#.#...#" "#........." "#.......#." "####...#.#" },
 { 1361, "#.#...###." "#........." "....#....." "..#......." "......#..#" "##....##.#" ".##..#..##" "..#......#" ".....##..#" "#..#....#." },
 { 1823, ".##.#.#..." "#........." "#..#.##.#." "#...##...." "##........" "#...#.#.##" "#........#" ".........#" "........#." "#.###...#." },
 { 2971, ".#.......#" "#.#....#.." "#..#.#...." "...#..#..." "##....#..." "#..#......" ".........#" "....##...." "#...###..#" "#...#.#.#." },
 { 3229, "..###.####" "#........#" ".#.......#" ".........." "##.......#" "#..#......" ".#.#......" "#.....##.#" ".#......#." ".#####.#.#" },
 { 1907, "####.#.#.." "....#....#" "#....#...." "#........." "#...#..###" "...#.#.#.#" "....##...." "#.###..###" "..#..##.##" "..##.##..." }, 
 { 1699, "..#..##..." ".#..#.#..." ".....#...#" ".#.#.#...#" "........#." "##.....#.." "#.#......#" ".##......#" "....###.#." "...##..###" }, 
 { 2131, "#..#####.." "#....#...#" "#..####..#" "......#..#" "#.#..#...#" "#.#...#..#" "..##......" "#.#####..#" "......#..#" "#...####.#" }, 
 { 1657, "..#..##.#." "#....##..." "##..#....#" "#........#" "#........." "#.......##" "#......###" "#.#.#...##" "........##" "#.##.#.##." }
};
