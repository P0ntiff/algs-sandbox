'''

We are designing an escape room game and we have a 2D map representing the room using an integer matrix. Each cell can be either a wall (denoted by a 1) or an empty space (0).

escape_room = [
  [0, 0, 0, 1, 1],
  [0, 0, 1, 0, 0],
  [0, 1, 0, 1, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
]

The player in our escape room can move 1 space at a time – up, down, left, or right. The player can't land on a wall or go through walls or move through the edges of the escape room.

Write a function which takes the escape_room and a starting_position (a row-column pair). This function should return all of the next immediately available positions that the player can move.

Example 1:
Input: findLegalMoves(escape_room, (1, 1))
Output: (0, 1), (1, 0)

Example 2: 
Input: findLegalMoves(escape_room, (5, 3))
Output: (5, 2), (5, 4), (4, 3), (6, 3)

Example 3: 
Input: findLegalMoves(escape_room, (5, 1))
Output:  (6, 1), (4, 1), (5, 0), (5, 2)

Example 4: 
Input: findLegalMoves(escape_room, (6, 0))
Output: (5, 0), (6, 1)

Example 5: 
Input: findLegalMoves(escape_room, (6, 4))
Output: (5, 4), (6, 3)

Example 6: 
Input: findLegalMoves(escape_room, (0, 0))
Output: (0, 1), (1, 0)

Example 7: 
Input: findLegalMoves(escape_room, (2, 2))
Output: [ ] # no moves possible

'''

""" Check each direction for valid or not and output
Time: O(1) since the directions is a constant size array, and we don't need to look at every coordinate in the grid
Space: O(1) since we are only storing at most 4 possible moves out of 4 directions
"""



# def findLegalMoves(escape_room, coordinates):
#     r, c = coordinates
#     def is_valid(r, c):
#         return 0 <= r < len(escape_room) and 0 <= c < len(escape_room[0]) and escape_room[r][c] != 1
    
#     output = []
#     for d in directions:
#         new_r = r + d[0]
#         new_c = c + d[1]
#         if is_valid(new_r, new_c):
#             output.append((new_r, new_c))
#     return output

# escape_room = [
#   [0, 0, 0, 1, 1],
#   [0, 0, 1, 0, 0],
#   [0, 1, 0, 1, 0],
#   [0, 0, 1, 0, 0],
#   [0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0],
# ]

# print(findLegalMoves(escape_room, (1, 1)))

'''

Given an escape room and the exit, determine if it is possible for a player to always get out of the room regardless of where their starting point is. 

Note that you're *not* actually given the starting point of the player, instead you have to assume the player could start anywhere. 

It is up to you to determine if it is possible to travel from *every* open cell in the room to the exit regardless of where the player starts.

escape_room_1 = [
    [ 0, 0, 0, 0, 1 ],
    [ 0, 1, 1, 0, 0 ],
    [ 0, 0, 0, 0, 0 ],
    [ 0, 1, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0 ],
]

escape_room_2 = [
    [ 0, 0, 0, 0, 1 ],
    [ 0, 1, 1, 0, 0 ],
    [ 0, 0, 0, 0, 0 ],
    [ 1, 1, 0, 0, 0 ],
    [ 0, 1, 0, 0, 0 ],
    [ 0, 1, 0, 0, 0 ],
]

escape_room_3 = [
    [ 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 1, 1, 1, 1, 1, 0 ],
    [ 0, 1, 0, 0, 0, 1, 0 ],
    [ 0, 1, 0, 0, 0, 1, 0 ],
    [ 0, 1, 0, 0, 0, 1, 0 ],
    [ 0, 1, 1, 1, 1, 1, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0 ],
]

escape_room_4 = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]

escape_room_5 = [
    [0],
]

exit_1 = (0, 0)
exit_2 = (5, 0)

# Expected output:

isPossibleToEscape(escape_room_1, exit_1) # -> True
isPossibleToEscape(escape_room_1, exit_2) # -> True
isPossibleToEscape(escape_room_2, exit_1) # -> False
isPossibleToEscape(escape_room_2, exit_2) # -> False
isPossibleToEscape(escape_room_3, exit_1) # -> False
isPossibleToEscape(escape_room_4, exit_1) # -> True
isPossibleToEscape(escape_room_5, exit_1) # -> True
'''
from collections import deque

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def isPossibleToEscape(escape_room, exit):
    # BFS approach: From the exit, try and "paint" every open cell (in-place mark) . If after the first iteration we have any open cells left, we can return False because if should have been reached on the first search.
    # Time: O(m*n) because we should only have to do one BFS which can visit at most m *n cells. There is a second pass needed in the same time complexity. 
    # Space: O(m*n) in the worst case of the maximum queue size, if every node is marked as we are marking in place
    exit_r, exit_c = exit
    def is_valid(r, c):
        return 0 <= r < len(escape_room) and 0 <= c < len(escape_room[0]) and escape_room[r][c] != 1 and escape_room[r][c] != -1
    def bfs():
        q = deque()
        q.append((exit_r, exit_c))
        # edge case to check, if the exit is a wall
        if escape_room[exit_r][exit_c] == 1:
            return False
        while len(q) > 0:
            r, c = q.pop()
            escape_room[r][c] = -1 # mark as visited
            for d in directions:
                new_r = r + d[0]
                new_c = c + d[1]
                if is_valid(new_r, new_c): # is an open neighbour, add to queue
                    q.appendleft((new_r, new_c))
    bfs()
    for r in range(len(escape_room)):
        for c in range(len(escape_room[0])):
            if escape_room[r][c] == 0:
                return False # missed one on the search
    return True


