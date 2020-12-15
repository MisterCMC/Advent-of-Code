from sys import argv
script, input_file = argv

in_file = open(input_file).read()
data = in_file.split(',')

recent = 0
pos = {}

for i in range(0, len(data)):
    pos[int(data[i])] = i

for i in range(7, 29999999):
    if i % 100000 == 0:
        print(i)
    if recent not in pos:
        pos[recent] = i
        recent = 0
        continue
    elif recent in pos:
        score = i - pos[recent]
        pos[recent] = i
        recent = score
        continue

print(recent)
