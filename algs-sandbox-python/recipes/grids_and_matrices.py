




def is_valid(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != "1"

def valid_moves(grid, r, c):
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    moves = []
    for d in directions:
        new_r = r + d[0]
        new_c = c + d[1]
        if is_valid(grid, new_r, new_c):
            moves.append([new_r, new_c])
    return moves 



g = [["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]]

print(valid_moves(g, 3, 0))