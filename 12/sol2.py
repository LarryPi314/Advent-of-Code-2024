
import queue

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

vis = set()
def bfs(grid, pos):
    global vis
    q = queue.Queue()
    q.put((pos[0], pos[1]))
    vis.add(pos)
    area = 0
    vertix_cnt = 0
    while q.qsize() > 0:
        r, c = q.get()
        area += 1
        # at a given tile in the area, this code calculates how many vertices border the tile. 
        # it adds these vertices to the set vertices, where a vertice's position is calculated
        # by the formula (2r, 2c), (2r, 2c+2), etc...

        # northwest corner:
        bool1, bool2 = False, False # edge case 1
        if r == 0:
            bool1 = True
        else:
            bool1 = grid[r-1][c] != grid[pos[0]][pos[1]]
        if c == 0:
            bool2 = True
        else:
            bool2 = grid[r][c-1] != grid[pos[0]][pos[1]]

        if r-1>=0 and c-1>=0 and grid[r-1][c] == grid[pos[0]][pos[1]] and grid[r][c-1] == grid[pos[0]][pos[1]]\
        and grid[r-1][c-1] != grid[pos[0]][pos[1]]:
            vertix_cnt += 1
        elif bool1 and bool2:
            vertix_cnt += 1

        # northeast corner:
        bool1, bool2 = False, False
        if r == 0:
            bool1 = True
        else:
            bool1 = grid[r-1][c] != grid[pos[0]][pos[1]]
        if c == len(grid[0])-1:
            bool2 = True
        else:
            bool2 = grid[r][c+1] != grid[pos[0]][pos[1]]
        
        if r-1>=0 and c+1<len(grid[0]) and grid[r-1][c] == grid[pos[0]][pos[1]] and grid[r][c+1] == grid[pos[0]][pos[1]]\
        and grid[r-1][c+1] != grid[pos[0]][pos[1]]:
            vertix_cnt += 1
        elif bool1 and bool2:
            vertix_cnt += 1
        
        # southwest corner:
        bool1, bool2 = False, False
        if r == len(grid)-1:
            bool1 = True
        else:
            bool1 = grid[r+1][c] != grid[pos[0]][pos[1]]
        if c == 0:
            bool2 = True
        else:
            bool2 = grid[r][c-1] != grid[pos[0]][pos[1]]
        if r+1<len(grid) and c-1>=0 and grid[r+1][c] == grid[pos[0]][pos[1]] and grid[r][c-1] == grid[pos[0]][pos[1]]\
        and grid[r+1][c-1] != grid[pos[0]][pos[1]]:
            vertix_cnt += 1
        elif bool1 and bool2:
            vertix_cnt += 1

        # southeast corner:
        bool1, bool2 = False, False
        if r == len(grid)-1:
            bool1 = True
        else:
            bool1 = grid[r+1][c] != grid[pos[0]][pos[1]]
        if c == len(grid[0])-1:
            bool2 = True
        else:
            bool2 = grid[r][c+1] != grid[pos[0]][pos[1]]

        if r+1<len(grid) and c+1<len(grid[0]) and grid[r+1][c] == grid[pos[0]][pos[1]] and grid[r][c+1] == grid[pos[0]][pos[1]]\
        and grid[r+1][c+1] != grid[pos[0]][pos[1]]:
            vertix_cnt += 1
        elif bool1 and bool2:
            vertix_cnt += 1

        for i in range(4):
            if r+dr[i]>=0 and r+dr[i]<len(grid) and c+dc[i]>=0 and c+dc[i]<len(grid[0])\
            and (r+dr[i], c+dc[i]) not in vis and  grid[r+dr[i]][c+dc[i]] == grid[pos[0]][pos[1]]:
                q.put((r+dr[i], c+dc[i]))
                vis.add((r+dr[i], c+dc[i]))

    return area*vertix_cnt
        



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