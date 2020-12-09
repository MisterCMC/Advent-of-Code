from sys import argv
import numpy as np
script, input = argv

in_file = open(input).read()
data_str = in_file.split('\n')

data = []
for item in data_str:
    data.append(int(item))

preamble = []
for i in range(0, 25):
    preamble.append(data[i])

sums = np.zeros( (25, 25) )
for i in range(25, len(data)):
    for ii in range(0, 25):
        for jj in range(0, 25):
            sums[ii][jj] = preamble[ii] + preamble[jj]
    if data[i] not in sums:
        print(data[i])
        break
    preamble.append(data[i])
    preamble.pop(0)

