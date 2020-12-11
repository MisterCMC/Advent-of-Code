from sys import argv
script, input_file = argv
import numpy as np

in_file = open(input_file).read()
list = in_file.split('\n')
x = len(list)
y = len(list[0])

data = np.zeros((x, y))
for i in range(0, x):
    for j in range(0, y):
        if list[i][j] == '.':
            data[i][j] = 0
        elif list[i][j] == 'L':
            data[i][j] = 1

def check_direction(dir, x, y, data):
    if dir == 0:
        iis = 0
        js = 1
    elif dir == 1:
        iis = 1
        js = 1
    elif dir == 2:
        iis = 1
        js = 0
    elif dir == 3:
        iis = 1
        js = -1
    elif dir == 4:
        iis = 0
        js = -1
    elif dir == 5:
        iis = -1
        js = -1
    elif dir == 6:
        iis = -1
        js = 0
    elif dir == 7:
        iis = -1
        js = 1
    while True:
        x = x + js
        y = y + iis
        if x < 0 or x >= 91:
            return 0
        if y < 0 or y >= 98:
            return 0
        if data[x][y] == 0:
            continue
        if data[x][y] == 1:
            return 0
        if data[x][y] == 10:
            return 1


print(data)
round = 0
occupied = False
old_score = 0
score = 0
while True:
    if score == old_score and round > 0:
        print(score)
        break
    old_score = score
    score = 0
    round = round + 1
    old_data = data.copy()
    for i in range(0, x):
        for j in range(0, y):
            if old_data[i][j] == 0:
                continue
            elif old_data[i][j] == 1:
                occupied = False
            elif old_data[i][j] == 10:
                occupied = True

            total = 0
            for k in range(0, 8):
                add = check_direction(k, i, j, old_data)
                total = total + add

            if total == 0 and occupied == False:
                data[i][j] = 10
            elif total < 5 and occupied == True:
                data[i][j] = 10
            elif total >= 5 and occupied == True:
                data[i][j] = 1
            elif total > 0 and occupied == False:
                data[i][j] = 1
    for i in range(0, x):
        for j in range(0, y):
            if data[i][j] == 10:
                score = score + 1
    print(data)

