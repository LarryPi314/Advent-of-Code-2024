from collections import defaultdict

def in_bounds(pos, n):
    r, c = pos[0], pos[1]
    return r >= 0 and r < n and c >= 0 and c < n

def add_antinodes(pos1, pos2, n, vis):
    dr = pos1[0]-pos2[0]
    dc = pos1[1]-pos2[1]
    for i in range(-n, n):
        if(in_bounds((pos1[0]+dr*i, pos1[1]+dc*i), n)):
            vis.add((pos1[0]+dr*i, pos1[1]+dc*i))

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
                    add_antinodes(one, two, len(grid), vis)

    return len(vis)

print(count_antinodes())


    