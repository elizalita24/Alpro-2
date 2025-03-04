import time
import networkx as nx
from collections import deque

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
    cycles = []
    def dfs(node, path):
        for neighbor in graph[node]:
            if neighbor == start and len(path) > 2:
                cycles.append(path + [start])
            elif neighbor not in path:
                dfs(neighbor, path + [neighbor])
    dfs(start, [start])
    for cycle in cycles:
        print("Cycle:", cycle)

def find_circuits(graph, start):
    queue = deque([(start, [start])])
    circuits = []
    while queue:
        node, path = queue.popleft()
        for neighbor in graph[node]:
            if neighbor == start and len(path) > 2:
                circuits.append(path + [start])
            elif neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
    if circuits:
        shortest = min(circuits, key=len)
        longest = max(circuits, key=len)
        print("Shortest Circuit:", shortest)
        print("Longest Circuit:", longest)
    else:
        print("No circuits found.")

# Definisi graf sesuai gambar pada CHALLENGE 2
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'F'],
    'D': ['A', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['C', 'E']
}

start_time = time.time()

# Mencari semua Path
print("--- Paths A to C ---")
find_paths(graph, 'A', 'C')

# Mencari semua Cycle
print("--- Cycles from C ---")
find_cycles(graph, 'C')

print("--- Cycles from B ---")
find_cycles(graph, 'B')

# Mencari circuit terpendek dan terpanjang dari A ke A
print("--- Circuits A to A ---")
find_circuits(graph, 'A')

end_time = time.time()
print(f"Execution Time: {end_time - start_time:.6f} seconds")