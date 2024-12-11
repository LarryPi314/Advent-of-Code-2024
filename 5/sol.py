from collections import defaultdict

def count_correct_orders():
    graph = defaultdict(list)
    ans = 0
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) == 5:
                a, b = line.split('|')
                graph[int(a)].append(int(b))
            elif len(line) != 0:
                order = list(map(int, line.split(',')))
                curr = order[0]
                is_valid = True
                for i in range(1, len(order)):
                    if order[i] not in graph[curr]:
                        is_valid = False
                        break
                    curr = order[i]
                if is_valid:
                    ans += order[len(order)//2]
    return ans



print(count_correct_orders()) 
