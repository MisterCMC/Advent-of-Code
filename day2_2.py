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
    first = policy[0]
    second = policy[1]
    if policy[2] == password[int(first)]:
        score = score + 1
    if policy[2] == password[int(second)]:
        score = score + 1
    if score == 1:
        total = total + 1

print(total)

# import data
