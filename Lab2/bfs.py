
"""
Breadth First Search (BFS) Traversal
Author: Dev Jain
Roll No: IC2K23-21
"""

from collections import deque


# Graph representation using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def breadth_first_search(network, start):

    visited = set()
    queue = deque([start])

    while queue:

        current_node = queue.popleft()

        if current_node not in visited:

            print(current_node, end=" ")
            visited.add(current_node)

            # Visit all connected nodes
            for neighbour in network[current_node]:

                if neighbour not in visited:
                    queue.append(neighbour)


print("BREADTH FIRST SEARCH")
print("-" * 35)

breadth_first_search(graph, 'A')
print()
