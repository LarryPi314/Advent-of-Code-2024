def blink_twentyfive():
    stones = []
    with open('sample_input.txt', 'r') as f:
        line = f.readline().strip()
        stones = line.split(' ')
        stones = list(map(int, stones))
    
    for i in range(20):
        a = 0
        print(i, len(stones))
        while a < len(stones):
            stone = stones[a]
            str_stone = str(stone)
            if len(str_stone) % 2 == 0:
                stones.insert(a+1, int(str_stone[len(str_stone)//2:]))
                stones[a] = int(str_stone[:len(str_stone)//2])
                a += 1
            elif stone == 0:
                stones[a] = 1
            else:
                stones[a] = stone*2024
            a += 1
    
    return len(stones)

print(blink_twentyfive())
print()
print(f"2023: {len(str(2023))}, 2023^2: {len(str(2023**2))}, 2023^3: {len(str(2023**3))}, 2023^4: {len(str(2023**4))}, 2023^5: {len(str(2023**5))}")
print(f"2023^6: {len(str(2023**6))}, 2023^7: {len(str(2023**7))}, 2023^8: {len(str(2023**8))}, 2023^9: {len(str(2023**9))}, 2023^10: {len(str(2023**10))}")

a, b = 2, 3
nums = [4, 5, 9, 13, 22, 31, 42, 68]
for num in nums:
    a = a+b
    c = b
    b = a
    a = c
    print(num-b)
