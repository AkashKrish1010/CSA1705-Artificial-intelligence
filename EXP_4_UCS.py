import heapq

def ucs(graph, start, goal):
    queue = []
    heapq.heappush(queue, (0, start, [start]))
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path, cost

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))

    return None, float('inf')


# -------------------------------------------------------------------
# Graph 1 - Simple Weighted Graph (A to G)
# -------------------------------------------------------------------
graph1 = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 3), ('E', 7)],
    'C': [('B', 1), ('D', 5)],
    'D': [('F', 2)],
    'E': [('F', 3)],
    'F': [('G', 1)],
    'G': []
}

# -------------------------------------------------------------------
# Graph 2 - Romania Map (Arad to Bucharest)
# -------------------------------------------------------------------
graph2 = {
    'Arad':      [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind':    [('Arad', 75), ('Oradea', 71)],
    'Oradea':    [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu':     [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj':     [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia':   [('Lugoj', 70), ('Dobreta', 75)],
    'Dobreta':   [('Mehadia', 75), ('Craiova', 120)],
    'Craiova':   [('Dobreta', 120), ('Rimnicu', 146), ('Pitesti', 138)],
    'Rimnicu':   [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras':   [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti':   [('Rimnicu', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101)]
}

# -------------------------------------------------------------------
# Graph 3 - City Road Network (S to G)
# -------------------------------------------------------------------
graph3 = {
    'S': [('A', 1), ('B', 5)],
    'A': [('B', 2), ('C', 7)],
    'B': [('C', 3), ('D', 6)],
    'C': [('G', 1)],
    'D': [('G', 8)],
    'G': []
}


print("Experiment 4 - Uniform Cost Search (UCS)")
print("=" * 45)

path, cost = ucs(graph1, 'A', 'G')
print("\nGraph 1 (Simple Weighted Graph):")
print("Path  :", " -> ".join(path))
print("Cost  :", cost)

path, cost = ucs(graph2, 'Arad', 'Bucharest')
print("\nGraph 2 (Romania Map):")
print("Path  :", " -> ".join(path))
print("Cost  :", cost)

path, cost = ucs(graph3, 'S', 'G')
print("\nGraph 3 (City Road Network):")
print("Path  :", " -> ".join(path))
print("Cost  :", cost)
