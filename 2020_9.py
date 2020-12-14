def strips(s):
    return s.strip()

f = open("input.txt")
# f = open("test.txt")


dat = list(map(int, f.readlines()))
# dat = list(map(strips, f.readlines()))
# dat = f.read().strip()

preamble = []
for i in range(25):
    preamble.append(dat[i])

preamble.sort()

for i in range(25,len(dat)):

    found = False
    for a in range(i-25,i):
        for b in range(a+1, i):
            if dat[a] + dat[b] == dat[i]:
                # print(str(dat[a]) + " " + str(dat[b]) + " " + str(dat[i]))
                found = True

            if found == True:
                break
        if found == True:
            break

    if found == False:
        print(dat[i])
        break

look = dat[i]

for i in range(len(dat)):
    a = 0
    while sum(dat[i:i+a]) <= look:
        a += 1
        if sum(dat[i:i+a]) == look:
            print(min(dat[i:i+a]) + max(dat[i:i+a]))
            print(dat[i] + dat[i+a])
            exit()
