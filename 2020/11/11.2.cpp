#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

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
    for (char x : line) board.back().push_back(x);
  }
  return true;
}

int neighbors(const Board& board, int i, int j, int n, int m)
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
    }
  }
  return x;
}

int occupied(const Board& board)
{
  int x = 0;
  for (auto& row : board) x += std::count(row.begin(), row.end(), OCCUPIED);
  return x;
}

bool iterate(Board& board, int n, int m)
{
  const Board board2 = board;  // watch out, the criteria is on the original board
  int p = 0;
  for (int i = 0; i < n; ++i)
  for (int j = 0; j < m; ++j) {
    if (board2[i][j] == FLOOR) continue;
    int x = neighbors(board2, i, j, n, m);
    if (board2[i][j] == EMPTY && x == 0) { board[i][j] = OCCUPIED; ++p; }
    if (board2[i][j] == OCCUPIED && x >= 5) { board[i][j] = EMPTY; ++p; }
  } 
  return p > 0;
}

int main(int argc, char **argv) {
  Board board;
  auto filename = argc > 1 ? argv[1] : "input.txt";
  if (!loadBoard(filename, board)) {
    std::cerr << "Couldn't open " << filename << std::endl;
    return -1;
  }
  const int n = board.size();
  const int m = board[0].size();
  while (iterate(board, n, m)) {
    std::cout << occupied(board) << std::endl;
  }
  return -1;
}
