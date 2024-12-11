'''
This "clean" solution makes extensive use of topological sort. 
For every invalid ordering, we find the valid ordering in o(n) time using
a toplogical sorting strategy. This is done by first creating a graph of the
dependencies between the nodes, then finding the leaf nodes in the graph.
We then remove the leaf nodes from the graph and add them to the order.
'''

from collections import defaultdict


def topo_sort(graph, nodes):
    in_degree = defaultdict(int)
    for node, neighbors in graph.items():
        in_degree[node] += 0
        for n in neighbors:
            in_degree[n] += 1
            
    leafs = []
    order = []

    for node, val in in_degree.items():
        if val == 0 and node in nodes:
            leafs.append(node)

    while nodes:
        curr = leafs.pop(0)
        order.append(curr)
        nodes.remove(curr)
        for n in graph[curr]:
            in_degree[n] -= 1
            if in_degree[n] == 0:
                leafs.append(n)
    return order

def count_correct_orders():
    graph_defns = []
    
    ans = 0
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) == 5:
                a, b = line.split('|')
                graph_defns.append((int(a), int(b)))
            elif len(line) != 0:
                order = list(map(int, line.split(',')))
                curr = order[0]

                graph = defaultdict(list)
                for line in graph_defns:
                    a, b = line
                    if a in order and b in order:
                        graph[a].append(b)

                is_valid = True
                for i in range(1, len(order)):
                    if order[i] not in graph[curr]:
                        is_valid = False
                        break
                    curr = order[i]
                
                if not is_valid:
                    order = topo_sort(graph, order)
                    ans += order[len(order)//2]
    return ans

print(count_correct_orders())