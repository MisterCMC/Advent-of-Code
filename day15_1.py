from sys import argv
script, input_file = argv

in_file = open(input_file).read()
data = in_file.split(',')

recent = '0'
while True:
    if recent not in data:
        data.append(recent)
        recent = '0'
    elif recent in data:
        dist = 0
        for i in range(len(data)-1, -1, -1):
            dist = dist + 1
            if data[i] == recent:
                data.append(recent)
                recent = str(dist)
                break
    if len(data)>2030:
        break

print(data[2019])