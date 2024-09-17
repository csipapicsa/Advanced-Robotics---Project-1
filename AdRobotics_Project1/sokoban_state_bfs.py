#TODO read state from file

#INITIAL STATE (game state)
maze = [[0, 0, 0, 0, 0, 0], # [y][x] where y is the row and x is the column
        [0, 1, 1, 1, 1, 0], # top left is (0, 0)
        [0, 1, 1, 1, 1, 0], # 0 is walls, 1 is free space
        [0, 1, 1, 1, 1, 0], 
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]
        ] 

robot_pos = (1, 1) # (y, x)
robot_direction = "RIGHT" # can be "UP", "DOWN", "LEFT", "RIGHT"

can_pos = (3, 2) # can be multiple cans
goal_pos = (1, 1) # can be multiple goals

def print_maze(maze, robot_pos, can_pos, goal_pos): # print game state, for testing
        for y in range(len(maze)):
                for x in range(len(maze[0])):
                        if (y, x) == robot_pos:
                                print("R", end=" ")
                        elif (y, x) == can_pos:
                                print("C", end=" ")
                        elif (y, x) == goal_pos:
                                print("G", end=" ")
                        elif maze[y][x] == 0:
                                print("X", end=" ")
                        else:
                                print(" ", end=" ")
                print()

class Node:
    def __init__(self, robot_pos, robot_direction, can_pos):
        self.robot_pos = robot_pos
        self.robot_direction = robot_direction
        self.can_pos = can_pos
        self.parent = None

root = Node(robot_pos, robot_direction, can_pos)

#SEARCH LISTS
states_openlist = [root] #starts with initial state
states_closedlist = set() #starts empty and contains visited states

#ACTIONS (game state)
def move_forward(maze, game_node): 
        if game_node.robot_direction == "UP":
                if maze[game_node.robot_pos[0] - 1][game_node.robot_pos[1]] == 1:
                        new_robot_pos = (game_node.robot_pos[0] - 1, game_node.robot_pos[1])
                        if game_node.robot_pos == game_node.can_pos:
                                new_can_pos = (game_node.can_pos[0] - 1, game_node.can_pos[1])
                        else:
                                new_can_pos = game_node.can_pos
                        new_robot_direction = "UP"
                else:
                        return None
        elif game_node.robot_direction == "DOWN":
                if maze[game_node.robot_pos[0] + 1][game_node.robot_pos[1]] == 1:
                        new_robot_pos = (game_node.robot_pos[0] + 1, game_node.robot_pos[1])
                        if game_node.robot_pos == game_node.can_pos:
                                new_can_pos = (game_node.can_pos[0] + 1, game_node.can_pos[1])
                        else:
                                new_can_pos = game_node.can_pos
                        new_robot_direction = "DOWN"
                else:
                        return None
        elif game_node.robot_direction == "LEFT":
                if maze[game_node.robot_pos[0]][game_node.robot_pos[1] - 1] == 1:
                        new_robot_pos = (game_node.robot_pos[0], game_node.robot_pos[1] - 1)
                        if game_node.robot_pos == game_node.can_pos:
                                new_can_pos = (game_node.can_pos[0], game_node.can_pos[1] - 1)
                        else:
                                new_can_pos = game_node.can_pos
                        new_robot_direction = "LEFT"
                else:
                        return None
        elif game_node.robot_direction == "RIGHT":
                if maze[game_node.robot_pos[0]][game_node.robot_pos[1] + 1] == 1:
                        new_robot_pos = (game_node.robot_pos[0], game_node.robot_pos[1] + 1)
                        if game_node.robot_pos == game_node.can_pos:
                                new_can_pos = (game_node.can_pos[0], game_node.can_pos[1] + 1)
                        else:
                                new_can_pos = game_node.can_pos
                        new_robot_direction = "RIGHT"
                else:
                        return None
        new_node = Node(new_robot_pos, new_robot_direction, new_can_pos)
        new_node.parent = game_node
        return new_node

