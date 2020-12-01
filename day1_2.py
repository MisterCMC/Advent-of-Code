from sys import argv
script, input = argv
import numpy as np

#create data list
input_file = open(input).read()
data_str = input_file.split('\n')
data = []
for i in range(0, len(data_str)-1):
    data.append(int(data_str[i]))

#create score matrix for two numbers
matrix = np.zeros( (len(data)-1, len(data)-1))
for i in range(0, len(data)-1):
    for j in range(0, len(data)-1):
        matrix[i][j] = data[i] + data[j]

# find third value
for i in range(0, len(data)-1):
    for j in range(0, len(data)-1):
        score = 2020 - matrix[i][j]
        if score < 0:
            continue
        elif score > 0:
            for k in range(0, len(data)-1):
                if score - data[k] == 0:
                    result = data[i] * data[j] * data[k]
                    print(result)
                    quit()
