import heapq

def ucs(graph, start, goal):

    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        cost, current_node, path = heapq.heappop(priority_queue)

        if current_node not in visited:
            visited.add(current_node)

            if current_node == goal:
                return path

            for neighbor, edge_cost in graph[current_node].items():
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path + [neighbor]))

    return None

# Example usage:
graph_with_costs = {
    'A': {'B': 1, 'C': 2},
    'B': {'A': 1, 'D': 3, 'E': 4},
    'C': {'A': 2, 'F': 1, 'G':0},
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

# Find the path using UCS
ucs_path = ucs(graph_with_costs, start_node, goal_node)

if ucs_path:
    print(f"Path from {start_node} to {goal_node}: {ucs_path}")
else:
    print(f"No path found from {start_node} to {goal_node}")
