from sys import exit


def read_graph_as_lists(vertex_quantity, edge_quantity):
    graph = [[] for i in range(vertex_quantity)]
    for edge in range(edge_quantity):
        link1, link2 = [int(x) for x in input().split()]
        graph[link1].append(link2)
    return graph


def deep_first_search(current_vertex, graph, stack=None, used_vertexes=None):
    stack.append(current_vertex), used_vertexes.add(current_vertex)
    for neighbour in graph[current_vertex]:
        if neighbour not in used_vertexes:
            deep_first_search(neighbour, graph, stack, used_vertexes)
        elif neighbour == stack[0]:
            print(' '.join(map(str, stack)))
            exit(0)
    stack.pop()

vertex_number, edge_number = tuple(map(int, input().split()))
my_graph = read_graph_as_lists(vertex_number, edge_number)
for vertex in range(vertex_number):
    deep_first_search(vertex, my_graph, [], set())
print('YES')
