import heapq

def greedy_best_first_search(graph, start, goal, heuristic):

    priority_queue = [(heuristic(start, goal), start, [start])]
    visited = set()

    while priority_queue:
        _, current_node, path = heapq.heappop(priority_queue)

        if current_node not in visited:
            visited.add(current_node)

            if current_node == goal:
                return path

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (heuristic(neighbor, goal), neighbor, path + [neighbor]))

    return None

# Example usage:
graph = {
    'A': {'B': 1, 'C': 2},
    'B': {'A': 1, 'D': 3, 'E': 4},
    'C': {'A': 2, 'F': 0, 'G':1},
    'D': {'B': 3},
    'E': {'B': 4, 'H': 5},
    'F': {'C': 1,'J':1},
    'G': {'C': 2,'J':0},
    'H': {'E': 5, 'I': 1, 'J': 3},
    'I': {'H': 1},
    'J': {'H': 3} 
}

start_node = 'A'
goal_node = 'J'

# Heuristic function (Euclidean distance between nodes)
def heuristic(node, goal):
    # For simplicity, let's assume all nodes are single letters
    return abs(ord(node) - ord(goal))

# Find the path using Greedy Best-First Search
gbfs_path = greedy_best_first_search(graph, start_node, goal_node, heuristic)

if gbfs_path:
    print(f"Path from {start_node} to {goal_node}: {gbfs_path}")
else:
    print(f"No path found from {start_node} to {goal_node}")