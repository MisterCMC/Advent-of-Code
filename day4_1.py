from sys import argv
script, input_file = argv

in_file = open(input_file).read()
full_data = in_file.split('\n\n')

criteria = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
score = 0
for item in full_data:

    outcome = True
    for thing in criteria:
        if thing not in item:
            outcome = False
    if outcome == True:
        score = score + 1

print(score)
