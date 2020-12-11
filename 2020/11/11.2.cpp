#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <regex>

constexpr int FLOOR = '.';
constexpr int OCCUPIED = '#';
constexpr int EMPTY = 'L';

typedef std::vector<std::vector<int>> Board;

bool loadBoard(const char* filename, Board& board)
{
  std::ifstream input(filename);
  if (!input) {
    return false;
  }
  std::string line, ppt;
  while (std::getline(input, line)) {
    board.push_back(std::vector<int>());
    for (char x : line) {
      board.back().push_back(x);
    }
    std::cout << "Line size " << board.back().size() << std::endl;
  }
  std::cout << "Loaded lines " << board.size() << std::endl;
  return true;
}

int count_neighbors(Board& board, int i, int j, int n, int m)
{
  int x = 0;
  for (int k : {-1,0,1})
  for (int l : {-1,0,1}) {
    if (k==0 && l == 0) continue;
    for (int p = 1; true; ++p) {
      if (i+p*k<0 || i+p*k >= n) break;
      if (j+p*l<0 || j+p*l >= m) break;
      if (board[i+p*k][j+p*l] == EMPTY) break;
      if (board[i+p*k][j+p*l] == OCCUPIED) { ++x; break; }
      // else FLOOR and then continue to ++p
    }
  }
  return x;
}

int occupied(Board& board)
{
  int x = 0;
  for (auto& row : board)
    x += std::count(row.begin(), row.end(), OCCUPIED);
  return x;
}

bool iterate(Board& board)
{
  Board board2 = board;
  const int n = board.size();
  const int m = board[0].size();
  int p = 0;
  for (int i = 0; i < n; ++i)
  for (int j = 0; j < m; ++j) {
    if (board2[i][j] == FLOOR) {++p; continue;}
    int x = count_neighbors(board2, i, j, n, m);
    if (board2[i][j] == EMPTY && x == 0) board[i][j] = OCCUPIED;
    else if (board[i][j] == OCCUPIED && x >= 5) board[i][j] = EMPTY;
    else ++p;
  } 
  std::cout << "Iterate changed " << n*m - p << std::endl;
  return p < n*m;
}

int main(int argc, char **argv) {
  Board board;
  auto filename = argc > 1 ? argv[1] : "input.txt";
  if (!loadBoard(filename, board)) {
    std::cerr << "Couldn't open " << filename << std::endl;
    return -1;
  }
  while (iterate(board)) {}
  std::cout << occupied(board) << std::endl;
  return -1;
}
