import sys



def topological_sort(graph, count):
    top_sort = []
    temp_visited = []
    visited = []

    number_of_nodes = len(graph)
    result = True

    # Initially all nodes are unvisited
    for i in range(0, number_of_nodes):
        temp_visited.append(False)
        visited.append(False)

    for i in range(0, number_of_nodes):
        result = visit(i, top_sort, visited, temp_visited, graph, count)
        if not result:
            return False

        if len(top_sort) == count:
            return True
    return True


def visit(node, top_sort, visited, temp_visited, graph, count):
    if visited[node]:
        return True

    if temp_visited[node]:
        return False


    # Mark node temporarily
    temp_visited[node] = True

    #Visit all its neighbours
    neighbours = graph[node]
    for neighbour in neighbours:
        result = visit(neighbour, top_sort, visited, temp_visited, graph, count)
        if not result:
            return False

    #m Mark node permanently
    visited[node] = True

    # Add node to head of list
    top_sort.insert(0, node)

    return True


graph = {}
graph[5] = [0,2]
graph[4] = [0,1]
graph[3] = [1]
graph[2] = [3]
graph[1] = []
graph[0] = []
print(topological_sort(graph, 6))

graph = {}
graph[1] = [0]
graph[0] = [1]
print(topological_sort(graph, 2))

graph = {}
graph[1] = [0]
graph[0] = []
count = 2
print(topological_sort(graph, count))

