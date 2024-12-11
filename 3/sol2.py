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

    pattern = re.compile(r'(mul\((\d+),(\d+)\))|(do\(\))|(don\'t\(\))')
    flag = True
    for match in pattern.finditer(line):
        if match.group(4) is not None:
            flag = True
        if match.group(5) is not None:
            flag = False
        if match.group(2) is not None and match.group(3) is not None and flag:
            multiplications.append((int(match.group(2)), int(match.group(3))))
    ans = 0
    for mult in multiplications:
        ans += mult[0]*mult[1]
    return ans

print(compute_multplications())
