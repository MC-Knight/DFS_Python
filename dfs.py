def depth_first_search(graph, start_seaarch, end_target, visited, path):
    visited.add(start_seaarch)
    path.append(start_seaarch)

    if start_seaarch == end_target:
        return path

    for neighbor in graph[start_seaarch]:
        if neighbor not in visited:
            result = depth_first_search(graph, neighbor, end_target, visited, path)
            if result:
                return result

    path.pop()
    return None


graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}


start_node = "A"
end_node = "F"
visited_nodes = set()
path = []

result = depth_first_search(graph, start_node, end_node, visited_nodes, path)
if result:
    print("Path found:", "->".join(result))
else:
    print("Path not found.")
