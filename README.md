# Graph Theory Coding Projects

---

## Traveling Salesman Problem (TSP)

The TSP finds the optimal route to visit all nodes in a graph exactly once, returning to the starting point with the lowest possible cost. A brute-force approach is used here, calculating all possible route permutations and selecting the one with the minimum cost.

### Functions
- `TSP(graph, edges_dict, start)` will compute the best TSP route.
- `main()` manages input/output and calls the TSP function.

### Example Input
```
Input
3 
4 
0 1 2 10 
1 2 3 5
2 3 1 7 
3 3 1 2 
1
```

- **Number of Nodes and Edges**
  - `n = 3` (number of nodes)
  - `e = 4` (number of edges) 
  The code will use `n` to create an adjacency matrix of size 3x3 and initialize its values to `float('inf')` to indicate that two nodes are not yet connected before costs are provided.

- **Cost Matrix and Edge-Id Dictionary**

  The `graph` is a 3x3 adjacency matrix, initially filled with `float('inf')`, indicating there are no connections between nodes yet. 
  The `edges_dict` is a dictionary that stores pairs of nodes connected by edges and their edge IDs.
  
  As the details of the edges are entered, the program will map the input according to the node index in the array (nodes are counted from 0):
  - **Edge 0**: Node 1 and 2, cost 10 → `graph[0][1] = 10`, `graph[1][0] = 10`, `edges_dict[(0, 1)] = 0`, `edges_dict[(1, 0)] = 0`
  - **Edge 1**: Node 2 and 3, cost 5 → `graph[1][2] = 5`, `graph[2][1] = 5`, `edges_dict[(1, 2)] = 1`, `edges_dict[(2, 1)] = 1`
  - **Edge 2**: Node 3 and 1, cost 7 → `graph[2][0] = 7`, `graph[0][2] = 7`, `edges_dict[(2, 0)] = 2`, `edges_dict[(0, 2)] = 2`
  - **Edge 3**: Node 3 and 1, cost 2 → `graph[2][0] = 2`, `graph[0][2] = 2`, `edges_dict[(2, 0)] = 3`, `edges_dict[(0, 2)] = 3`

- **Starting Node**
  - `start = 0` (because input 1 is converted to array index starting from 0).

### TSP(graph, edges_dict, start) Function
The function `TSP(graph, edges_dict, start)` is called by `main()` with the following parameters:
- `graph = [[inf, 10, 2], [10, inf, 5], [2, 5, inf]]`: The adjacency matrix with travel costs between nodes
- `edges_dict = {(0, 1): 0, (1, 0): 0, (1, 2): 1, (2, 1): 1, (2, 0): 3, (0, 2): 3}`: A dictionary containing pairs of nodes and their edge IDs
- `start = 0`: The starting node (node 1)

The function removes the starting node (0) from the list of nodes to generate all permutations of the remaining nodes. Thus, the possible permutations are (1, 2) and (2, 1).

- Cost Calculation for Each Permutation:
  - **Permutation (1, 2)**:
    - Start from node 0 (start = 0)
    - Cost node 0 to node 1 = 10
    - Cost node 1 to node 2 = 5
    - Cost node 2 to node 0 = 2
    - Total cost = 10 + 5 + 2 = 17

  - **Permutation (2, 1)**:
    - Start from node 0 (start = 0)
    - Cost node 0 to node 2 = 2
    - Cost node 2 to node 1 = 5
    - Cost node 1 to node 0 = 10
    - Total cost = 2 + 5 + 10 = 17

Both routes have a total cost of 17. Therefore, the program selects one, and in this example, we assume the route (1, 2) is the best route.

### Output
- Minimum Cost = 17
- Route based on edge IDs:
  - Node 0 to node 1 (Edge 0)
  - Node 1 to node 2 (Edge 1)
  - Node 2 back to node 0 (Edge 3)

---

## 2. CPP (Chinese Postman Problem)

### Overview

The Chinese Postman Problem (CPP) aims to find the shortest closed path that visits every edge in a graph at least once. This implementation reads graph data, handles odd-degree nodes, constructs an Eulerian circuit, and outputs the total cost and the route.

**Input Example**
```
3 
4 
0 1 2 10 
1 2 3 5
2 3 1 7 
3 3 1 2 
1
```

**Expected Output**
```
Cost: 26
Route: 0, 1, 3, 2, 3
```

### Code Breakdown

- **Input Handling:**
  - First two lines take the number of `nodes (n)` and `edges (e)`.
  - The next `e` lines describe the edges with their cost.
  - The last line gives the start node for the Eulerian circuit.
