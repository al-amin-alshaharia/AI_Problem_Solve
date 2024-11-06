from collections import deque

def bidirectional_search(graph, start, goal):

    start_queue = deque([(start, [start])])
    goal_queue = deque([(goal, [goal])])

    start_visited = set()
    goal_visited = set()

    while start_queue and goal_queue:
        start_node, start_path = start_queue.popleft()
        goal_node, goal_path = goal_queue.popleft()

        # Check if the paths from the start and goal nodes intersect
        intersection = set(start_path) & set(goal_path)
        if intersection:
            meeting_point = intersection.pop()
            return start_path + goal_path[::-1][1:]

        # Explore neighbors from the start node
        if start_node not in start_visited:
            for neighbor in graph[start_node]:
                start_queue.append((neighbor, start_path + [neighbor]))
            start_visited.add(start_node)

        # Explore neighbors from the goal node
        if goal_node not in goal_visited:
            for neighbor in graph[goal_node]:
                goal_queue.append((neighbor, goal_path + [neighbor]))
            goal_visited.add(goal_node)

    return None

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

# Find the path using Bidirectional Search
bidirectional_path = bidirectional_search(graph, start_node, goal_node)

if bidirectional_path:
    print(f"Path from {start_node} to {goal_node}: {bidirectional_path}")
else:
    print(f"No path found from {start_node} to {goal_node}")