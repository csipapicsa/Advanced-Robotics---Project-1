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
    queue = deque([(start, [])])
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    while queue:
        (x, y), path = queue.popleft()
        
        """
        # dont show the can's path
        if (x, y) == end:
            return path
        """
        
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

    # Combine paths
    full_path = path_to_can + path_to_goal[1:]  # Exclude the first step of path_to_goal as it's the same as the last step of path_to_can

    return full_path


path = solve_maze(maze, robot_start_pos, cans_start_pos, goal_start_pos)
print(path)