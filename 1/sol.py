import sys

def total_distance():
    data = []
    with open('input.txt', 'r') as f:
        for line in f:
            data.append(line.strip().split(' '))
    list1 = [int(data[i][0]) for i in range(len(data))]
    list2 = [int(data[i][-1]) for i in range(len(data))]
    list1 = sorted(list1)
    list2 = sorted(list2)
    sum = 0
    for i in range(len(data)):
        sum += abs(list1[i]-list2[i])
    return sum

print(total_distance())