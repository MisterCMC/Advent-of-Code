from sys import argv
script, input_file = argv

in_file = open(input_file).readlines()
full_data = in_file[1].split(',')
data = []
target = int(in_file[0])
for id in full_data:
    if id != 'x':
        data.append(int(id))

closest = 10000
best = 0
for id in data:
    score = target + (id - (target % id))
    if score - target < closest:
        closest = score - target
        best = id * closest

print(best)



