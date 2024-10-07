import itertools

def TSP(graph, edges_dict, start):
    # Get all possible permutations of nodes except the starting point
    vertices = list(range(len(graph)))
    vertices.remove(start)
    
    min_cost = float('inf')
    best_path = []

    # Try all possible tours and calculate their costs
    for perm in itertools.permutations(vertices):
        current_cost = 0
        current_path = [start]
        k = start
        
        # Traverse all nodes in the order of the permutation
        for j in perm:
            current_cost += graph[k][j]
            current_path.append(j)
            k = j
        
        # Add the cost to return to the starting point
        current_cost += graph[k][start]
        current_path.append(start)
        
        # If this path is better, update the result
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path

    return min_cost, best_path

def main():
    # Input number of nodes and number of edges
    n = int(input("Enter the number of nodes: "))
    e = int(input("Enter the number of edges: "))
    # Initialize adjacency matrix and edge dictionary
    graph = [[float('inf') for _ in range(n)] for _ in range(n)]
    edges_dict = {}

    # Input edge details and costs
    print("Enter edge details (format: edge_id node1 node2 cost):")
    for _ in range(e):
        edge_id, u, v, cost = map(int, input().split())
        graph[u-1][v-1] = cost
        graph[v-1][u-1] = cost  # Undirected graph
        edges_dict[(u-1, v-1)] = edge_id
        edges_dict[(v-1, u-1)] = edge_id  # For undirected graph

    # Input starting point
    start = int(input("Enter the starting point (node): ")) - 1

    # Call TSP function to calculate minimum cost and path
    min_cost, best_path = TSP(graph, edges_dict, start)

    # Output
    print(f"\nMinimum traveled distance = {min_cost}")
    
    # Generate output route with edge_id
    route_edges = []
    for i in range(len(best_path) - 1):
        u, v = best_path[i], best_path[i + 1]
        route_edges.append(edges_dict[(u, v)])
    
    print(f"Route: {', '.join(map(str, route_edges))}")

if __name__ == "__main__":
    main()