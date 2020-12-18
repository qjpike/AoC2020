from math import ceil

f = open("input.txt")
dat = f.readlines()

a = [z.strip() for z in dat]
for a in range(dat.__len__()-1):
    for b in range(a,dat.__len__()-1):
        if int(dat[a]) + int(dat[b]) == 2020:
            part1 = int(dat[a]) * int(dat[b])

        for c in range(b,dat.__len__()-1):
            if int(dat[a])+int(dat[b]) +int(dat[c]) == 2020:
                part2 = int(dat[a]) * int(dat[b])*int(dat[c])

print("Part 1:",part1)
print("Part 2:",part2)

#Extra Credit from DM
twos = {}
threes = {}
for i in range(1010):
    twos[(i,2020-i)] = i*(2020-i)
    for j in range(i,ceil(2020/3)):
        if i < 2020/3:
            threes[(i, j, (2020-i-j))] = i*j*(2020-i-j)


intersect = list(set(twos.values()) & set(threes.values()))

twos_key_list = list(twos.keys())
twos_val_list = list(twos.values())

threes_key_list = list(threes.keys())
threes_val_list = list(threes.values())

# for i in range(1,intersect.__len__()):
#     print(str(intersect[i]) +"\t: " +  str(twos_key_list[twos_val_list.index(intersect[i])]) \
#           + " \t " + str(threes_key_list[threes_val_list.index(intersect[i])]))