from sys import argv
script, input_file = argv
import math

in_file = open(input_file).read()
instructions = in_file.split('\n')

bns = 0
bew = 0
wns = 1
wew = 10
new_wew = wew
new_wns = wns
for item in instructions:
    action = item[0]
    value = int(item[1:])
    if action == 'N':
        new_wns = wns + value

    elif action == 'S':
        new_wns = wns - value

    elif action == 'E':
        new_wew = wew + value

    elif action == 'W':
        new_wew = wew - value

    elif action == 'L':
        if value == 180:
            new_wns = -wns
            new_wew = -wew
        elif value == 90:
            new_wew = -wns
            new_wns = wew
        elif value == 270:
            new_wew = wns
            new_wns = -wew
    elif action == 'R':
        if value == 180:
            new_wns = -wns
            new_wew = -wew
        elif value == 90:
            new_wew = wns
            new_wns = -wew
        elif value == 270:
            new_wew = -wns
            new_wns = wew
    elif action == 'F':
        bns = bns + (value * wns)
        bew = bew + (value * wew)
    wew = new_wew
    wns = new_wns

    print('')
    print(str(bew) + ', ' + str(bns))
    print(str(wew) + ', ' + str(wns))
print(abs(bns) + abs(bew))