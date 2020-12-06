from sys import argv
script, input_file = argv

in_file = open(input_file).read()
data = filter(None, in_file.split('\n'))

all_id = []
for i in range(1, 1024):
    all_id.append(i)

for item in data:
    bin = []
    for i in item:
        if i == 'B' or i == 'R':
            bin.append(1)
        else:
            bin.append(0)

    score = int("".join(map(str, bin)), 2)

    if score in all_id:
        print(score)
        all_id.remove(score)
print(all_id)
