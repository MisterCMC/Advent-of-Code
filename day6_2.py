from sys import argv
script, input_file = argv

in_file = open(input_file).read()
data = in_file.split('\n\n')

total = 0
for group in data:
    answer = []
    people  = group.split('\n')
    for line in people:
        if line == '':
            people.remove(line)
    for character in people[0]:
        everyone = True
        for i in range(1, len(people)):
            if character not in people[i]:
                everyone = False
        if everyone == True:
            answer.append(character)
    total = total + len(answer)
print(total)
