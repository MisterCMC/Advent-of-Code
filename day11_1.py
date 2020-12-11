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
            coordx = np.zeros((3,3))
            coordx[0] = i - 1
            coordx[1] = i
            coordx[2] = i + 1
            coordy = np.zeros((3,3))
            coordy[:,0] = j - 1
            coordy[:,1] = j
            coordy[:,2] = j + 1

            total = 0
            for xx in range(0, 3):
                for yy in range(0, 3):
                    if xx == 1 and yy == 1:
                        continue
                    cx = int(coordx[xx][yy])
                    cy = int(coordy[xx][yy])
                    if cx <= -1 or cx >= 91:
                        continue
                    if cy <= -1 or cy >= 98:
                        continue
                    if old_data[cx][cy] == 0 or old_data[cx][cy] == 1:
                        continue
                    elif old_data[cx][cy] == 10:
                        total = total + 1
                        continue
            if total == 0 and occupied == False:
                data[i][j] = 10
            elif total < 4 and occupied == True:
                data[i][j] = 10
            elif total >= 4 and occupied == True:
                data[i][j] = 1
            elif total > 0 and occupied == False:
                data[i][j] = 1
    for i in range(0, x):
        for j in range(0, y):
            if data[i][j] == 10:
                score = score + 1
    print(data)

