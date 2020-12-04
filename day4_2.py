from sys import argv
script, input_file = argv

in_file = open(input_file).read()
full_data = in_file.split('\n\n')

def validation(data):
    dict = {}
    for item in data:
        dict[item[0:3]] = item[4:]
    byr = birth(dict['byr'])
    iyr = issue(dict['iyr'])
    eyr = expiration(dict['eyr'])
    hgt = height(dict['hgt'])
    hcl = hair(dict['hcl'])
    ecl = eye(dict['ecl'])
    pid = passport(dict['pid'])
    sum = byr + iyr + eyr + hgt + hcl + ecl + pid
    if sum == 0:
        return 1
    else:
        return 0

def birth(byr):
    if int(byr) >= 1920 and int(byr) <= 2002:
        return 0
    else:
        return 1

def issue(iyr):
    if int(iyr) >= 2010 and int(iyr)<= 2020:
        return 0
    else:
        return 1

def expiration(eyr):
    if int(eyr) >= 2020 and int(eyr)<= 2030:
        return 0
    else:
        return 1

def height(hgt):
    if hgt[-1] == 'n':
        height = int(hgt[0:2])
        if height >= 59 and height <= 76:
            return 0
        else:
            return 1
    elif hgt[-1] == 'm':
        if len(hgt) == 4:
            return 1
        height = int(hgt[0:3])
        if height >= 150 and height <= 193:
            return 0
        else:
            return 1
    else:
        return 1

def hair(hcl):
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    if hcl[0] != '#':
        return 1
    if len(hcl) != 7:
        return 1
    for i in range(1, len(hcl)):
        if hcl[i] not in hex:
            return 1
    return 0

def eye(ecl):
    colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if ecl not in colours:
        return 1
    else:
        return 0

def passport(pid):
    if len(pid) == 9:
        return 0
    else:
        return 1

criteria = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
score = 0
for item in full_data:
    outcome = True
    for thing in criteria:
        if thing not in item:
            outcome = False

    if outcome == True:
        i = item.replace('\n', ' ')
        data = i.split(' ')
        score = score + validation(data)



print(score)


#pid (Passport ID) - a nine-digit number, including leading zeroes.
