
def in_bounds(pos, n):
    r, c = pos[0], pos[1]
    return r >= 0 and r < n and c >= 0 and c < n

def count_distinct_locs():
    grid = []
    with open("input.txt", 'r') as f:
        for line in f:
            grid.append(list(line.strip()))
    
    vis = set()
    pos = (-1, -1)
    dir = 'U'
    dir_to_delta = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                pos = (i, j)

    while True:
        vis.add(pos)
        r, c = pos[0], pos[1]
        new_r, new_c = r + dir_to_delta[dir][0], c + dir_to_delta[dir][1]
        if not in_bounds((new_r, new_c), len(grid)):
            break

        if grid[new_r][new_c] == '#':
            new_r, new_c = r, c
            print(f"turn at {r}, {c}")
            if dir == 'U':
                dir = 'R'
            elif dir == 'R':
                dir = 'D'
            elif dir == 'D':
                dir = 'L'
            else:
                dir = 'U'

        if in_bounds((new_r, new_c), len(grid)):
            pos = (new_r, new_c)
        else:
            break

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) in vis:
                print('X', end ='')
            else:
                print(grid[i][j], end='')
        print()
    return len(vis)


print(count_distinct_locs())


    
