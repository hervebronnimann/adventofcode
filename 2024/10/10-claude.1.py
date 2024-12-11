def find_trailheads(grid):
    rows, cols = len(grid), len(grid[0])
    trailheads = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

def get_neighbors(pos, rows, cols):
    i, j = pos
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    neighbors = []
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols:
            neighbors.append((ni, nj))
    return neighbors

def calculate_score(grid, start):
    rows, cols = len(grid), len(grid[0])
    reachable_nines = set()

    def dfs(pos, current_height, path):
        if grid[pos[0]][pos[1]] == 9:
            reachable_nines.add(pos)
            return

        for next_pos in get_neighbors(pos, rows, cols):
            next_height = grid[next_pos[0]][next_pos[1]]
            if next_height == current_height + 1 and next_pos not in path:
                new_path = path | {next_pos}
                dfs(next_pos, next_height, new_path)

    dfs(start, 0, {start})
    return len(reachable_nines)

def solve(input_data):
    # Parse input into grid
    grid = [[int(c) for c in line.strip()] for line in input_data.split('\n')]

    # Find all trailheads
    trailheads = find_trailheads(grid)

    # Calculate score for each trailhead
    total_score = 0
    for trailhead in trailheads:
        score = calculate_score(grid, trailhead)
        total_score += score

    return total_score

test_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

result = solve(test_input)
print(result)  # Should print 36 for this example
