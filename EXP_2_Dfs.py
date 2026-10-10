def dfs(graph, start):
    visited = []
    seen = set()

    def recurse(node):
        seen.add(node)
        visited.append(node)
        for neighbor in graph[node]:
            if neighbor not in seen:
                recurse(neighbor)

    recurse(start)
    return visited


# Graph 1 - Simple tree: 1-2-3-4-5
graph1 = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

# Graph 2 - Larger tree: root=1, children 2,7; 2->3,6; 7->8,10; 3->4,5; 6->9
graph2 = {
    1:  [2, 7],
    2:  [3, 6],
    7:  [8, 10],
    3:  [4, 5],
    6:  [9],
    8:  [],
    10: [],
    4:  [],
    5:  [],
    9:  []
}

# Graph 3 - Undirected graph: 1 connected to 2,3; 2->5,6; 3->4,7; 4-8 (square)
graph3 = {
    1: [2, 3],
    2: [1, 5, 6],
    3: [1, 4, 7],
    4: [3, 8],
    5: [2],
    6: [2],
    7: [3, 8],
    8: [4, 7]
}

# Graph 4 - Directed graph: 0->1->3->4->5; 2->1; 1->2 (cycle); 3->2; 6->4; 5->7->6
graph4 = {
    0: [1],
    1: [3, 2],
    2: [1],
    3: [2, 4],
    4: [5],
    5: [7],
    6: [4],
    7: [6]
}


print("Experiment 2 - Depth First Search (DFS)")
print("=" * 45)

print("\nGraph 1 (Simple Tree):")
print("DFS traversal:", dfs(graph1, 1))

print("\nGraph 2 (Larger Tree):")
print("DFS traversal:", dfs(graph2, 1))

print("\nGraph 3 (Undirected Graph with cycles):")
print("DFS traversal:", dfs(graph3, 1))

print("\nGraph 4 (Directed Graph):")
print("DFS traversal:", dfs(graph4, 0))
