from sys import argv
script, input_file = argv

in_file = open(input_file).read()
commands = in_file.split('\n')

total = 0
completed = []
i = 0
jump = False

while True:
    if i == len(commands):
        print(total)
        break
    print(i)
    if i in completed:
        print(total)
        break
    elif i not in completed:
        completed.append(i)
    instr = commands[i][0:3]
    argu = int(commands[i][4:])
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
