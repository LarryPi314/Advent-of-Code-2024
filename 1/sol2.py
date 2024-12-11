from collections import defaultdict

def sim_score():
    data = []
    with open('input.txt', 'r') as f:
        for line in f:
            data.append(line.strip().split(' '))
    list1 = [int(data[i][0]) for i in range(len(data))]
    list2 = [int(data[i][-1]) for i in range(len(data))]

    list2_freqs = defaultdict(int)
    for i in list2:
        list2_freqs[i] += 1

    sum = 0
    for i in list1:
        if i in list2_freqs:
            sum += i*list2_freqs[i]
    return sum

print(sim_score())