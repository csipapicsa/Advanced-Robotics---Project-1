#TODO read state from file

#INITIAL STATE (game state)
maze = [[1, 1, 1, 1, 1, 1, 1], # [y][x] where y is the row and x is the column
        [1, 0, 1, 0, 1, 0, 1], # top left is (0, 0)
        [1, 1, 1, 1, 1, 1, 1], # 0 is empty space, 1 is line
        [1, 0, 1, 0, 1, 0, 1], # the cans can only start on y and x values equals to 0, 2, 4, 6
        [1, 1, 1, 1, 1, 1, 1], 
        [1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
        ] 

robot_pos = (0, 0) # (y, x)
robot_direction = "RIGHT" # can be "UP", "DOWN", "LEFT", "RIGHT"

can_pos = (4, 2) # can be multiple cans
goal_pos = (6, 2) # can be multiple goals

def print_maze(maze, robot_pos, can_pos, goal_pos): # print game state, for testing
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if robot_pos == [y, x]:
                print("R", end="")
            elif can_pos == [y, x]:
                print("C", end="")
            elif goal_pos == [y, x]:
                print("G", end="")
            elif maze[y][x] == 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()

#print_maze(maze, robot_pos, can_pos, goal_pos)

#the only change in game state is the robot position, direction and can position
#the goal position is fixed
#SEARCH LISTS
states_openlist = [(robot_pos, robot_direction, can_pos)] #starts with initial state
states_closedlist = [] #starts empty and contains visited states

#ACTIONS (game state)
def move_forward(maze, robot_pos, robot_direction): # example of action (0, 0) -> (0, 2)
        y, x = robot_pos
        if robot_direction == "UP":
                if maze[y-1][x] == 1:
                        if can_pos == (y-1, x):
                                if maze[y-2][x] == 1:
                                        new_can_pos = (y-2, x)
                                        new_robot_pos = (y-1, x)
                                        states_openlist.append((new_robot_pos, robot_direction, new_can_pos))
                        else:
                                new_robot_pos = (y-1, x)
                                states_openlist.append((new_robot_pos, robot_direction, can_pos))
        elif robot_direction == "DOWN":
                if maze[y+1][x] == 0:
                        return (y+1, x)
        elif robot_direction == "LEFT":
                if maze[y][x-1] == 0:
                        return (y, x-1)
        elif robot_direction == "RIGHT":
                if maze[y][x+1] == 0:
                        return (y, x+1)

def move_backward(maze, robot_pos, robot_direction): 
    
def move_left(maze, robot_pos, robot_direction):
    
def move_right(maze, robot_pos, robot_direction): # (0, 0) -> (2, 0)


#BFS on game states

