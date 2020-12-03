from sys import argv
script, filename = argv

input_file = open(filename).read()
data = input_file.split('\n')

def toboggan(j_change, i_change, data):
    score = 0
    j = 0
    for i in range(0, len(data), i_change):
        if i == 0:
            continue
        if data[i] == '':
            continue
        j = j+j_change
        if j > 30:
            j = j - 31
        if data[i][j] == '#':
            score = score + 1
    return score

one_one = toboggan(1, 1, data)
print(one_one)
three_one = toboggan(3, 1, data)
print(three_one)
five_one = toboggan(5, 1, data)
print(five_one)
seven_one = toboggan(7, 1, data)
print(seven_one)
one_two = toboggan(1, 2, data)
print(one_two)

product = one_one * three_one * five_one * seven_one * one_two
print(product)
