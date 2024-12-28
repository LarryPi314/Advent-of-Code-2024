

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
    for i in range(100):
        for robot in robots:
            robot[0] += robot[2]
            robot[0] %= 101
            robot[1] += robot[3]
            robot[1] %= 103
    q1, q2, q3, q4 = 0, 0, 0, 0
    for robot in robots:
        if robot[0] == 50 or robot[1] == 51:
            continue
        elif robot[0] < 50 and robot[1] < 51:
            q1 += 1
        elif robot[0] > 50 and robot[1] < 51:
            q2 += 1
        elif robot[0] < 50 and robot[1] > 51:
            q3 += 1
        elif robot[0] > 50 and robot[1] > 51:
            q4 += 1
    print(q1, q2, q3, q4)
    return q1*q2*q3*q4

print(safety_factor())