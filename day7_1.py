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
    for i in range(5, len(words), 4):
        contained = words[i] + words[i+1]
        list.append(contained)
    dict[container] = list

good_bags = []
while True:
    old_score = len(good_bags)
    for rule in data:
        words = rule.split(' ')
        container = words[0] + words[1]
        result = dict[container]
        if 'shinygold' in result and container not in good_bags:
            good_bags.append(container)
            continue
        for bag in result:
            if bag in good_bags and container not in good_bags:
                good_bags.append(container)
    new_score = len(good_bags)
    if new_score - old_score == 0:
        break
print(len(good_bags))
