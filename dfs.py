def dfs(graph, start, goal):
    visited = set()

    def dfs_recursive(current_node, path):
        visited.add(current_node)

        if current_node == goal:
            return path

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                result = dfs_recursive(neighbor, path + [neighbor])
                if result:
                    return result

        return None

    start_path = [start]
    return dfs_recursive(start, start_path)

# Example usage:
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F', 'G'},
    'D': {'B'},
    'E': {'B', 'H'},
    'F': {'C'},
    'G': {'C'},
    'H': {'E', 'I', 'J'},
    'I': {'H'},
    'J': {'H'}
}

start_node = 'A'
goal_node = 'I'

# Find the path using DFS
dfs_path = dfs(graph, start_node, goal_node)

if dfs_path:
    print(f"Path from {start_node} to {goal_node}: {dfs_path}")
else:
    print(f"No path found from {start_node} to {goal_node}")