
"""
Experiment 3: Water Jug Problem Using BFS
Author: Dev Jain
Roll No: IC2K23-21
"""

from collections import deque


def generate_states(state, jug_a, jug_b):
    """Returns all possible states from the current state."""

    a, b = state

    transfer_ab = min(a, jug_b - b)
    transfer_ba = min(b, jug_a - a)

    next_states = [
        ("Fill Jug A", (jug_a, b)),
        ("Fill Jug B", (a, jug_b)),
        ("Empty Jug A", (0, b)),
        ("Empty Jug B", (a, 0)),
        ("Pour A into B", (a - transfer_ab, b + transfer_ab)),
        ("Pour B into A", (a + transfer_ba, b - transfer_ba))
    ]

    return next_states


def solve_water_jug(jug_a, jug_b, target):
    """Finds the solution using Breadth First Search."""

    start = (0, 0)

    q = deque([start])
    visited = {start}

    parent = {start: None}
    move = {}

    while q:

        state = q.popleft()
        a, b = state

        # Check whether target is achieved
        if a == target or b == target:
            result = state
            break

        # Explore all neighbouring states
        for action, new_state in generate_states(state, jug_a, jug_b):

            if new_state not in visited:

                visited.add(new_state)
                parent[new_state] = state
                move[new_state] = action

                q.append(new_state)

    else:
        return None

    # Trace back the solution
    solution = []
    current = result

    while current is not None:
        solution.append((current, move.get(current)))
        current = parent[current]

    return solution[::-1]


def main():

    jug_a = 4
    jug_b = 3
    target = 2

    print("WATER JUG PROBLEM USING BFS")
    print("-" * 40)

    print("Capacity of Jug A:", jug_a, "Litres")
    print("Capacity of Jug B:", jug_b, "Litres")
    print("Required Water:", target, "Litres")

    answer = solve_water_jug(jug_a, jug_b, target)

    if answer is None:
        print("\nTarget cannot be achieved.")
    else:
        print("\nSolution Found!")
        print("\nSteps to reach the target:")

        for i, (state, action) in enumerate(answer):

            if action is None:
                print(f"Step {i}: Starting State -> {state}")
            else:
                print(f"Step {i}: {action} -> {state}")

        print("\nFinal Goal State:", answer[-1][0])


if __name__ == "__main__":
    main()
