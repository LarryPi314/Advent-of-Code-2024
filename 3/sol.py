import re
'''
This function uses a regex to find all occurrences of "mul(a,b)" in the input file
and adds it to a list. 
'''
def compute_multplications():
    multiplications = []
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    line = ''.join(lines)

    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    for match in pattern.finditer(line):
        multiplications.append((int(match.group(1)), int(match.group(2))))

    ans = 0
    for mult in multiplications:
        ans += mult[0]*mult[1]
    return ans

print(compute_multplications())
