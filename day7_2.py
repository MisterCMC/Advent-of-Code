from sys import argv
script, input_file = argv

in_file = open(input_file).read()
data = in_file.split('\n')

dict = {}
dict['otherbags.'] = None
for rule in data:
    words = rule.split(' ')
    container = words[0] + words[1]
    list = []
    for i in range(4, len(words), 4):
        contained = words[i] + words[i+1] + words[i + 2]
        list.append(contained)
    dict[container] = list

key = 'shinygold'

bag_count = {}
while True:
    old_score = len(bag_count)
    for rule in data:
        words = rule.split(' ')
        container = words[0] + words[1]
        result = dict[container]
        score = 1
        if result[0] == 'nootherbags.':
            bag_count[container] = score
            continue
        all = True
        for bag in result:

            if bag[1:] in bag_count:
                multiplier = int(bag[0])
                score = score + multiplier * int(bag_count[bag[1:]])
            else:
                all = False
                break
        if all == False:
            continue
        elif all == True:
            bag_count[container] = score
    new_score = len(bag_count)
    if new_score - old_score == 0:
        break

print(bag_count['shinygold']-1)


