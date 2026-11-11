
"""
Hill Climbing Algorithm
"""

def hill_climbing(start, values):

    current = start

    while True:

        neighbours = [current - 1, current + 1]
        best = current

        for next_state in neighbours:

            if (next_state in values and
                    values[next_state] > values[best]):
                best = next_state

        if best == current:
            break

        current = best

    return current


values = {
    0: 2,
    1: 5,
    2: 8,
    3: 6,
    4: 10,
    5: 7
}

answer = hill_climbing(0, values)

print("HILL CLIMBING ALGORITHM")
print("-" * 35)

print("Best State:", answer)
print("Maximum Value:", values[answer])
