
def rearrange_file():
    original_file = []
    with open("input.txt", "r") as f:
        line = f.readline().strip()
        files = []
        empty_spaces = []

        for i in range(len(line)):
            if i % 2 == 0:
                files.append((len(original_file), len(original_file)+int(line[i])-1))
                for a in range(int(line[i])):
                    original_file.append(str(i//2))
            else:
                empty_spaces.append((len(original_file), len(original_file)+int(line[i])-1))
                for a in range(int(line[i])):
                    original_file.append('.')
                    
    for i in range(len(files)-1, -1, -1):
        for j in range(len(empty_spaces)):
            if files[i][0] <= empty_spaces[j][0]:
                continue

            len_file = files[i][1] - files[i][0] + 1
            len_empty = empty_spaces[j][1] - empty_spaces[j][0] + 1
            if len_file <= len_empty:
                for k in range(files[i][0], files[i][1]+1):
                    original_file[k] = '.'
                for k in range(empty_spaces[j][0], empty_spaces[j][0]+len_file):
                    original_file[k] = str(i)
                files.pop(i)
                if len_file == len_empty:
                    empty_spaces.pop(j)
                else:
                    empty_spaces[j] = (empty_spaces[j][0]+len_file, empty_spaces[j][1])

                break

    ans = 0
    for i in range(len(original_file)):
        if original_file[i] != '.':
            ans += i*int(original_file[i])
    return ans

print(rearrange_file()) 
                
