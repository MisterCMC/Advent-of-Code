from sys import argv
script, input_file = argv
import numpy as np

in_file = open(input_file).read()
data = in_file.split('\n')

def float(loc, count):
    possible = []
    total = pow(2, count)
    form_lang = '#0' + str(count+2)+'b'
    for i in range(0, total):
        loc_cop = loc.copy()
        perm = list(format(i, form_lang))
        num = 2
        for j in range(0, len(loc_cop)):
            if loc_cop[j] != 'X':
                continue
            elif loc_cop[j] == 'X':
                loc_cop[j] = perm[num]
                num = num + 1
        possible.append(''.join(loc_cop))
    return possible


memory = {}
for command in data:
    if command[1] == 'a':
        mask = list(command[7:])
        continue
    elif command[1] == 'e':
        mem = command.split(']')
        val = int(mem[1][3:])
        value = int(mem[0][4:])
        bin_loc = list(format(value, '#038b'))
        num = 0
        for i in range(0, len(mask)):
            if mask[i] == '0':
                continue
            elif mask[i] == '1':
                bin_loc[i+2] = '1'
            elif mask[i] == 'X':
                bin_loc[i+2] = 'X'
                num = num + 1
        possible = float(bin_loc, num)
        for item in possible:
            location_bin = ''.join(item)
            location = int(location_bin, 2)
            memory[location] = val

score = 0
for key in memory:
    score = score + memory[key]


print(score)