def update_pos(grid, move, box_locs, box_loc_map, pos1, pos2, is_box=False):
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
        return False

    new_r_1 = pos1[0] + dr
    new_c_1 = pos1[1] + dc

    new_r_2 = pos2[0] + dr
    new_c_2 = pos2[1] + dc
    # print()
    # print(move, pos1, (new_r_1, new_c_1), pos2, (new_r_2, new_c_2))
    # print()

    if not (0 <= new_r_1 < len(grid) and 0 <= new_c_1 < len(grid[0])):
        return False
    if is_box and not (0 <= new_r_2 < len(grid) and 0 <= new_c_2 < len(grid[0])):
        return False

    if grid[new_r_1][new_c_1] == '#':
        return False    
    if is_box and grid[new_r_2][new_c_2] == '#':
        return False

    if is_box:
        box_locs.remove(pos1)
        box_locs.remove(pos2)
        good1, good2 = False, False
        if (new_r_1, new_c_1) in box_locs:
            pushed = update_pos(grid, move, box_locs, box_loc_map, (new_r_1, new_c_1), box_loc_map[(new_r_1, new_c_1)], is_box=True)
            if pushed:
                good1 = True
            else:
                box_locs.add(pos1)
                box_locs.add(pos2)
                return False
            
        if (new_r_2, new_c_2) in box_locs:
            pushed = update_pos(grid, move, box_locs, box_loc_map, (new_r_2, new_c_2), box_loc_map[(new_r_2, new_c_2)], is_box=True)
            if pushed:
                good2 = True
            else: 
                box_locs.add(pos1)
                box_locs.add(pos2)
                return False
            
        if good1 or good2:
            box_locs.add((new_r_1, new_c_1))
            box_locs.add((new_r_2, new_c_2))
            if pos1 in box_loc_map:
                del box_loc_map[pos1]
            if pos2 in box_loc_map:
                del box_loc_map[pos2]
            box_loc_map[(new_r_1, new_c_1)] = (new_r_2, new_c_2)
            box_loc_map[(new_r_2, new_c_2)] = (new_r_1, new_c_1)
            return True
        else:
            box_locs.add((new_r_1, new_c_1))
            box_locs.add((new_r_2, new_c_2))
            del box_loc_map[pos1]
            del box_loc_map[pos2]
            box_loc_map[(new_r_1, new_c_1)] = (new_r_2, new_c_2)
            box_loc_map[(new_r_2, new_c_2)] = (new_r_1, new_c_1)
            return (new_r_1, new_c_1)

    else:
        if (new_r_1, new_c_1) in box_locs:
            pushed = update_pos(grid, move, box_locs, box_loc_map, (new_r_1, new_c_1), box_loc_map[(new_r_1, new_c_1)], is_box=True)
            if pushed:
                return (new_r_1, new_c_1) 
            else:
                return False
        elif grid[new_r_1][new_c_1] == '#':
            return False
        else:
            return (new_r_1, new_c_1)

def convert_grid(grid):
    new_grid = []
    for i in range(len(grid)):
        curr = []
        for j in range(len(grid[i])):
            if grid[i][j] == 'O':
                curr.append('[')
                curr.append(']')
            elif grid[i][j] == '@':
                curr.append('@')
                curr.append('.')
            else:
                curr.append(grid[i][j])
                curr.append(grid[i][j])
        new_grid.append(curr)

    return new_grid

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

    new_grid = convert_grid(grid)

    grid = new_grid

    box_locs = set()
    
    box_loc_map = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '[':
                box_locs.add((i, j))
                box_locs.add((i, j+1))
                box_loc_map[(i, j)] = (i, j+1)
                box_loc_map[(i, j+1)] = (i, j)
            elif grid[i][j] == '@':
                pos = (i, j)

    # print_grid(grid, box_locs, pos)
    # print(moves)
    for i, move in enumerate(moves):
        new_pos = update_pos(grid, move, box_locs, box_loc_map, pos, (0, 0), is_box = False)
        if new_pos:
            pos = new_pos
    #     print(f"Move {i+1}: {move}")
    #     print_grid(grid, box_locs, pos)
    #     print()
    # print_grid(grid, box_locs, pos)
    ans = 0
    # print_grid(grid, box_locs, pos)
    vis = set()
    for box_loc_1, box_loc_2 in box_loc_map.items():
        if box_loc_2 in vis:
            continue
        # print(box_loc_1)
        minX = min(box_loc_1[0], box_loc_2[0])
        minY = min(box_loc_1[1], box_loc_2[1])
        ans += minX*100+minY
        vis.add(box_loc_1)
    return ans

print(find_locs())