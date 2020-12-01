from sys import argv
script, input = argv
import numpy as np

#create data list
input_file = open(input).read()
data_str = input_file.split('\n')
data = []
for i in range(0, len(data_str)-1):
    data.append(int(data_str[i]))

for i in range(0, len(data)-1):
    for j in range(0, len(data)-1):
        if data[i] + data[j] == 2020:
            print(data[i] * data[j])
            quit()