- **Graph Construction:**
  - `networkx` is used to create a multi-graph `(nx.MultiGraph)`.
  - Each edge is added with its weight (cost) and name (index in the input).
- **Odd-Degree Node Handling:**
  - Nodes with an odd degree are identified.
  - If odd-degree nodes exist, we add extra edges to create an Eulerian graph using a minimum cost matching algorithm between odd-degree nodes.
- **Eulerian Circuit**
  - Once the graph is Eulerian (all nodes have even degree), an Eulerian circuit is computed starting from the specified node.
  - The total cost of the circuit is tracked and append each edge's name to the route.

### Actual Output Result and Possible Causes

However, there's a problem faced during the making of this code. The result of the output is different from the original expected output in the question. Here is the explanation of the possible causes on why the result might differs from the original question.

**Output**
```
Cost: 26
Route: 3, 2, 1, 0
```
- **Non-Unique Eulerian Path:**

The Eulerian circuit generated is not guaranteed to match the expected order because multiple valid solutions exist for CPP.

- **Traversal Logic:**

The route depends on how the algorithm decides to traverse edges. In the current implementation, the algorithm may not prioritize the exact input order of edges.

## 3. The Knight's Tour

### Overview

The **Knight's Tour** problem involves finding a path on a chessboard where the knight visits every square exactly once. The knight starts from a given square, and it must use its unique L-shaped moves to cover all squares without revisiting any.
The goal is to find such a path, and if it exists, output the sequence of moves that the knight takes. This is typically solved using **backtracking** or **brute-force** techniques.

### Example Input
```
Input
5 5
2 2
```

This input means:
1. **5 5**: The chessboard size is 5x5.
2. **2 2**: The knight starts at position (2, 2) on the board (indexing starts from 0).

### Knight's Moves

In chess, the knight moves in an L-shape: it can move either two squares in one direction and one square perpendicular, or one square in one direction and two squares perpendicular. From any square `(x, y)`, there are up to **8 possible moves** the knight can make:
1. `(x+2, y+1)`
2. `(x+2, y-1)`
3. `(x-2, y+1)`
4. `(x-2, y-1)`
5. `(x+1, y+2)`
6. `(x+1, y-2)`
7. `(x-1, y+2)`
8. `(x-1, y-2)`

### Initialization

The chessboard is initialized with all squares marked as **unvisited** (often with `-1` in code), except for the knight's starting square, which is marked with the move number `0` (indicating it's the first move).

In this case:
- The knight starts at `(2, 2)`, so the board looks like this initially:
```
-1  -1  -1  -1  -1
-1  -1  -1  -1  -1
-1  -1   0  -1  -1
-1  -1  -1  -1  -1
-1  -1  -1  -1  -1
```
Here, `0` represents the starting point.

### Knight's Tour Process

The **Knight's Tour algorithm** works by recursively trying to move the knight to unvisited squares. The idea is to keep moving the knight from square to square, marking each square as visited with an increasing move number, until all 25 squares on the board have been visited. If a dead-end is reached (i.e., no valid moves are left), the algorithm backtracks and tries a different path.

### Brute-Force Approach

The brute-force approach for solving the Knight's Tour involves the following steps:

1. **Start from (2, 2)**: Mark this square as visited and set it as `0` (first move).
2. **Try all 8 possible knight moves** from (2, 2):
   - For each valid move (i.e., a move that stays within the board and lands on an unvisited square), move the knight and mark the square with the next move number (`1`, `2`, etc.).
   - If a move doesn't work (leads to a dead-end), backtrack by unmarking the square and trying a different move.
3. **Continue until the knight visits all squares on the board**.

### Output

Once a complete valid path is found, the sequence of moves is output as coordinates, showing the order in which the knight visits each square. In this example, let's assume the knight completes the tour successfully.

### Example Output

For the given starting point `(2, 2)`, here is a possible output (the exact sequence may vary):

```
Output
2 2
4 1
2 0
0 1
1 3
3 4
4 2
3 0
1 1
0 3
2 4
4 3
3 1
1 0
0 2
1 4
3 3
2 1
4 0
3 2
4 4
2 3
0 4
1 2
0 0
```

### Explanation of Moves

Each line in the output represents a square on the board that the knight visits, in the order the squares are visited. Here's a breakdown:

1. **Start at (2, 2)**.
2. From there, the knight moves to (4, 1), making its L-shaped move.
3. The knight then moves to (2, 0), and so on.

This path continues until all squares have been visited.

### Visualization of the Final Chessboard
In this 5x5 board, each number represents the order in which the knight visited the square:

```
24   3  14  19  22
 9  12   1   6  17
 2   0  25   5  16
23  11   4  18   7
10  13   8  21  20
```

