# Possible moves for a knight in chess (8 possible moves)
knight_moves = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

# Function to check if the move is valid
def is_valid_move(x, y, board, n):
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1

# Function to solve the Knight's Tour using backtracking
def solve_knights_tour(board, curr_x, curr_y, move_count, path, n):
    # Base case: If all squares have been visited
    if move_count == n * n:
        return True
    
    # Try all possible knight moves
    for dx, dy in knight_moves:
        next_x, next_y = curr_x + dx, curr_y + dy
        if is_valid_move(next_x, next_y, board, n):
            board[next_x][next_y] = move_count
            path.append((next_x, next_y))  # Append the move to the path
            # Recursively try to complete the tour from the new position
            if solve_knights_tour(board, next_x, next_y, move_count + 1, path, n):
                return True
            # Backtrack: if the move doesn't lead to a solution, undo the move
            board[next_x][next_y] = -1
            path.pop()  # Remove the move from the path
    
    return False

# Function to initiate and print the Knight's Tour solution
def knights_tour(n, start_x, start_y):
    # Initialize the chessboard with -1 (meaning unvisited)
    board = [[-1 for _ in range(n)] for _ in range(n)]
    
    # Track the knight's path in a list of tuples (coordinates)
    path = [(start_x, start_y)]
    
    # Mark the starting position with move number 0
    board[start_x][start_y] = 0
    
    # Start the knight's tour from the initial position
    if solve_knights_tour(board, start_x, start_y, 1, path, n):
        # Print the path taken by the knight as coordinates
        for move in path:
            print(f"{move[0]} {move[1]}")
    else:
        print("No solution exists for the given starting position.")

# Read input
# Input the size of the board and the starting position
n, _ = map(int, input("Enter the board size (e.g., '5 5'): ").split())
start_x, start_y = map(int, input("Enter the starting position (e.g., '2 2'): ").split())

# Call the function with the input values
knights_tour(n, start_x, start_y)

