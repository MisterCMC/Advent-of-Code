from sys import argv
script, input_file = argv

in_file = open(input_file).read()
data_str = in_file.split('\n')
data_unsorted = [0]
for item in data_str:
    data_unsorted.append(int(item))

data = sorted(data_unsorted)
final = data[-1] + 3
data.append(final)
difference = []
ones = 0
threes = 0
for i in range(0, len(data)-1):
    current = data[i+1] - data[i]
    difference.append(current)
    if current == 1:
        ones = ones + 1
    elif current == 3:
        threes = threes + 1

score = [ones * threes]
print(score)


