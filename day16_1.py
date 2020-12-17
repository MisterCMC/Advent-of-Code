from sys import argv
script, input_file = argv

in_file = open(input_file).read()
data = in_file.split('\n')

rules = []
numbers = []
for i in range(0, 20):
    for j in range(0, len(data[i])):
        if data[i][j] == '-':
            rules.append(data[i][j-3:j+4])



invalid = []
for k in range(0, 1000):
    invalid.append(str(k))

for rule in rules:
    numbers = rule.split('-')
    start = int(numbers[0])
    end = int(numbers[1])
    for k in range(start, end+1):
        if str(k) in invalid:
            invalid[k] = 0


score = 0
for i in range(25, len(data)):
    line = data[i].split(',')
    print(line)
    for field in line:
        if str(field) in invalid:
            score = score + int(field)
print(score)