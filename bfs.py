from collections import deque

def bfs_shortest_path(graph, start, goal):
    if start == goal:
        return [start]

    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current_node, path = queue.popleft()

        if current_node not in visited:
            for neighbor in graph[current_node]:
                if neighbor == goal:
                    return path + [neighbor]

                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

            visited.add(current_node)

# Example usage:
# Define a graph using an adjacency list
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F', 'G'},
    'D': {'B'},
    'E': {'B', 'H'},
    'F': {'C'},
    'G': {'C'},
    'H': {'E','I','J'},
    'I': {'H'},
    'J': {'H'}
}

# Define start and goal nodes
start_node = 'A'
goal_node = 'J'

# Find the shortest path
shortest_path = bfs_shortest_path(graph, start_node, goal_node)

if shortest_path:
    print(f"Shortest path from {start_node} to {goal_node}: {shortest_path}")
else:
    print(f"No path found from {start_node} to {goal_node}")