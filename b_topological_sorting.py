from sys import exit


def read_graph_as_lists(vertex_quantity, edge_quantity):
    graph = [[] for i in range(vertex_quantity)]
    for edge in range(edge_quantity):
        link1, link2 = [int(x) for x in input().split()]
        graph[link1].append(link2)
    return graph


def deep_first_search_tarjan(current_vertex, graph, sorted_path=None, used_vertexes=None, gray_vertexes=None):
    gray_vertexes.add(current_vertex), used_vertexes.add(current_vertex)
    for neighbour in graph[current_vertex]:
        if neighbour not in used_vertexes:
            deep_first_search_tarjan(neighbour, graph, sorted_path, used_vertexes, gray_vertexes)
        elif neighbour in gray_vertexes:
            print('NO')
            exit(0)
    gray_vertexes.remove(current_vertex), sorted_path.append(current_vertex)


def topological_sorting(graph, vertex_quantity):
    sorted_vertexes, used_vertexes = [], set()
    for vertex in range(vertex_quantity):
        if vertex not in used_vertexes:
            deep_first_search_tarjan(vertex, graph, sorted_vertexes, used_vertexes, set())
    print(' '.join(map(str, sorted_vertexes[::-1])))

vertex_number, edge_number = tuple(map(int, input().split()))
topological_sorting(read_graph_as_lists(vertex_number, edge_number), vertex_number)
