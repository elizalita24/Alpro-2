from collections import deque
import time

def find_trails(graph, start, end):
    queue = deque([(start, [start], set())])
    trails = []
    while queue:
        node, path, visited_edges = queue.popleft()
        if node == end:
            trails.append(path)
        for neighbor in graph[node]:
            edge = tuple(sorted([node, neighbor]))
            if edge not in visited_edges:
                queue.append((neighbor, path + [neighbor], visited_edges | {edge}))
    for trail in trails:
        print("Trail:", trail)

def find_paths(graph, start, end):
    queue = deque([(start, [start])])
    paths = []
    while queue:
        node, path = queue.popleft()
        if node == end:
            paths.append(path)
        for neighbor in graph[node]:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
    for path in paths:
        print("Path:", path)

def find_cycles(graph, start):
    queue = deque([(start, [start])])
    cycles = []
    while queue:
        node, path = queue.popleft()
        for neighbor in graph[node]:
            if neighbor == start and len(path) > 2:
                cycles.append(path + [start])
            elif neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
    for cycle in cycles:
        print("Cycle:", cycle)

# Definisi graf sebagai adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

start_time = time.time()

# Mencari Trail dari A ke D
print("--- Trails A to D ---")
find_trails(graph, 'A', 'D')

# Mencari semua Path dari A ke D
print("--- Paths A to D ---")
find_paths(graph, 'A', 'D')

# Mencari semua Cycle dari A
print("--- Cycles from A ---")
find_cycles(graph, 'A')

end_time = time.time()
print(f"Execution Time: {end_time - start_time:.6f} seconds")