# escape_room_1 = [
#     [ 0, 0, 0, 0, 1 ],
#     [ 0, 1, 1, 0, 0 ],
#     [ 0, 0, 0, 0, 0 ],
#     [ 0, 1, 0, 0, 0 ],
#     [ 0, 0, 0, 0, 0 ],
#     [ 0, 0, 0, 0, 0 ],
# ]

# exit_2 = (5, 0)

# escape_room_2 = [
#     [ 0, 0, 0, 0, 1 ],
#     [ 0, 1, 1, 0, 0 ],
#     [ 0, 0, 0, 0, 0 ],
#     [ 1, 1, 0, 0, 0 ],
#     [ 0, 1, 0, 0, 0 ],
#     [ 0, 1, 0, 0, 0 ],
# ]

# escape_room_3 = [
#     [ 0, 0, 0, 0, 0, 0, 0 ],
#     [ 0, 1, 1, 1, 1, 1, 0 ],
#     [ 0, 1, 0, 0, 0, 1, 0 ],
#     [ 0, 1, 0, 0, 0, 1, 0 ],
#     [ 0, 1, 0, 0, 0, 1, 0 ],
#     [ 0, 1, 1, 1, 1, 1, 0 ],
#     [ 0, 0, 0, 0, 0, 0, 0 ],
# ]

# escape_room_4 = [
#     [0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 0],
#     [0, 1, 1, 1, 0],
#     [0, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0],
# ]

# escape_room_5 = [
#     [0],
# ]

# exit_1 = (0, 0)

# print(isPossibleToEscape(escape_room_1, exit_1)) # -> True
# print(isPossibleToEscape(escape_room_1, exit_2)) # -> True
# print(isPossibleToEscape(escape_room_2, exit_1)) # -> False
# print(isPossibleToEscape(escape_room_2, exit_2)) # -> False
# print(isPossibleToEscape(escape_room_3, exit_1)) # -> False
# print(isPossibleToEscape(escape_room_4, exit_1)) # -> True
# print(isPossibleToEscape(escape_room_5, exit_1)) # -> True


"""
Ideas: Shortest path (Dijkstra's algorithm). This won't work because it's greedy, and I need to ensure every route with clues is fully checked.

Backtracking, can check every possible path and check if every clue was collected. Only real solution because the problem is NP-complete, i.e. TSP.  You can't do better than exponential. 

Decision tree:
From starting point, try each available direction. Track the current path we're on so we don't double back on ourselves.

At a leaf node when we can't go any further in a direction. Backtrack and try another direction.

Track as we go the current path we're on, in a set for O(1) lookup

When at a leaf node, check if we've reached the exit and collected all keys
 - Update the shortest path if this is shorter than the shortest known path


"""

