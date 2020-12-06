from sys import argv
script, input_file = argv

in_file = open(input_file).read()
data = filter(None, in_file.split('\n'))

highest = 0
for item in data:
    bin = []
    for i in item:
        if i == 'B' or i == 'R':
            bin.append(1)
        else:
            bin.append(0)

    score = int("".join(map(str, bin)), 2)
    if score > highest:
        highest = score
print(highest)
