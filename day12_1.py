from sys import argv
script, input_file = argv
import math

in_file = open(input_file).read()
instructions = in_file.split('\n')

bns = 0
bew = 0
ang = 0
for item in instructions:
    action = item[0]
    value = int(item[1:])
    if action == 'N':
        ns = ns + value
    elif action == 'S':
        ns = ns - value
    elif action == 'E':
        ew = ew + value
    elif action == 'W':
        ew = ew - value
    elif action == 'L':
        ang = ang + value
    elif action == 'R':
        ang = ang - value
    elif action == 'F':
        rad = ang * (math.pi/180)
        ns = ns + (value * math.sin(rad))
        ew = ew + (value * math.cos(rad))
print(abs(ns) + abs(ew))