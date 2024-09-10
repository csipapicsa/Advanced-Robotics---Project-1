from collections import deque

# Define the directions in which the player can move
DIRECTIONS = [
    (0, -1),  # left
    (0, 1),   # right
    (-1, 0),  # up
    (1, 0),   # down
]

# Function to find the player start position
def find_start_position(board):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == '@':
                return x, y

# Function to check if the move is valid
def is_valid_move(board, player_pos, direction):
    x, y = player_pos
    dx, dy = direction
    target_x, target_y = x + dx, y + dy
    if board[target_y][target_x] in (' ', '.'):
        return True
    elif board[target_y][target_x] in ('$'):
        # Check if the can can be pushed
        beyond_x, beyond_y = target_x + dx, target_y + dy
        if board[beyond_y][beyond_x] in (' ', '.'):
            return True
    return False

# Function to make a move
def make_move(board, player_pos, direction):
    x, y = player_pos
    dx, dy = direction
    target_x, target_y = x + dx, y + dy
    
    # Copy the board to avoid modifying the original
    new_board = [list(row) for row in board]
    
    # Move the player
    if new_board[target_y][target_x] in (' ', '.'):
        new_board[y][x], new_board[target_y][target_x] = ' ', '@'
    elif new_board[target_y][target_x] in ('$'):
        # Move the can
        beyond_x, beyond_y = target_x + dx, target_y + dy
        new_board[y][x], new_board[target_y][target_x], new_board[beyond_y][beyond_x] = ' ', '@', '$'
        if board[beyond_y][beyond_x] == '.':
            new_board[beyond_y][beyond_x] = '*'
    
    return new_board, (target_x, target_y)

# Function to check if the puzzle is solved
def is_solved(board):
    for row in board:
        for cell in row:
            if cell == '$':
                return False
    return True

# Breadth-First Search Solver
def bfs_solver(board):
    start_pos = find_start_position(board)
    queue = deque([(board, start_pos, [])])
    visited = set()
    
    while queue:
        current_board, player_pos, path = queue.popleft()
        
        if is_solved(current_board):
            return path
        
        for direction in DIRECTIONS:
            if is_valid_move(current_board, player_pos, direction):
                new_board, new_pos = make_move(current_board, player_pos, direction)
                new_board_tuple = tuple(tuple(row) for row in new_board)
                
                if new_board_tuple not in visited:
                    visited.add(new_board_tuple)
                    queue.append((new_board, new_pos, path + [direction]))
    
    return None

# Example board
board = [
    "XXXXXXXXX",
    "X@ X     X",
    "X.X$X X X",
    "X       X",
    "X X$X X X",
    "X .   X X",
    "X X X X X",
    "X*      X",
    "XXXXXXXXX"
]

# Convert the board to a list of lists
board = [list(row) for row in board]

# Solve the puzzle
solution = bfs_solver(board)

# Output the solution
if solution:
    direction_names = {
        (0, -1): "Left",
        (0, 1): "Right",
        (-1, 0): "Up",
        (1, 0): "Down"
    }
    print("Solution found!")
    for move in solution:
        print(direction_names[move])
else:
    print("No solution found.")
