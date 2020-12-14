from sys import argv
script, input_file = argv
import numpy as np

in_file = open(input_file).read()
data = in_file.split('\n')

memory = {}
for command in data:
    if command[1] == 'a':
        mask = list(command[7:])
        continue
    elif command[1] == 'e':
        mem = command.split(']')
        location = mem[0][4:]
        value = int(mem[1][3:])
        bin_val = list(format(value, '#038b'))

        for i in range(0, len(mask)):
            if mask[i] == 'X':
                continue
            elif mask[i] == '1':
                bin_val[i+2] = '1'
            elif mask[i] == '0':
                bin_val[i+2] = '0'

        value = int(''.join(bin_val), 2)
        memory[location] = value

score = 0
for key in memory:
    score = score + memory[key]

print(score)