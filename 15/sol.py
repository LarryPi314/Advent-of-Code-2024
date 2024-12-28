def update_pos(grid, move, box_locs, pos, is_box=False):
    dr, dc = 0, 0
    if move == '>':
        dr, dc = 0, 1
    elif move == '^':
        dr, dc = -1, 0
    elif move == '<':
        dr, dc = 0, -1
    elif move == 'v':
        dr, dc = 1, 0
    else:
        # Invalid move character
        return False

    new_r = pos[0] + dr
    new_c = pos[1] + dc

    # Check bounds
    if not (0 <= new_r < len(grid) and 0 <= new_c < len(grid[0])):
        return False

    # If moving a box
    if is_box:
        if (new_r, new_c) in box_locs:
            # Attempt to push the next box
            pushed = update_pos(grid, move, box_locs, (new_r, new_c), is_box=True)
            if pushed:
                # Move current box
                box_locs.remove(pos)
                box_locs.add((new_r, new_c))
                return (new_r, new_c)  # New position of the pushed box
            else:
                return False
        elif grid[new_r][new_c] == '#':
            return False
        else:
            # Move the box to the new position
            box_locs.remove(pos)
            box_locs.add((new_r, new_c))
            return (new_r, new_c)
    else:
        if (new_r, new_c) in box_locs:
            # Attempt to push the box
            pushed = update_pos(grid, move, box_locs, (new_r, new_c), is_box=True)
            if pushed:
                return (new_r, new_c)  # New position of the robot after pushing
            else:
                return False
        elif grid[new_r][new_c] == '#':
            return False
        else:
            # Move the robot to the new position
            return (new_r, new_c)


def print_grid(grid, box_locs, pos):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in box_locs:
                print('O', end='')
            elif (i, j) == pos:
                print('@', end='')
            elif grid[i][j] == '#':
                print(grid[i][j], end='')
            else:
                print('.', end='')
        print()
        
def find_locs():
    grid = []
    moves = ""
    with open('input.txt', 'r') as f:
        flag = False
        for line in f:
            line = line.strip()
            if not line:
                flag = True
                continue
            if not flag:
                grid.append(list(line))
            else:
                moves += line

    box_locs = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                box_locs.add((i, j))
            elif grid[i][j] == '@':
                pos = (i, j)

    for move in moves:
        new_pos = update_pos(grid, move, box_locs, pos)
        if new_pos:
            pos = new_pos
        
    ans = 0
    for box_loc in box_locs:
        ans += box_loc[0]*100+box_loc[1]

    return ans

print(find_locs())