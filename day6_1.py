from sys import argv
script, input_file = argv

in_file = open(input_file).read()
data = in_file.split('\n\n')

total = 0
for group in data:
    answers = []
    for character in group:
        if character in answers:
            continue
        if character == '\n':
            continue
        answers.append(character)
    print(answers)
    total = total + len(answers)
print(total)
