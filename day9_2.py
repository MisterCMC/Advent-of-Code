from sys import argv
import numpy as np
script, input = argv

in_file = open(input).read()
data_str = in_file.split('\n')

data = []
for item in data_str:
    data.append(int(item))

invalid = 105950735
for i in range(563, 0, -1):
    sums = 0
    all = []
    while sums < invalid:
        all.append(data[i])
        sums = sums + data[i]
        if sums == invalid:
            highest = 0
            lowest = 100000000000
            for item in all:
                if item > highest:
                    highest = item
                if item < lowest:
                    lowest = item
            print(highest + lowest)
            exit()
        i = i - 1


