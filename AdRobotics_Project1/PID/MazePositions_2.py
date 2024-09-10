maze = [[1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
        ]

robot_start_pos = [[2, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    ]


cans_start_pos = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 3, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                ]


goal_start_pos = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 4, 0, 0],
                ]


from collections import deque

def find_position(grid, target):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == target:
                return (i, j)
    return None

def is_valid(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1

def bfs(maze, start, end):
    queue = deque([(start, [start])])  # Include start in the initial path
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    while queue:
        (x, y), path = queue.popleft()
        
        if (x, y) == end:
            return path
        
        if (x, y) not in visited:
            visited.add((x, y))
            
            for dx, dy in directions:
                next_x, next_y = x + dx, y + dy
                if is_valid(next_x, next_y, maze):
                    queue.append(((next_x, next_y), path + [(next_x, next_y)]))
    
    return None  # No path found

def solve_maze(maze, robot_start_pos, cans_start_pos, goal_start_pos):
    robot_pos = find_position(robot_start_pos, 2)
    can_pos = find_position(cans_start_pos, 3)
    goal_pos = find_position(goal_start_pos, 4)

    if not all([robot_pos, can_pos, goal_pos]):
        return None  # One or more positions not found

    # Find path from robot to can
    path_to_can = bfs(maze, robot_pos, can_pos)
    if not path_to_can:
        return None  # No path from robot to can

    # Find path from can to goal
    path_to_goal = bfs(maze, can_pos, goal_pos)
    if not path_to_goal:
        return None  # No path from can to goal

    # Combine paths, ensuring both start and can positions are included
    full_path = path_to_can + path_to_goal[1:]  # Include can_pos from path_to_can, exclude it from path_to_goal

    return full_path


path = solve_maze(maze, robot_start_pos, cans_start_pos, goal_start_pos)
# path to directions

print(path)

# turn the path into a list of directions

def path_to_relative_directions(path):
    directions = []
    current_facing = 'right'  # Assume the robot starts facing right
    direction_mapping = {
        'right': (0, 1),
        'down': (1, 0),
        'left': (0, -1),
        'up': (-1, 0)
    }

    # for i in range(len(path) - 1):
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]

        # Determine the desired direction
        desired_direction = None
        if x1 == x2:
            if y2 > y1:
                desired_direction = 'right'
            else:
                desired_direction = 'left'
        else:
            if x2 > x1:
                desired_direction = 'down'
            else:
                desired_direction = 'up'

        # Determine relative movement based on the current facing direction
        if current_facing == desired_direction:
            directions.append('forward')
        elif (current_facing, desired_direction) in [('right', 'down'), ('down', 'left'), ('left', 'up'), ('up', 'right')]:
            directions.append('right-forward')
            #directions.append('forward')
            current_facing = desired_direction
        elif (current_facing, desired_direction) in [('right', 'up'), ('up', 'left'), ('left', 'down'), ('down', 'right')]:
            directions.append('left-forward')
            #directions.append('forward')
            current_facing = desired_direction
        
        # OH
        
        
        else:
            # Turn 180 degrees if and move
            #
            directions.append("backward")
            # directions.append('left')
            # directions.append('left')
            # directions.append('forward')
            current_facing = desired_direction
        

    return directions
directions = path_to_relative_directions(path)
print(directions)