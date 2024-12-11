

def dfs(arr, target, idx, curr):
    if idx == len(arr):
        if target == curr:
            return True
        else:
            return False
    possOne = dfs(arr, target, idx+1, curr+arr[idx])
    possTwo = dfs(arr, target, idx+1, curr*arr[idx])
    possThree = dfs(arr, target, idx+1, int(str(curr)+str(arr[idx])))
    
    if possOne or possTwo or possThree:
        return True
    return False

def sum_total_valid():
    ans = 0
    with open("input.txt", 'r') as f:
        for line in f:
            arr = line.strip().split()
            arr[0] = arr[0][:-1]
            arr = list(map(int, arr))

            target = arr[0]
            arr = arr[1:]
            if dfs(arr, target, 0, 0):
                ans += target
    return ans

print(sum_total_valid())