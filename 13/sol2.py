
'''
Numpy mixed integer precision is not to be trusted whoops. 
'''
# def not_int(data):
#     if abs(data[0]-int(data[0])) > 0.00000001 or abs(data[1]-int(data[1])) > 0.00000001:
#         return True
#     return False

# def min_moves(buttonA, buttonB, prize):
#     LHS = np.array([[buttonA[0], buttonB[0]], [buttonA[1], buttonB[1]]])
#     RHS = np.array([prize[0], prize[1]])
#     det = np.linalg.det(LHS)
#     if det == 0:
#         return -1
#     inv = np.linalg.inv(LHS)
#     ans = np.dot(inv, RHS)
#     if ans[0] < 0 or ans[1] < 0 or not_int(ans):
#         return -1
#     return int(ans[0])*3 + int(ans[1])

def min_moves(buttonA, buttonB, prize):
    A_x, A_y = buttonA
    B_x, B_y = buttonB
    P_x, P_y = prize

    # Calculate the determinant
    det = A_x * B_y - A_y * B_x

    if det == 0:
        # No unique solution exists
        return -1

    # Calculate determinants for a and b using Cramer's Rule
    a_num = P_x * B_y - P_y * B_x
    b_num = A_x * P_y - A_y * P_x

    # Check if a_num and b_num are divisible by det
    if det < 0:
        # Ensure determinant is positive for consistency
        det = -det
        a_num = -a_num
        b_num = -b_num

    if a_num % det != 0 or b_num % det != 0:
        # Solutions are not integers
        return -1

    a = a_num // det
    b = b_num // det

    # Check if a and b are non-negative
    if a < 0 or b < 0:
        return -1

    # Calculate the total cost
    total_cost = a * 3 + b
    return total_cost

def minimum_moves():
    inp = []
    with open('input.txt', 'r') as f:
        for line in f:
            if line == '\n':
                continue
            inp.append(line.strip().split(' '))
    
    ans = 0
    big = 10000000000000
    for i in range(len(inp)//3):
        buttonA = inp[3*i]
        buttonB = inp[3*i+1]
        prize = inp[3*i+2]
        buttonA = (int(buttonA[2][2:-1]), int(buttonA[3][2:]))
        buttonB = (int(buttonB[2][2:-1]), int(buttonB[3][2:]))
        prize = (int(prize[1][2:-1])+big, int(prize[2][2:])+big)
        temp = min_moves(buttonA, buttonB, prize)
        if temp != -1:
            ans += temp
    return ans

print(minimum_moves())