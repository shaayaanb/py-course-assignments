# ---------------------------------------------
# الگوریتم های پیمایش گراف
# ---------------------------------------------

def BFS(graph, start):
    queue = [start]
    visited = set([start])

    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited

def DFS(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited)

    return visited