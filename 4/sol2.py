dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
targets = ['SAM', 'MAS']

'''
This function counts the number of horizontal, backwards, and two diagonals XMAS
occurrences starting at r, c in the grid. XMAS can be spelled backwards.
'''
def is_x_mas(grid, r, c):
    if r <= 0 or r >= len(grid) - 1 or c <= 0 or c >= len(grid[0]) - 1:
        return False
    str1 = grid[r-1][c-1]+grid[r][c]+grid[r+1][c+1]
    str2 = grid[r-1][c+1]+grid[r][c]+grid[r+1][c-1]
    if str1 in targets and str2 in targets:
        return True
    return False

def find_x_mas():    
    grid = []
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            grid.append([let for let in line.strip()])
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'A' and is_x_mas(grid, i, j):
                cnt += 1
    return cnt

print(find_x_mas())
    