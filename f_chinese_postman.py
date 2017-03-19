def read_graph_as_wm(vertex_quantity, edge_quantity):
    weight_matrix = [[float('+inf')] * vertex_quantity for i in range(vertex_quantity)]
    graph = [[] for i in range(vertex_quantity)]
    for i in range(vertex_quantity):
        weight_matrix[i][i] = 0
    for edge in range(edge_quantity):
        link1, link2, weight = [int(x) for x in input().split()]
        weight_matrix[link1][link2], weight_matrix[link2][link1] = weight, weight
        graph[link1].append(link2), graph[link2].append(link1)
    return [weight_matrix, graph]


def floyd_warshall(weight_matrix, vertexes):
    for k in range(vertexes):
        for i in range(vertexes):
            for j in range(vertexes):
                weight_matrix[i][j] = min(weight_matrix[i][j], weight_matrix[i][k] + weight_matrix[k][j])
    return weight_matrix


def expose_odd_vertexes(graph, vertex_quantity):
    odd_vertexes, even_sum = [], 0
    for vertex in range(vertex_quantity):
        if len(graph[vertex]) % 2 == 1:
            odd_vertexes.append(vertex)
    return odd_vertexes


# FIXME! This functions works for factorial time, but it is possible to make an algorithm that works for polynomial time
def minimal_pairs(graph, weight_matrix, vertex=0, previous=0, used=set(), matching=True):
    used.add(vertex)
    neighbours_length, tmp = float('+inf'), 0
    for neighbour in graph:
        if neighbour not in used:
            tmp = minimal_pairs(graph, weight_matrix, neighbour, vertex, used, matching ^ True)
            if tmp < neighbours_length:
                neighbours_length = tmp
    used.remove(vertex)
    if not matching:
        return weight_matrix[previous][vertex] + tmp
    else:
        return neighbours_length

vertex_number, edge_number = tuple(map(int, input().split()))
my_graph = read_graph_as_wm(vertex_number, edge_number)
full_price, used = 0, set()
for vertex in range(vertex_number):
    for neighbour in my_graph[1][vertex]:
        if (vertex, neighbour) not in used:
            full_price += my_graph[0][vertex][neighbour]
            used.add((neighbour, vertex))
my_graph[0] = floyd_warshall(my_graph[0], vertex_number)
odds = expose_odd_vertexes(my_graph[1], vertex_number)
print(full_price + minimal_pairs(odds, my_graph[0], odds[0]))
