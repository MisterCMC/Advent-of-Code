from sys import argv
script, input_file = argv

input_data = open(input_file).read()
input_list = input_data.split('\n')
data_list =[]
for item in input_list:
    data_list.append(item.split(':'))

total = 0
for i in range(0, len(data_list)-1):
    password = data_list[i][1]
    policy_str = data_list[i][0].replace('-', ' ')
    policy = policy_str.split(' ')

    score = 0
    for character in password:
        if policy[2] == character:
            score = score + 1
    if score >= int(policy[0]) and score <= int(policy[1]):
        total = total + 1

print(total)

# import data
