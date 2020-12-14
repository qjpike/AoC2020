def strips(s):
    return s.strip()

f = open("input.txt")
f = open("test.txt")


# dat = list(map(int, f.readlines()))
dat = list(map(strips, f.readlines()))
# dat = f.read().strip()

x_pos = 0
trees_3 = 0
for i in range(len(dat)):
    if dat[i][x_pos] == "#":
        trees_3 += 1

    x_pos = (x_pos + 3)%len(dat[i])

x_pos = 0
trees_1 = 0
for i in range(len(dat)):
    if dat[i][x_pos] == "#":
        trees_1 += 1

    x_pos = (x_pos + 1)%len(dat[i])

x_pos = 0
trees_5 = 0
for i in range(len(dat)):
    if dat[i][x_pos] == "#":
        trees_5 += 1

    x_pos = (x_pos + 5)%len(dat[i])

x_pos = 0
trees_7 = 0
for i in range(len(dat)):
    if dat[i][x_pos] == "#":
        trees_7 += 1

    x_pos = (x_pos + 7)%len(dat[i])

x_pos = 0
trees1_2 = 0
for i in range(0,len(dat),2):
    if dat[i][x_pos] == "#":
        trees1_2 += 1

    x_pos = (x_pos + 1)%len(dat[i])

print(trees_1)
print(trees_3)
print(trees_5)
print(trees_7)
print(trees1_2)
print(trees_1*trees_3*trees_5*trees_7*trees1_2)