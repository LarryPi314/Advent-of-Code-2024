def print_robots(robot_locs):
    for i in range(103):
        for j in range(101):
            if (j, i) in robot_locs:
                print('X', end='')
            else:
                print('.', end='')
        print()


def safety_factor():
    robots = []
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip().split(' ')
            pos = line[0].split(',')
            vel = line[1].split(',')

            p0, p1, v0, v1 = int(pos[0][2:]), int(pos[1]), int(vel[0][2:]), int(vel[1])
            pos = (p0, p1)
            vel = (v0, v1)
            robots.append([pos[0], pos[1], vel[0], vel[1]])
    
    for i in range(10000):
        
        robot_locs = set()
        for robot in robots:
            robot_locs.add((robot[0], robot[1]))
        print("SHREK", i)
        print_robots(robot_locs)
        print()
        print()
        for robot in robots:
            robot[0] += robot[2]
            robot[0] %= 101
            robot[1] += robot[3]
            robot[1] %= 103
    
print(safety_factor())