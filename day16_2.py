from sys import argv
script, input_file = argv

in_file = open(input_file).read()
data = in_file.split('\n')

rules = []
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




tickets = []
for i in range(25, len(data)-1):
    tickets.append(data[i].split(','))

for k in range(0, len(tickets)-1):
    for field in tickets[k]:
        if tickets[k] == None:
            break
        if str(field) in invalid:
            tickets[k] = None
            break

for j in range(0, 20):
    current_field = []
    for i in range(0, len(tickets)):
        if tickets[i] == None:
            continue
        current_field.append(int(tickets[i][j]))
        current_field.sort()
    possible = []
    for i in range(0, 20):
        cur_rules = [int(rules[2*i].split('-')[0]), int(rules[2*i].split('-')[1]), int(rules[2*i+1].split('-')[0]), int(rules[2*i+1].split('-')[1])]
        right = True
        for k in range(0, cur_rules[0]):
            if k in current_field:
                right = False
        for k in range(cur_rules[1]+1, cur_rules[2]):
            if k in current_field:
                right = False
        for k in range(cur_rules[3]+1, 1000):
            if k in current_field:
                right = False
        if right == True:
            possible.append(i)
    print(str(j) + ': ' + str(len(possible)) + ': '+ str(possible))

print(179*157*227*199*223*181)



