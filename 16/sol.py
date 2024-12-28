import heapq

def print_grid(grid, vis):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in vis:
                print('X', end='') 
            else:
                print(grid[i][j], end='')
        print()
    
def solve(grid):
    # Find start (S) and end (E)
    start, end = None, None
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)
            elif cell == 'E':
                end = (i, j)

    # Directions: North, East, South, West
    # (dr, dc) changes for these directions
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # Initial direction is East (1)
    start_dir = 1

    # Initialize dist with a large number
    R, C = len(grid), len(grid[0])
    dist = [[[float('inf')] * 4 for _ in range(C)] for __ in range(R)]
    dist[start[0]][start[1]][start_dir] = 0

    # Priority queue: (cost, row, col, dir)
    pq = [(0, start[0], start[1], start_dir)]
    heapq.heapify(pq)

    while pq:
        cost, r, c, d = heapq.heappop(pq)
        # If this cost is not the best known, skip
        if dist[r][c][d] < cost:
            continue
        # If we reached the end
        if (r, c) == end:
            return cost

        # Consider rotating left
        d_left = (d - 1) % 4
        if cost + 1000 < dist[r][c][d_left]:
            dist[r][c][d_left] = cost + 1000
            heapq.heappush(pq, (cost + 1000, r, c, d_left))

        # Consider rotating right
        d_right = (d + 1) % 4
        if cost + 1000 < dist[r][c][d_right]:
            dist[r][c][d_right] = cost + 1000
            heapq.heappush(pq, (cost + 1000, r, c, d_right))

        # Consider moving forward
        dr, dc = directions[d]
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
            if cost + 1 < dist[nr][nc][d]:
                dist[nr][nc][d] = cost + 1
                heapq.heappush(pq, (cost + 1, nr, nc, d))

    # If we can't reach the end
    return -1


def find_lowest_path():
    grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            grid.append(list(line))

    start, end = (), ()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)
    return solve(grid)

print(find_lowest_path())