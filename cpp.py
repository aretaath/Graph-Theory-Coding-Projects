import networkx as nx
from itertools import combinations

# Input function for reading the problem
def read_input():
    n = int(input())  # number of nodes
    e = int(input())  # number of edges
    edges = []
    for _ in range(e):
        edge_data = list(map(int, input().split()))
        edges.append(edge_data)
    start_node = int(input())  # starting node
    return n, e, edges, start_node

# Function to find odd-degree nodes in the graph
def find_odd_degree_nodes(G):
    return [v for v, degree in G.degree() if degree % 2 == 1]

# Function to find the minimum cost of pairing odd-degree nodes
def minimum_cost_matching(G, odd_nodes):
    odd_pairs = list(combinations(odd_nodes, 2))
    # Find shortest paths between all odd pairs
    odd_pair_costs = {(u, v): nx.shortest_path_length(G, u, v, weight='weight') for u, v in odd_pairs}
    # Find minimum cost perfect matching using a simple greedy approach
    min_matching = []
    visited = set()
    for u, v in sorted(odd_pair_costs, key=odd_pair_costs.get):
        if u not in visited and v not in visited:
            min_matching.append((u, v, odd_pair_costs[(u, v)]))
            visited.add(u)
            visited.add(v)
    return min_matching

# Function to solve the Chinese Postman Problem
def chinese_postman_problem(n, e, edges, start_node):
    # Create graph with given edges
    G = nx.MultiGraph()
    original_edges = []
    
    for edge in edges:
        edge_name, u, v, cost = edge
        # Add edges with both the cost and the name as attributes, and explicitly set the key
        G.add_edge(u, v, key=edge_name, weight=cost, name=edge_name)
        original_edges.append((u, v, edge_name))
        original_edges.append((v, u, edge_name))  # Consider undirected nature of graph

    # Find nodes with odd degree
    odd_degree_nodes = find_odd_degree_nodes(G)
    
    # If there are odd-degree nodes, find the minimum cost matching to make degrees even
    if odd_degree_nodes:
        min_matching = minimum_cost_matching(G, odd_degree_nodes)
        # Add edges to make all nodes even, but don't worry about 'name' for these extra edges
        for u, v, cost in min_matching:
            G.add_edge(u, v, weight=cost)  # no 'name' for extra edges

    # Find Eulerian circuit starting from the specified node
    euler_circuit = list(nx.eulerian_circuit(G, source=start_node, keys=True))

    # Calculate total cost and route
    total_cost = 0
    route = []
    visited_edges = set()

    for u, v, key in euler_circuit:
        edge_tuple = (u, v, key)
        
        # Check if we've already traversed this edge
        if edge_tuple in visited_edges:
            continue
        
        visited_edges.add(edge_tuple)
        total_cost += G[u][v][key]['weight']
        
        # Only append the name if this is an original edge
        if (u, v, key) in original_edges:
            route.append(G[u][v][key]['name'])  # Append the edge name
        
        # In an undirected graph, we should also mark the reverse direction
        visited_edges.add((v, u, key))

    return total_cost, route

# Main code
if __name__ == "__main__":
    # Reading input
    n, e, edges, start_node = read_input()

    # Solving Chinese Postman Problem
    cost, route = chinese_postman_problem(n, e, edges, start_node)

    # Output the result
    print("Cost:", cost)
    print("Route:", ", ".join(map(str, route)))
