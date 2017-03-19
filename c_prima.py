def read_graph_as_lists(vertex_quantity, edge_quantity):
    graph = [[] for i in range(vertex_quantity)]
    for edge in range(edge_quantity):
        link1, link2, weight = [int(x) for x in input().split()]
        graph[link1].append((link2, int(weight))), graph[link2].append((link1, int(weight)))
    return graph


def prim(graph, vertex_quantity):
    spanning_edges, spanning_vertexes, full_weight = [], {0}, 0
    for i in range(vertex_quantity - 1):
        min_length = float('+inf')
        for vertex in spanning_vertexes:
            for (neighbour, weight) in graph[vertex]:
                if neighbour not in spanning_vertexes and weight < min_length:
                    min_length, current_vertex, current_edges = weight, neighbour, (vertex, neighbour)
        spanning_edges.append(current_edges), spanning_vertexes.add(current_vertex)
        full_weight += min_length
    return full_weight, spanning_edges

vertex_number, edge_number = tuple(map(int, input().split()))
result = prim(read_graph_as_lists(vertex_number, edge_number), vertex_number)
print(result[0])
for edge in result[1]:
    print(' '.join(map(str, edge)))
