from collections import deque

def water_jug_bfs(capacities, initial, target):
    queue = deque()
    queue.append((initial, [initial]))
    visited = set()
    visited.add(initial)

    while queue:
        state, path = queue.popleft()

        if target in state:
            return path

        n = len(capacities)
        next_states = []

        for i in range(n):
            # Fill jug i from tap
            new = list(state)
            new[i] = capacities[i]
            next_states.append(tuple(new))

            # Empty jug i
            new = list(state)
            new[i] = 0
            next_states.append(tuple(new))

            # Pour from jug i to jug j
            for j in range(n):
                if i != j:
                    new = list(state)
                    pour = min(state[i], capacities[j] - state[j])
                    new[i] -= pour
                    new[j] += pour
                    next_states.append(tuple(new))

        for ns in next_states:
            if ns not in visited:
                visited.add(ns)
                queue.append((ns, path + [ns]))

    return None


def print_solution(capacities, path, target):
    labels = [f"Jug{i+1}({capacities[i]}L)" for i in range(len(capacities))]
    header = "  ".join(f"{l:>12}" for l in labels)
    print(f"  {'Step':>4}  {header}")
    print("  " + "-" * (14 * len(capacities) + 6))
    for step, state in enumerate(path):
        row = "  ".join(f"{v:>12}" for v in state)
        marker = "  <-- TARGET FOUND" if target in state else ""
        print(f"  {step:>4}  {row}{marker}")


print("Experiment 3 - Water Jug Problem (WJP)")
print("=" * 45)

# -------------------------------------------------------------------
# Problem 1: Capacities 12, 8, 5 | Start: (12, 0, 0) | Target: 4
# -------------------------------------------------------------------
caps1    = (12, 8, 5)
initial1 = (12, 0, 0)
target1  = 4

print(f"\nProblem 1: Jugs = {caps1}, Start = {initial1}, Target = {target1}")
path1 = water_jug_bfs(caps1, initial1, target1)
if path1:
    print_solution(caps1, path1, target1)
    print(f"  Steps taken: {len(path1) - 1}")
else:
    print("  No solution found.")

# -------------------------------------------------------------------
# Problem 2: Capacities 6, 8, 5 | Start: (0, 0, 0) | Target: 5
# -------------------------------------------------------------------
caps2    = (6, 8, 5)
initial2 = (0, 0, 0)
target2  = 5

print(f"\nProblem 2: Jugs = {caps2}, Start = {initial2}, Target = {target2}")
path2 = water_jug_bfs(caps2, initial2, target2)
if path2:
    print_solution(caps2, path2, target2)
    print(f"  Steps taken: {len(path2) - 1}")
else:
    print("  No solution found.")

# -------------------------------------------------------------------
# Problem 3 (Choice): Capacities 3, 5 | Start: (0, 0) | Target: 4
# Classic 2-jug problem - requires multiple pour operations
# -------------------------------------------------------------------
caps3    = (3, 5)
initial3 = (0, 0)
target3  = 4

print(f"\nProblem 3: Jugs = {caps3}, Start = {initial3}, Target = {target3}")
path3 = water_jug_bfs(caps3, initial3, target3)
if path3:
    print_solution(caps3, path3, target3)
    print(f"  Steps taken: {len(path3) - 1}")
else:
    print("  No solution found.")
