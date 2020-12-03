from sys import argv
script, filename = argv

input_file = open(filename).read()
data = input_file.split('\n')

score = 0
j = 0
for i in range(1, len(data)-1):
    j = j+3
    if j > 29:
        j = j - 31
    if data[i][j] == '#':
        score = score + 1

print(score)
