import heapq

def astar(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic[start], 0, start, [start]))

    visited = set()

    while open_list:
        f, g, node, path = heapq.heappop(open_list)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path, g

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')


# -------------------------------------------------------------------
# Graph 1 - Simple Weighted Graph
# Nodes: A B C D E F G
# Find shortest path from A to G
# -------------------------------------------------------------------
graph1 = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1), ('E', 3)],
    'D': [('F', 2)],
    'E': [('F', 1)],
    'F': [('G', 2)],
    'G': []
}

heuristic1 = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}

# -------------------------------------------------------------------
# Graph 2 - Romania Map (Classic AI Problem)
# Find shortest path from Arad to Bucharest
# -------------------------------------------------------------------
graph2 = {
    'Arad':        [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind':      [('Arad', 75), ('Oradea', 71)],
    'Oradea':      [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu':       [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu', 80)],
    'Timisoara':   [('Arad', 118), ('Lugoj', 111)],
    'Lugoj':       [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia':     [('Lugoj', 70), ('Dobreta', 75)],
    'Dobreta':     [('Mehadia', 75), ('Craiova', 120)],
    'Craiova':     [('Dobreta', 120), ('Rimnicu', 146), ('Pitesti', 138)],
    'Rimnicu':     [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras':     [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti':     [('Rimnicu', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest':   [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu':     [('Bucharest', 90)],
    'Urziceni':    [('Bucharest', 85)]
}

heuristic2 = {
    'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Sibiu': 253,
    'Timisoara': 329, 'Lugoj': 244, 'Mehadia': 241, 'Dobreta': 242,
    'Craiova': 160, 'Rimnicu': 193, 'Fagaras': 176, 'Pitesti': 100,
    'Bucharest': 0, 'Giurgiu': 77, 'Urziceni': 80
}

# -------------------------------------------------------------------
# Graph 3 - Grid-style Weighted Graph
# Nodes: 1 to 8, find path from 1 to 8
# -------------------------------------------------------------------
graph3 = {
    1: [(2, 2), (3, 5)],
    2: [(1, 2), (4, 3), (5, 4)],
    3: [(1, 5), (5, 2), (6, 6)],
    4: [(2, 3), (7, 4)],
    5: [(2, 4), (3, 2), (7, 1), (8, 6)],
    6: [(3, 6), (8, 3)],
    7: [(4, 4), (5, 1), (8, 2)],
    8: [(5, 6), (6, 3), (7, 2)]
}

heuristic3 = {
    1: 7, 2: 5, 3: 6,
    4: 4, 5: 3, 6: 4,
    7: 2, 8: 0
}


print("Experiment 3 - A* Search Algorithm")
print("=" * 45)

path, cost = astar(graph1, heuristic1, 'A', 'G')
print("\nGraph 1 (Simple Weighted Graph):")
print("Path  :", " -> ".join(path))
print("Cost  :", cost)

path, cost = astar(graph2, heuristic2, 'Arad', 'Bucharest')
print("\nGraph 2 (Romania Map):")
print("Path  :", " -> ".join(path))
print("Cost  :", cost)

path, cost = astar(graph3, heuristic3, 1, 8)
print("\nGraph 3 (Grid-style Weighted Graph):")
print("Path  :", " -> ".join(str(n) for n in path))
print("Cost  :", cost)
