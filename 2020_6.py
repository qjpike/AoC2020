def strips(s):
    return s.strip()

f = open("input.txt")
# f = open("test.txt")


# dat = list(map(int, f.readlines()))
dat = list(map(strips, f.readlines()))
# dat = f.read().strip()

end_of_record = False
yess = []
count = 0
for i in dat:
    if i == '':
        end_of_record = True
    else:
        for j in i:
            if j not in yess:
                yess += j

    if end_of_record:
        count += len(yess)
        end_of_record = False
        yess = []

print("Part 1:",count)

yess = {}
party_size = 0
count = 0
for i in dat:
    if i == '':
        end_of_record = True
    else:
        for j in i:
            if j not in yess:
                yess[j] = 1
            else:
                yess[j] += 1
        party_size += 1

    if end_of_record:
        for k in list(yess.keys()):
            if yess[k] == party_size:
                count += 1
        end_of_record = False
        yess = {}
        party_size = 0

print("Part 2:",count)

