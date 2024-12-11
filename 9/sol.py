
def rearrange_file():
    original_file = []
    with open("input.txt", "r") as f:
        line = f.readline().strip()
        for i in range(len(line)):
            if i % 2 == 0:
                for a in range(int(line[i])):
                    original_file.append(str(i//2))
            else:
                for a in range(int(line[i])):
                    original_file.append('.')

    pt1, pt2 = 0, len(original_file)-1
    for i in range(len(original_file)):
        if original_file[i] == '.':
            pt1 = i
            break
    for i in range(len(original_file)-1, -1, -1):
        if original_file[i] != '.':
            pt2 = i
            break
    
    while pt1 < pt2:
        if original_file[pt1] != '.':
            pt1 += 1
            continue
        if original_file[pt2] == '.':
            pt2 -= 1
            continue

        original_file[pt1] = original_file[pt2]
        original_file[pt2] = '.'
        pt1 += 1
        pt2 -= 1
    ans = 0
    for i in range(len(original_file)):
        if original_file[i] != '.':
            ans += i*int(original_file[i])
    return ans

print(rearrange_file()) 
                