def move_backward(maze, game_node): 
        if game_node.robot_direction == "UP":
                if maze[game_node.robot_pos[0] + 1][game_node.robot_pos[1]] == 1:
                        new_robot_pos = (game_node.robot_pos[0] + 1, game_node.robot_pos[1])
                        new_robot_direction = "DOWN"
                        if new_robot_pos == game_node.can_pos:
                                return None
                else:
                        return None
        elif game_node.robot_direction == "DOWN":
                if maze[game_node.robot_pos[0] - 1][game_node.robot_pos[1]] == 1:
                        new_robot_pos = (game_node.robot_pos[0] - 1, game_node.robot_pos[1])
                        new_robot_direction = "UP"
                        if new_robot_pos == game_node.can_pos:
                                return None
                else:
                        return None
        elif game_node.robot_direction == "LEFT":
                if maze[game_node.robot_pos[0]][game_node.robot_pos[1] + 1] == 1:
                        new_robot_pos = (game_node.robot_pos[0], game_node.robot_pos[1] + 1)
                        new_robot_direction = "RIGHT"
                        if new_robot_pos == game_node.can_pos:
                                return None
                else:
                        return None
        elif game_node.robot_direction == "RIGHT":
                if maze[game_node.robot_pos[0]][game_node.robot_pos[1] - 1] == 1:
                        new_robot_pos = (game_node.robot_pos[0], game_node.robot_pos[1] - 1)
                        new_robot_direction = "LEFT"
                        if new_robot_pos == game_node.can_pos:
                                return None
                else:
                        return None
        new_node = Node(new_robot_pos, new_robot_direction, game_node.can_pos)
        new_node.parent = game_node
        return new_node
    
def move_left(maze, game_node): 
        if game_node.robot_direction == "UP":
                if maze[game_node.robot_pos[0]][game_node.robot_pos[1] - 1] == 1:
                        new_robot_pos = (game_node.robot_pos[0], game_node.robot_pos[1] - 1)
                        new_robot_direction = "LEFT"
                        if game_node.robot_pos == game_node.can_pos:
                                return None
                else:
                        return None
        elif game_node.robot_direction == "DOWN":
                if maze[game_node.robot_pos[0]][game_node.robot_pos[1] + 1] == 1:
                        new_robot_pos = (game_node.robot_pos[0], game_node.robot_pos[1] + 1)
                        new_robot_direction = "RIGHT"
                        if game_node.robot_pos == game_node.can_pos:
                                return None
                else:
                        return None
        elif game_node.robot_direction == "LEFT":
                if maze[game_node.robot_pos[0] + 1][game_node.robot_pos[1]] == 1:
                        new_robot_pos = (game_node.robot_pos[0] + 1, game_node.robot_pos[1])
                        new_robot_direction = "DOWN"
                        if game_node.robot_pos == game_node.can_pos:
                                return None
                else:
                        return None
        elif game_node.robot_direction == "RIGHT":
                if maze[game_node.robot_pos[0] - 1][game_node.robot_pos[1]] == 1:
                        new_robot_pos = (game_node.robot_pos[0] - 1, game_node.robot_pos[1])
                        new_robot_direction = "UP"
                        if game_node.robot_pos == game_node.can_pos:
                                return None
                else:
                        return None
        new_node = Node(new_robot_pos, new_robot_direction, game_node.can_pos)
        new_node.parent = game_node
        return new_node
    
def move_right(maze, game_node): 
        if game_node.robot_direction == "UP":
                if maze[game_node.robot_pos[0]][game_node.robot_pos[1] + 1] == 1:
                        new_robot_pos = (game_node.robot_pos[0], game_node.robot_pos[1] + 1)
                        new_robot_direction = "RIGHT"
                        if game_node.robot_pos == game_node.can_pos:
                                return None
                else:
                        return None
        elif game_node.robot_direction == "DOWN":
                if maze[game_node.robot_pos[0]][game_node.robot_pos[1] - 1] == 1:
                        new_robot_pos = (game_node.robot_pos[0], game_node.robot_pos[1] - 1)
                        new_robot_direction = "LEFT"
                        if game_node.robot_pos == game_node.can_pos:
                                return None
                else:
                        return None
        elif game_node.robot_direction == "LEFT":
                if maze[game_node.robot_pos[0] - 1][game_node.robot_pos[1]] == 1:
                        new_robot_pos = (game_node.robot_pos[0] - 1, game_node.robot_pos[1])
                        new_robot_direction = "UP"
                        if game_node.robot_pos == game_node.can_pos:
                                return None
                else:
                        return None
        elif game_node.robot_direction == "RIGHT":
                if maze[game_node.robot_pos[0] + 1][game_node.robot_pos[1]] == 1:
                        new_robot_pos = (game_node.robot_pos[0] + 1, game_node.robot_pos[1])
                        new_robot_direction = "DOWN"
                        if game_node.robot_pos == game_node.can_pos:
                                return None
                else:
                        return None
        new_node = Node(new_robot_pos, new_robot_direction, game_node.can_pos)
        new_node.parent = game_node
        return new_node

