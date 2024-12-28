memo = {}

def dp(stone, n):
    if (stone, n) in memo:
        return memo[(stone, n)]
    if n == 0:
        memo[(stone, n)] = 1
        return memo[(stone, n)]
    
    if stone == 0:
        memo[(stone, n)] = dp(1, n-1)
    elif len(str(stone)) % 2 == 0:
        memo[(stone, n)] = dp(int(str(stone)[:len(str(stone))//2]), n-1) + dp(int(str(stone)[len(str(stone))//2:]), n-1)
    else:
        memo[(stone, n)] = dp(stone*2024, n-1)

    return memo[(stone, n)]



def blink_twentyfive():
    stones = []
    with open('input.txt', 'r') as f:
        line = f.readline().strip()
        stones = line.split(' ')
        stones = list(map(int, stones))
    ans = 0
    for stone in stones:
        ans += dp(stone, 75)
    
    return ans

print(blink_twentyfive())

