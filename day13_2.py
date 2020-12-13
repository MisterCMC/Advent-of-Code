from sys import argv
script, input_file = argv
import queue

in_file = open(input_file).readlines()
full_data = in_file[1].split(',')
data = []
target = int(in_file[0])
rel = [None] * 9
for id in full_data:
    if id != 'x':
        data.append(int(id))
    else:
        data.append(0)

dict = {}
j = 0
for i in range(0, len(data)):
    if data[i] != 0:
        rel[j] = data[i]
        j = j + 1

dict[19] = -19
dict[41] = -10
dict[521] = 0
dict[23] = 8
dict[17] = 17
dict[29] = 29
dict[523] = 31
dict[37] = 37
dict[13] = 44

prod1 = 180567659
prod2 = 6411457

i = 0
while True:
    i = i + prod1
    target = i + 31
    if target % prod2 == 0:
        print(i-19)
        break


