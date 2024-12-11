
def bfs(pos, grid):
    n, m = len(grid), len(grid[0])
    q = [(pos[0], pos[1], 0)]
    vis = set()
    while q:
        r, c, dist = q.pop(0)
        if dist == 9:
            vis.add((r, c, dist))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == dist+1:
                q.append((nr, nc, dist + 1))
    return len(vis)
    

def sum_trailheads():
    grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            grid.append(list(map(int, list(line.strip()))))
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                ans += bfs((i, j), grid)
    return ans

print(sum_trailheads())
