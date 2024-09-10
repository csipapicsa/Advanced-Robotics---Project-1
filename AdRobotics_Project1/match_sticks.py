def is_valid_move(state, position):
    return position + 2 < len(state) and state[position] in '|X' and state[position + 1] in '|X' and state[position + 2] in '|X'

def make_move(state, position):
    new_state = state[:position] + ['X', ' ', 'X'] + state[position + 3:]
    return new_state

def is_goal_state(state):
    return state.count('X') == 4 and state.count(' ') == 4

def solve(state):
    if is_goal_state(state):
        return []
    
    for i in range(len(state) - 2):
        if is_valid_move(state, i):
            new_state = make_move(state, i)
            solution = solve(new_state)
            if solution is not None:
                return [i] + solution
    
    return None

def print_state(state):
    print(''.join(state))

# Initial state
initial_state = ['|', '|', '|', '|', '|', '|', '|', '|']

# Solve the puzzle
solution = solve(initial_state)

if solution:
    print("Solution found:")
    current_state = initial_state
    print_state(current_state)
    for move in solution:
        current_state = make_move(current_state, move)
        print_state(current_state)
else:
    print("No solution found.")