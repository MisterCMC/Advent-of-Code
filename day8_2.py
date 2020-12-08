from sys import argv
script, input_file = argv

in_file = open(input_file).read()
commands = in_file.split('\n')

total = 0
for j in range(0, len(commands)):
    if commands[j][0:3] == 'jmp':
        line = commands[j].replace('jmp', 'nop')
    elif commands[j][0:3] == 'nop':
        line = commands[j].replace('nop', 'jmp')
    else:
        line = commands[j]
    total = 0
    i = 0
    completed = []
    while True:
        if i == len(commands):
            print(total)
            break
        if i in completed:
            break
        elif i not in completed:
            completed.append(i)
        instr = commands[i][0:3]
        argu = int(commands[i][4:])
        if i == j:
            instr = line[0:3]
            argu = int(line[4:])
        if instr == 'acc':
            total = total + argu
            i = i + 1
            continue
        elif instr == 'jmp':
            i = i + argu
            continue
        elif instr == 'nop':
            i = i + 1
            continue
