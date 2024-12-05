dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
target = "XMAS"
'''
BFS Solution doesn't apply to this problem. 
'''
def bfs(grid, r, c):
    cnt = 0
    q = []
    q.append((r, c, 0)) # row, col, distance
    while len(q):
        curr = q.pop(0)
        currR, currC, dist = curr[0], curr[1], curr[2]
        if dist == 3:
            cnt += 1
            continue
        for i in range(8):
            if currR+dy[i] < 0 or currR+dy[i]>=len(grid) \
                or currC+dx[i] < 0 or currC+dx[i]>=len(grid[0]):
                continue
            if target[dist+1] == grid[currR+dy[i]][currC+dx[i]]:
                if currR+dy[i] >= 0 and currR+dy[i]<len(grid) \
                    and currC+dx[i] >= 0 and currC+dx[i]<len(grid[0]):
                        q.append((currR + dy[i], currC + dx[i], dist + 1))
    return cnt

'''
This function counts the number of horizontal, backwards, and two diagonals XMAS
occurrences starting at r, c in the grid. XMAS can be spelled backwards.
'''
def cnt_xmas_given_starting(grid, r, c):
    cnt = 0
    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]
    for i in range(8):
        currR, currC = r, c
        for j in range(4):
            if currR < 0 or currR >= len(grid) or currC < 0 or currC >= len(grid[0]):
                break
            if grid[currR][currC] != target[j]:
                break
            if j == 3:
                cnt += 1
            currR += dy[i]
            currC += dx[i]
    return cnt

def find_xmas():    
    grid = []
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            grid.append([let for let in line.strip()])
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'X':
                cnt += cnt_xmas_given_starting(grid, i, j)
    return cnt

print(find_xmas())
    