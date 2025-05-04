



# peel off algo:
# topo_order = empty list
#  while 0 degree node:
#       add 0 degree node to  topo order
#      decrease in-degree of neighbours 
#      remove node from 0 degree nodes
#  if len(topo_order) < V: cycles, no more nodes with 0 degree but still left in the graph not peeled off
#



from collections import defaultdict

def topological_sort(graph):
    V = len(graph)
    in_degree = defaultdict(int)
    for node in range(V):
        for neighbour in graph[node]:
            in_degree[neighbour] += 1
    
    zero_degree_nodes = set([node for node in range(V) if in_degree[node] == 0])
    topo_order = []
    while len(zero_degree_nodes) > 0:
        latest = zero_degree_nodes.pop()
        topo_order.append(latest)
        for neighbour in graph[latest]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                zero_degree_nodes.append(neighbour)
    if len(topo_order) < Z:
        return [] # cycles
    return topo_order