from collections import defaultdict

def in_bounds(pos, n):
    r, c = pos[0], pos[1]
    return r >= 0 and r < n and c >= 0 and c < n
def count_antinodes():
    grid = []
    vis = set()
    with open('input.txt') as f:
        for line in f:
            grid.append(list(line.strip()))
    
    node_locs = defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '.':
                node_locs[grid[i][j]].append((i, j))
    
    for node, locs in node_locs.items():
        for one in locs:
            for two in locs:
                if one != two:
                    dr = one[0]-two[0]
                    dc = one[1]-two[1]
                    if in_bounds((one[0]+dr, one[1]+dc), len(grid)):
                        vis.add((one[0]+dr, one[1]+dc))
                    if in_bounds((two[0]-dr, two[1]-dc), len(grid)):
                        vis.add((two[0]-dr, two[1]-dc))
    
    return len(vis)

print(count_antinodes())


    