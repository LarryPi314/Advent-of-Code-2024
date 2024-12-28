def run_binary():
    regA, regB, regC = 0, 0, 0
    instructions = []
    output = []
    with open('input.txt', 'r') as f:
        regA = int(f.readline().strip().split()[-1])
        regB = int(f.readline().strip().split()[-1])
        regC = int(f.readline().strip().split()[-1])
        f.readline()
        instructions = f.readline().strip().split(' ')[-1].split(',')

    ptr = 0
    while ptr < len(instructions):
        # print(ptr)
        instr = instructions[ptr]
        input = instructions[ptr + 1]
        input_combo = 0
        if int(input) < 4:
            input_combo = int(input)
        elif int(input) == 4:
            input_combo = regA
        elif int(input) == 5:
            input_combo = regB
        elif int(input) == 6:
            input_combo = regC

        if instr == '0':
            regA = regA // (2 ** input_combo)
        elif instr == '1':
            regB = regB ^ int(input)
        elif instr == '2':
            regB = input_combo % 8
        elif instr == '3':
            if regA != 0:
                ptr = int(input)*2
                continue
        elif instr == '4':
            regB = regB ^ regC
        elif instr == '5':
            output.append(input_combo % 8)
        elif instr == '6':
            regB = regA // (2 ** input_combo)
        elif instr == '7':
            regC = regA // (2 ** input_combo)
        ptr += 2

    return ','.join([str(x) for x in output])

print(run_binary())