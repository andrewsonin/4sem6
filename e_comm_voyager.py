def read_graph_as_wm(vertex_quantity, edge_quantity):
    weight_matrix = [[float('+inf')] * vertex_quantity for i in range(vertex_quantity)]
    graph = [[] for i in range(vertex_quantity)]
    for i in range(vertex_quantity):
        weight_matrix[i][i] = 0
    for edge in range(edge_quantity):
        link1, link2, weight = [int(x) for x in input().split()]
        weight_matrix[link1][link2], weight_matrix[link2][link1] = weight, weight
        graph[link1].append(link2), graph[link2].append(link1)
    return weight_matrix, graph


def hamilton_cycle(graph, vertex_quantity, vertex=0, used=set(), path=list(), paths=list()):
    used.add(vertex), path.append(vertex)
    if len(path) == vertex_quantity:
        if path[0] in graph[path[-1]]:
            paths.append(path.copy())
    else:
        for neighbour in graph[vertex]:
            if neighbour not in used:
                hamilton_cycle(graph, vertex_quantity, neighbour, used, path, paths)
    path.pop(), used.remove(vertex)

vertex_number, edge_number = tuple(map(int, input().split()))
my_graph = read_graph_as_wm(vertex_number, edge_number)
my_paths = []
hamilton_cycle(my_graph[1], vertex_number, paths=my_paths)
full_price, profitable_path = float('+inf'), []
for path in my_paths:
    current_price = 0
    for i in range(vertex_number):
        current_price += my_graph[0][path[i - 1]][path[i]]
    if current_price < full_price:
        full_price = current_price
        profitable_path = path
print(full_price)
print(' '.join(map(str, profitable_path)))
