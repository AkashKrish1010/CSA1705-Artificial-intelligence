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
