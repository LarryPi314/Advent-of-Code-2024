
import queue

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

vis = set()
def bfs(grid, pos):
    global vis
    q = queue.Queue()
    q.put((pos[0], pos[1]))
    vis.add(pos)
    area, perimeter = 0, 0
    while q.qsize() > 0:
        r, c = q.get()
        area += 1
        dper = 0
        for i in range(4):
            if r+dr[i]<0 or r+dr[i]>=len(grid) or c+dc[i]<0 or c+dc[i]>=len(grid[0]) \
            or grid[r+dr[i]][c+dc[i]] != grid[pos[0]][pos[1]]:
                dper += 1
        perimeter += dper
        for i in range(4):
            if r+dr[i]>=0 and r+dr[i]<len(grid) and c+dc[i]>=0 and c+dc[i]<len(grid[0])\
            and (r+dr[i], c+dc[i]) not in vis and  grid[r+dr[i]][c+dc[i]] == grid[pos[0]][pos[1]]:
                q.put((r+dr[i], c+dc[i]))
                vis.add((r+dr[i], c+dc[i]))

    return area*perimeter
        



def calc_price():
    global vis
    grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            grid.append(list(line.strip()))
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in vis:
                ans += bfs(grid, (i, j))
    
    return ans

print(calc_price())
