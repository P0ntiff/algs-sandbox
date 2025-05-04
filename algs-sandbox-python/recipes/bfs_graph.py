





def bfs(g):
    q = deque()
    q.append(0)
    distances = {0: 0}
    while len(q) > 0:
        node = q.popleft()
        for neighbour in g[node]:
            if neighbour in distances:
                continue 
            distances[neighbour] = 1 + distances[node]
            q.append(neighbour)
        