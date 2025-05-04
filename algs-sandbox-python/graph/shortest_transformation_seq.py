"""Given two words, start and end, and a dictionary containing an array of words, return the length of the shortest transformation sequence to transform start to end. A transformation sequence is a series of words in which:

Each word differs from the preceding word by exactly one letter.
Each word in the sequence exists in the dictionary.
If no such transformation sequence exists, return 0.

Example:
Input: start = 'red', end = 'hit',
       dictionary = [
            'red', 'bed', 'hat', 'rod', 'rad', 'rat', 'hit', 'bad', 'bat'
       ]
Output: 5
Constraints:
All words are the same length.
All words contain only lowercase English letters.
The dictionary contains no duplicate words.
"""
from typing import List

from collections import deque, defaultdict

def shortest_transformation_sequence(start: str, end: str, dictionary: List[str]) -> int:
    # Approach: BFS through adjacent words. Stop when reach end 
    # construct graph 
    dict_set = set(dictionary)
    g = defaultdict(list) # { word: [neighbouring word1, 2, ...]}
    for word in dictionary:
        # generate adjacent words by swapping each letter and seeing if it's in the dictionary set 
        for j in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                neighbour = word[:j] + c + word[j + 1:]
                if neighbour in dict_set and neighbour != word:
                    g[word].append(neighbour)
    # bfs 
    distances = {start : 0}
    q = deque()
    q.append(start)
    while len(q) > 0:
        curr = q.popleft()
        for neighbour in g[curr]:
            if neighbour not in distances:
                distances[neighbour] = distances[curr] + 1
                q.append(neighbour)
    if end not in distances:
        return 0
    print(distances)
    return distances[end] + 1


print(shortest_transformation_sequence("red", "hit", ["red","bed","hat","rod","rad","rat","hit","bad","bat"]))