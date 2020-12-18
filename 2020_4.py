import re

def strips(s):
    return s.strip()

def validate_passport(passport):
    if int(passport["byr"]) not in range(1920, 2003):
        return False
    if int(passport["iyr"]) not in range(2010, 2021):
        return False
    if int(passport["eyr"]) not in range(2020, 2031):
        return False
    if passport['hgt'][len(passport['hgt'])-2:] not in ['in', 'cm']:
        return False
    if passport['hgt'][len(passport['hgt'])-2:] == 'cm':
        if int(re.match("[0-9]+",passport['hgt']).group(0)) not in range(150,194):
             return False
    if passport['hgt'][len(passport['hgt'])-2:] == 'in':
        if int(re.match("[0-9]+",passport['hgt']).group(0)) not in range(59,75):
             return False
    if not bool(re.search("#[0-9a-f]{6,6}",passport['hcl'])):
        return False
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if len(passport['pid']) == 9 and bool(re.search("[0-9]",passport['pid'])):
        return True

f = open("input.txt")
# f = open("test.txt")


# dat = list(map(int, f.readlines()))
dat = list(map(strips, f.readlines()))
# dat = f.read().strip()

valid = 0
record_needs = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
record_needs.sort()
end_of_record = False
record_contains = []
for i in dat:

    if i == '' :
        end_of_record = True
    else:
        i = i.split(":")
        for j in range(len(i)-1):
            record_contains.append(i[j][len(i[j])-3:])

    if end_of_record:
        if record_contains.count("cid"):
            record_contains.remove("cid")
        record_contains.sort()
        if record_contains == record_needs:
            valid += 1

        record_contains = []
        end_of_record = False

print("Part 1:", valid)

passport = {}
valid = 0
for i in dat:

    if i == '':
        pass_key_list = list(passport.keys())
        if pass_key_list.__contains__("cid"):
            pass_key_list.remove("cid")
        pass_key_list.sort()
        if pass_key_list == record_needs:
            if validate_passport(passport):
                valid += 1
        passport = {}
    else:
        i = i.split(" ")
        for j in i:
            k = j.split(":")
            passport[k[0]] = k[1]

print("Part 2:", valid)