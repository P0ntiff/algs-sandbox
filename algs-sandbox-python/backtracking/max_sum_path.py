


def max_sum_path(grid):
    # solution state 
    max_sum = float('-inf')
    # directions = [(0, 1), (1, 0)] # right and down
    R, C = len(grid), len(grid[0])
    def visit(r, c, partial_sum):
        nonlocal max_sum
        # check if end
        partial_sum += grid[r][c]
        if r == R - 1 and c == C - 1:
            # end of the grid, update max 
            max_sum = max(max_sum, partial_sum)
        if c + 1 < C:
            # something to the right 
            visit(r, c + 1, partial_sum)
        if r + 1 < R:
            # something down
            visit(r + 1, c, partial_sum)
    visit(0, 0, 0)
    return max_sum
    


grid = [[1, 5, 1],
        [2, 3, 1],
        [5, 8, 9]]

print(max_sum_path(grid))