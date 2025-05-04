




#V = 4
#Edge List: [(0, 1), (0, 2), (1, 3), (2, 3)]





















def build_adjacency_list(v: int, edge_list: list):
    res = [[] for _ in range(v)]
    for start, end in edge_list:
        res[start].append(end)
        res[end].append(start)
    return res 



#graph example to practice DFS 

"""
A ---- B      E ---- F
| \  / |
|  \/  |
|  /\  |
| /  \ |
C ---- D

"""

# V = 6 vertices = [(0, 1), (0, 2), (0, 3), (1, 3), (2, 1), (2, 3), (4, 5)]

# def build_adjacency_list(V, edge_list):
#     nodes = [[] for _ in range(V)]
#     for start, end in edge_list:
#         nodes[start].append(end)
#         nodes[end].append(start)
#     return nodes 


def find_dfs(V, edge_list, start, target):
    g = build_adjacency_list(V, edge_list)
    visited = set()
    def visit(start):
        nonlocal visited
        if start is None:
            return False
        if start == target:
            return True
        for neighbour in g[start]:
            if neighbour in visited:
                continue
            visited.add(neighbour)
            if visit(neighbour):
                return True
        return False
    return visit(start)

from collections import deque 

def find_bfs(V, edge_list, start, target):
    g = build_adjacency_list(V, edge_list)
    visited = set()
    def bfs(start):
        nonlocal visited
        q = deque()
        q.append(start)
        while len(q) > 0:
            node = q.popleft()
            if node == target:
                return True
            for n in g[node]:
                if n in visited:
                    continue
                visited.add(n)
                q.append(n)
        return False
    return bfs(start)

edge_list = [(0, 1), (0, 2), (0, 3), (1, 3), (2, 1), (2, 3), (4, 5)]
V = 6
print(find_bfs(V, edge_list, 2, 3))

# def dfs(v: int, edge_list: list, start):
#     node_list = build_adjacency_list(v, edge_list)
#     visited = {start}
#     def visit(node: int):
#         visited.add(node)
#         for neighbour in adj_list[node]:
#             if neighbour not in visited:
#                 dfs(neighbour)

#     return visit(start)

def count_connected_components(adj_list: list):
    visited = set()
    count = 0
    def dfs(v):
        visited.add(v)
        for neighbour in adj_list[v]:
            if neighbour not in visited:
                dfs(neighbour)
    for v in range(len(adj_list)):
        if v in visited:
            continue 
        count += 1
        dfs(v)
    return count


adj_list = build_adjacency_list(6, [(0, 1), (0, 2), (0, 3), (1, 3), (2, 1), (2, 3), (4, 5)])
print(count_connected_components(adj_list))