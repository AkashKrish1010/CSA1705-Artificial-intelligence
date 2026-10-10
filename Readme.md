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

# Experiment 3 - Water Jug Problem (WJP)

## Objective

Solve the Water Jug Problem using BFS to find the minimum sequence of operations to reach a target volume.

---

## Pseudo Code

```
WJP_BFS(capacities, initial, target):
    Create a queue and enqueue (initial, path=[initial])
    Create an empty set visited
    Add initial to visited

    While queue is not empty:
        state, path = Dequeue from queue

        If target in state:
            Return path

        For each jug i:
            Fill jug i         -> new_state[i] = capacities[i]
            Empty jug i        -> new_state[i] = 0
            For each jug j != i:
                Pour i to j    -> transfer min(state[i], cap[j] - state[j])

            If new_state not in visited:
                Add to visited
                Enqueue (new_state, path + [new_state])

    Return None
```

---

## Inputs

| Problem | Capacities | Initial State | Target |
|---------|------------|---------------|--------|
| 1 | (12, 8, 5) | (12, 0, 0) | 4 |
| 2 | (6, 8, 5) | (0, 0, 0) | 5 |
| 3 | (3, 5) | (0, 0) | 4 |

---

## Time and Space Complexity

| Metric           | Value    |
|------------------|----------|
| Time Complexity  | O(C1 x C2 x ... x Cn) |
| Space Complexity | O(C1 x C2 x ... x Cn) |

Where C1, C2, ..., Cn are the capacities of each jug.

---

## File

`EXP_3_WJP.py`

---

# Experiment 4 - Uniform Cost Search (UCS)

## Objective

Implement Uniform Cost Search to find the least-cost path in a weighted graph by expanding nodes in order of cumulative path cost.

---

## Pseudo Code

```
UCS(Graph, start, goal):
    Create a priority queue
    Push (cost = 0, start, path = [start]) into queue
    Create an empty set visited

    While queue is not empty:
        cost, node, path = Pop node with lowest cost

        If node in visited: continue
        Add node to visited

        If node == goal:
            Return path, cost

        For each (neighbor, weight) in Graph[node]:
            If neighbor not in visited:
                Push (cost + weight, neighbor, path + [neighbor])

    Return None
```

---

## Inputs

| Graph | Description | Start | Goal |
|-------|-------------|-------|------|
| Graph 1 | Simple weighted graph | A | G |
| Graph 2 | Romania Map | Arad | Bucharest |
| Graph 3 | City road network | S | G |

---

## Time and Space Complexity

| Metric           | Value      |
|------------------|------------|
| Time Complexity  | O(E log V) |
| Space Complexity | O(V)       |

Where V = number of vertices and E = number of edges.

---

## File

`EXP_4_UCS.py`

---

# Experiment 5 - A* Search Algorithm

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

`EXP_5_Astar.py`
