
"""
Experiment 4: A* Search Algorithm
Author: Dev Jain
Roll No: IC2K23-21
"""

import heapq


# Define the graph with nodes and edge costs
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 4)],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}


# Heuristic values for each node
h_value = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 2,
    'G': 0
}


def a_star_search(source, destination):

    # Priority queue stores cost, node and path
    open_list = [(h_value[source], 0, source, [source])]

    explored = {}

    while open_list:

        total_cost, current_cost, current_node, route = heapq.heappop(open_list)

        # Check if destination is reached
        if current_node == destination:
            print("Shortest Path:", " -> ".join(route))
            print("Total Cost:", current_cost)
            return

        # Skip previously explored better paths
        if current_node in explored and explored[current_node] <= current_cost:
            continue

        explored[current_node] = current_cost

        # Visit neighbouring nodes
        for next_node, weight in graph[current_node]:

            updated_cost = current_cost + weight
            estimated_cost = updated_cost + h_value[next_node]

            heapq.heappush(
                open_list,
                (estimated_cost, updated_cost, next_node, route + [next_node])
            )

    print("No path found.")


print("A* SEARCH ALGORITHM")
print("-" * 35)

a_star_search('A', 'G')
