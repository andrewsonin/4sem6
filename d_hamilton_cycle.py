def read_graph_as_lists(vertex_quantity, edge_quantity):
    graph = [[] for i in range(vertex_quantity)]
    for edge in range(edge_quantity):
        link1, link2 = [int(x) for x in input().split()]
        graph[link1].append(link2), graph[link2].append(link1)
    return graph


def hamilton_cycle(graph, vertex_quantity, vertex=0, used_vertexes=None, path=None):
    if not used_vertexes:
        used_vertexes, path = {0}, []
    path.append(vertex)
    if len(path) == vertex_quantity:
        if path[-1] in graph[path[0]]:
            return True, path
        else:
            path.pop()
            return False
    used_vertexes.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used_vertexes:
            if hamilton_cycle(graph, vertex_quantity, neighbour, used_vertexes, path):
                return True, path
    used_vertexes.remove(vertex), path.pop()
    return False

vertex_number, edge_number = tuple(map(int, input().split()))
print(' '.join(map(str, hamilton_cycle(read_graph_as_lists(vertex_number, edge_number), vertex_number)[1])))
