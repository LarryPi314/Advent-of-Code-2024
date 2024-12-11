
def in_bounds(pos, n):
    r, c = pos[0], pos[1]
    return r >= 0 and r < n and c >= 0 and c < n

def add_new_obstacle(row, col, grid):
    grid[row][col] = '#'

    vis = set()

    dir = 'U'
    pos = (-1, -1, dir)
    dir_to_delta = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                pos = (i, j, dir)

    vis2 = set()
    while True:
        vis.add(pos)
        vis2.add((pos[0], pos[1]))
        r, c = pos[0], pos[1]
        new_r, new_c = r + dir_to_delta[dir][0], c + dir_to_delta[dir][1]
        if not in_bounds((new_r, new_c), len(grid)):
            break

        if grid[new_r][new_c] == '#':
            new_r, new_c = r, c
            if dir == 'U':
                dir = 'R'
            elif dir == 'R':
                dir = 'D'
            elif dir == 'D':
                dir = 'L'
            else:
                dir = 'U'

        if in_bounds((new_r, new_c), len(grid)):
            pos = (new_r, new_c, dir)
        else:
            break
        if pos in vis:
            grid[row][col] = '.'
            return True


    grid[row][col] = '.'
    return False

def count_places_to_add():
    grid = []
    with open("input.txt", 'r') as f:
        for line in f:
            grid.append(list(line.strip()))
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '#' and grid[i][j] != '^' and add_new_obstacle(i, j, grid):
                ans += 1
    
    return ans

print(count_places_to_add())


    