def bfs():
    while len(states_openlist) > 0:
        current_node = states_openlist.pop(0)
        states_closedlist.add(current_node)
        if current_node.can_pos == goal_pos:
            return current_node
        else:
            new_node = move_forward(maze, current_node)
            if new_node != None and new_node not in states_openlist and new_node not in states_closedlist:
                states_openlist.append(new_node)
            if current_node.robot_pos == current_node.can_pos:  #given only one can
                new_node = move_backward(maze, current_node)
                if new_node != None and new_node not in states_openlist and new_node not in states_closedlist:
                        states_openlist.append(new_node)
            new_node = move_left(maze, current_node)
            if new_node != None and new_node not in states_openlist and new_node not in states_closedlist:
                states_openlist.append(new_node)
            new_node = move_right(maze, current_node)
            if new_node != None and new_node not in states_openlist and new_node not in states_closedlist:
                states_openlist.append(new_node)
    return None

print("Start state:")
import time
start_time = time.time()

print_maze(maze, root.robot_pos, root.can_pos, goal_pos)
print()
result = bfs()
stop_time = time.time()
if result == None:
        print("No solution found")
else: 
        print("Solution found")
        path = []
        while result != None:
                path.append(result)
                result = result.parent
        path.reverse()
        for node in path:
                print_maze(maze, node.robot_pos, node.can_pos, goal_pos)
                print()
        
        moves = []
        for node in path:
                if node.parent != None:
                        if node.robot_pos[0] - node.parent.robot_pos[0] == 1: #robot moved down in y,x
                                if node.parent.robot_direction == "UP":
                                        moves.append("BACKWARD")
                                elif node.parent.robot_direction == "DOWN":
                                        moves.append("FORWARD")
                                elif node.parent.robot_direction == "LEFT":
                                        moves.append("LEFT")
                                elif node.parent.robot_direction == "RIGHT":
                                        moves.append("RIGHT")
                        elif node.robot_pos[0] - node.parent.robot_pos[0] == -1: #robot moved up in y,x
                                if node.parent.robot_direction == "UP":
                                        moves.append("FORWARD")
                                elif node.parent.robot_direction == "DOWN":
                                        moves.append("BACKWARD")
                                elif node.parent.robot_direction == "LEFT":
                                        moves.append("RIGHT")
                                elif node.parent.robot_direction == "RIGHT":
                                        moves.append("LEFT")
                        elif node.robot_pos[1] - node.parent.robot_pos[1] == 1: #robot moved right in y,x
                                if node.parent.robot_direction == "UP":
                                        moves.append("RIGHT")
                                elif node.parent.robot_direction == "DOWN":
                                        moves.append("LEFT")
                                elif node.parent.robot_direction == "LEFT":
                                        moves.append("BACKWARD")
                                elif node.parent.robot_direction == "RIGHT":
                                        moves.append("FORWARD")
                        elif node.robot_pos[1] - node.parent.robot_pos[1] == -1: #robot moved left in y,x
                                if node.parent.robot_direction == "UP": 
                                        moves.append("LEFT") 
                                elif node.parent.robot_direction == "DOWN":
                                        moves.append("RIGHT")
                                elif node.parent.robot_direction == "LEFT":
                                        moves.append("FORWARD")
                                elif node.parent.robot_direction == "RIGHT":
                                        moves.append("BACKWARD")
        print(moves)
        print("Time: ", stop_time - start_time)