def shortest_path(escape_room, starting_point, exit_point):
    def is_valid(r, c, curr_path):
        in_bounds = 0 <= r < len(escape_room) and 0 <= c < len(escape_room[0])
        return in_bounds and escape_room[r][c] != 1 and (r, c) not in curr_path 

    start_r, start_c = starting_point 
    exit_r, exit_c = exit_point
    # count clues
    max_clues = 0
    for i in range(len(escape_room)):
        for j in range(len(escape_room[0])):
            if escape_room[i][j] == 2:
                max_clues += 1
    # global answer
    shortest_route_size = float('inf')
    shortest_route = []
    def search(curr_path, r, c, path_size, clues_collected):
        nonlocal shortest_route_size, shortest_route
        # check for leaf node  + answer 
        choices_available = [(r + d[0], c + d[1]) for d in directions if is_valid(r + d[0], c + d[1], curr_path)]
        print(f"currPath {curr_path}: {choices_available} choices for r {r} c {c}")
        at_exit = (r == exit_r and c == exit_c)
        if not choices_available or at_exit:
            if at_exit: 
                # check if answer 
                if path_size < shortest_route_size and clues_collected == max_clues:
                    shortest_route = curr_path.copy()
                    shortest_route_size = path_size 
                print("answer!")
            return
        # include in path
        clues_collected += 1 if escape_room[r][c] == 2 else 0
        for new_r, new_c in choices_available:
            # for each choice available, search
            curr_path.append((new_r, new_c))
            search(curr_path, new_r, new_c, path_size + 1, clues_collected)
            # backtrack after search 
            curr_path.pop()

        return False 

    search([(start_r, start_c)], start_r, start_c, 0, 0)
    return shortest_route


# three things missed in the answer: 

# 1. Accidentally was skipping a key grid type in the "is valid" condition
# 2. 
# 3. Exit if condition was not correctly nested in the leaf return
#   All leafs should exit, only some should update the answer

escape_room_1 = [
    [ 0, 1, 2 ],
    [ 1, 1, 2 ],
    [ 0, 0, 0 ],
]

escape_room_2 = [
    [ 2, 0, 0, 0, 0 ],
    [ 0, 1, 1, 0, 0 ],
    [ 0, 1, 0, 2, 0 ],
    [ 1, 0, 0, 0, 0 ],
    [ 0, 2, 1, 0, 0 ],
    [ 0, 0, 0, 0, 0 ],
]

escape_room_3 = [
    [ 0, 2, 1 ],
    [ 0, 0, 0 ],
    [ 0, 0, 0 ],
]
# print(shortest_path(escape_room_1, (0, 0), (2, 2)))
# valid path: None

# print(shortest_path(escape_room_2, (5, 2), (2, 0)))
# valid path: [(5, 2), (5, 1), (4, 1), (3, 1), (3, 2), (2, 2), (2, 3), (1, 3), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0)]


print(shortest_path(escape_room_3, (2, 1), (1, 2)))
# valid path:  [(2, 1), (2, 0), (1, 0), (0, 0), (0, 1), (1, 1), (1, 2)]
'''

Great! We now have an escape room that can be escaped from and a way to traverse it effectively. Your final task is the most challenging.

In every escape room, there are open spaces (0) and walls (1) but now there also will be clues (2). An escape room cannot be properly escaped from until a player has first found *all* of the clues.

Given an escape room, a starting point, and an exit, write a function to return the shortest simple path of open spaces from the start to the exit, if such a path even exists. If multiple paths exist return any of the valid paths.

*Important*
- A simple path is one that does not revist any location (i.e. you can't step on the same cell twice!)
- A path is not considered valid unless you collect all of the clues
- While returning any path is a start towards solving the problem, we are looking for the *shortest* path that collects all the clues and does not revist any locations.

escape_room_1 = [
    [ 0, 1, 2 ],
    [ 1, 1, 2 ],
    [ 0, 0, 0 ],
]

escape_room_2 = [
    [ 2, 0, 0, 0, 0 ],
    [ 0, 1, 1, 0, 0 ],
    [ 0, 1, 0, 2, 0 ],
    [ 1, 0, 0, 0, 0 ],
    [ 0, 2, 1, 0, 0 ],
    [ 0, 0, 0, 0, 0 ],
]

escape_room_3 = [
    [ 0, 2, 1 ],
    [ 0, 0, 0 ],
    [ 0, 0, 0 ],
]

shortest_path(escape_room_1, (0, 0), (2, 2))
# valid path: None

shortest_path(escape_room_2, (5, 2), (2, 0))
# valid path: [(5, 2), (5, 1), (4, 1), (3, 1), (3, 2), (2, 2), (2, 3), (1, 3), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0)]

# Or

# valid path: [(5, 2), (5, 1), (4, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0)]

shortest_path(escape_room_2, (0, 0), (4, 1))
# valid path: [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (3, 2), (3, 1), (4, 1)]

# Or

# valid path: [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1)]
  
shortest_path(escape_room_2, (5, 0), (0, 4))
# valid path: None

shortest_path(escape_room_3, (2, 1), (1, 2))
# valid path:  [(2, 1), (2, 0), (1, 0), (0, 0), (0, 1), (1, 1), (1, 2)]

'''
