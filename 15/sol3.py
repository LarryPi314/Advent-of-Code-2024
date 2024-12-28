def transform_line(line):
    """Transform a single line of the original map into the scaled-up version."""
    new_line = []
    for ch in line:
        if ch == '#':
            new_line.append('##')
        elif ch == 'O':
            new_line.append('[]')
        elif ch == '.':
            new_line.append('..')
        elif ch == '@':
            new_line.append('@.')
        else:
            # Unrecognized character (shouldn't happen in the puzzle input)
            new_line.append('..')
    return ''.join(new_line)

def read_input(filename='input.txt'):
    grid = []
    moves = []
    with open(filename, 'r') as f:
        lines = f.read().split('\n')

    # Separate the map and moves
    # First, find the blank line indicating the start of moves
    blank_index = None
    for i, line in enumerate(lines):
        if line.strip() == '':
            blank_index = i
            break

    # Map lines
    original_map = lines[:blank_index]
    # Moves lines (concatenate ignoring newlines)
    moves_str = ''.join(lines[blank_index+1:]).strip()

    # Transform the original map
    transformed_map = [transform_line(l) for l in original_map]

    return transformed_map, moves_str

def find_robot_and_boxes(grid):
    """Find the robot position and box positions in the transformed grid."""
    robot_pos = None
    boxes = set()
    for r in range(len(grid)):
        line = grid[r]
        # Each cell is 2 chars wide, so step by 2
        for c in range(0, len(line), 2):
            cell = line[c:c+2]
            if cell == '@.':
                robot_pos = (r, c)
            elif cell == '[]':
                boxes.add((r, c))
    return robot_pos, boxes

def in_bounds(r, c, grid):
    return 0 <= r < len(grid) and 0 <= c+1 < len(grid[0])  # c+1 because each cell spans two chars

def cell_at(grid, r, c):
    return grid[r][c:c+2]

def set_cell(grid, r, c, val):
    # val should be a 2-char string
    line = grid[r]
    new_line = line[:c] + val + line[c+2:]
    grid[r] = new_line

def move_delta(move):
    # '^' = up (-1, 0)
    # 'v' = down (+1, 0)
    # '<' = left (0, -2)
    # '>' = right (0, +2)
    if move == '^':
        return -1, 0
    elif move == 'v':
        return 1, 0
    elif move == '<':
        return 0, -2
    elif move == '>':
        return 0, 2
    return 0,0

def try_push(grid, r, c, dr, dc):
    """Try to push the box at (r,c) in direction (dr,dc).
       Returns True if successful, False if blocked."""
    new_r = r + dr
    new_c = c + dc
    if not in_bounds(new_r, new_c, grid):
        return False
    next_cell = cell_at(grid, new_r, new_c)
    if next_cell == '##':  # wall
        return False
    if next_cell == '[]':  # another box, push it
        if not try_push(grid, new_r, new_c, dr, dc):
            return False
        # If successful, move this box
        set_cell(grid, new_r, new_c, '[]')
        set_cell(grid, r, c, '..')
        return True
    else:
        # Empty cell or '@.', we can move into it
        if next_cell == '@.':
            # Robot cell shouldn't be in front of a box, but handle gracefully
            return False
        # Move the box
        set_cell(grid, new_r, new_c, '[]')
        set_cell(grid, r, c, '..')
        return True

def simulate(grid, moves):
    # Find initial positions
    robot_pos, _ = find_robot_and_boxes(grid)
    r, c = robot_pos

    for m in moves:
        dr, dc = move_delta(m)
        nr, nc = r+dr, c+dc
        # Check if next cell is valid
        if not in_bounds(nr, nc, grid):
            # Can't move outside
            continue
        next_cell = cell_at(grid, nr, nc)
        if next_cell == '##':
            # wall, no move
            continue
        elif next_cell == '[]':
            # try push
            if try_push(grid, nr, nc, dr, dc):
                # success, move robot
                set_cell(grid, r, c, '..')
                set_cell(grid, nr, nc, '@.')
                r, c = nr, nc
            else:
                # push failed, no move
                continue
        else:
            # empty or floor
            # Move robot
            set_cell(grid, r, c, '..')
            set_cell(grid, nr, nc, '@.')
            r, c = nr, nc

def compute_gps_sum(grid):
    # After final state, find all boxes and sum GPS coordinates
    total = 0
    for row in range(len(grid)):
        line = grid[row]
        for col in range(len(line)):
            if line[col:col+2] == '[]':
                # Box found at (row, col)
                # GPS = row * 100 + col_of_left_bracket
                total += row * 100 + col
    return total

def main():
    grid = []
    moves = ""
    with open('sample_input3.txt', 'r') as f:
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
    # Simulate the robot moves in the scaled-up warehouse
    simulate(grid, moves)
    # Compute sum of GPS coordinates of all boxes
    ans = compute_gps_sum(grid)
    print(ans)

if __name__ == "__main__":
    main()
