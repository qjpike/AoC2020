def strips(s):
    return s.strip()


f = open("input.txt")
#f = open("test.txt")


# dat = list(map(int, f.readlines()))
dat = list(map(strips, f.readlines()))
# dat = f.read().strip()

import re

count = 0
count2 = 0
for i in dat:
    x = re.findall("[0-9]+",i)
    let = i[i.index(":")-1]
    i = i[i.index(":")+1:].strip()

    dic = {}
    for z in i:
        if z in dic:
            dic[z] += 1
        else:
            dic[z] = 1


    if let in dic and int(x[0]) <= dic[let] <= int(x[1]):
        count += 1

    if i[int(x[0])-1] == let :
        if i[int(x[1])-1] != let:
            count2 += 1
    elif i[int(x[1])-1] == let:
        count2 += 1

print("Part 1:",count)
print("Part 2:",count2)