# Experiment 1 - Breadth First Search (BFS)

## Objective

Implement and demonstrate Breadth First Search (BFS) traversal on multiple graph structures.

---

## Pseudo Code

```
BFS(Graph, start_node):
    Create an empty queue Q
    Create an empty visited list
    Create an empty set seen

    Enqueue start_node into Q
    Add start_node to seen

    While Q is not empty:
        node = Dequeue from Q
        Append node to visited

        For each neighbor in Graph[node]:
            If neighbor not in seen:
                Add neighbor to seen
                Enqueue neighbor into Q

    Return visited
```

---

## Time and Space Complexity

| Metric          | Value     |
|-----------------|-----------|
| Time Complexity | O(V + E)  |
| Space Complexity| O(V)      |

Where V = number of vertices and E = number of edges.

---

## File

`EXP_1_Bfs.py`

---

# Experiment 2 - Depth First Search (DFS)

## Objective

Implement and demonstrate Depth First Search (DFS) traversal on multiple graph structures.

---

## Pseudo Code

```
DFS(Graph, start_node):
    Create an empty visited list
    Create an empty set seen

    Define recurse(node):
        Add node to seen
        Append node to visited

        For each neighbor in Graph[node]:
            If neighbor not in seen:
                Call recurse(neighbor)

    Call recurse(start_node)
    Return visited
```

---

## Time and Space Complexity

| Metric           | Value    |
|------------------|----------|
| Time Complexity  | O(V + E) |
| Space Complexity | O(V)     |

Where V = number of vertices and E = number of edges.

---

## File

`EXP_2_Dfs.py`

---

# Experiment 3 - A* Search Algorithm

## Objective

Implement and demonstrate the A* search algorithm to find the optimal path in weighted graphs using a heuristic function.

---

## Pseudo Code

```
ASTAR(Graph, heuristic, start, goal):
    Create a priority queue open_list
    Push (f = 0 + h(start), g = 0, start, path = [start]) into open_list
    Create an empty set visited

    While open_list is not empty:
        Pop (f, g, node, path) with lowest f from open_list

        If node in visited: continue
        Add node to visited

        If node == goal:
            Return path, g

        For each (neighbor, cost) in Graph[node]:
            If neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                Push (new_f, new_g, neighbor, path + [neighbor]) into open_list

    Return None
```

---

## Inputs

| Graph | Description | Start | Goal |
|-------|-------------|-------|------|
| Graph 1 | Simple weighted graph (A to G) | A | G |
| Graph 2 | Romania Map (classic AI problem) | Arad | Bucharest |
| Graph 3 | Grid-style weighted graph | 1 | 8 |

---

## Time and Space Complexity

| Metric           | Value         |
|------------------|---------------|
| Time Complexity  | O(E log V)    |
| Space Complexity | O(V)          |

Where V = number of vertices and E = number of edges.

---

## File

`EXP_3_Astar.py`
