# Lab 2 – Search Algorithms in Artificial Intelligence

## Aim
To understand and implement different search algorithms used in Artificial Intelligence.

## Experiments Performed

1. Breadth First Search (BFS)
2. Depth First Search (DFS)
3. Hill Climbing
4. Best First Search
5. A* Search Algorithm

---

## 1. Breadth First Search (BFS)

BFS is an uninformed search algorithm that explores nodes level by level. It uses a Queue (FIFO) data structure to visit nodes.

## 2. Depth First Search (DFS)

DFS is an uninformed search algorithm that explores one branch deeply before backtracking. It uses recursion or a Stack (LIFO) data structure.

## 3. Hill Climbing

Hill Climbing is a heuristic search algorithm that selects a better neighbouring state at each step until no further improvement is possible.

## 4. Best First Search

Best First Search is an informed search algorithm that selects the most promising node based on its heuristic value.

## 5. A* Search Algorithm

A* is an informed search algorithm that finds a least-cost path by considering the actual path cost and estimated remaining cost.

**Formula:**

\[
f(n) = g(n) + h(n)
\]

Where:
- \(f(n)\) = Total estimated cost
- \(g(n)\) = Actual cost from the starting node
- \(h(n)\) = Estimated cost to reach the goal

---

## Results

All five search algorithms were implemented and executed successfully. Their outputs demonstrated different approaches to exploring and finding solutions in a search space.

## Learning Outcomes

1. Understood graph traversal techniques.
2. Learned the difference between BFS and DFS.
3. Understood heuristic-based search algorithms.
4. Implemented Hill Climbing and Best First Search.
5. Learned how A* finds a least-cost path.

## Conclusion

The lab work helped in understanding different uninformed and informed search techniques used in Artificial Intelligence. Practical implementation improved the understanding of graph traversal, heuristic evaluation, and problem-solving strategies.