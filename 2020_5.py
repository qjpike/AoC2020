


def strips(s):
    return s.strip()

f = open("input.txt")
# f = open("test.txt")


# dat = list(map(int, f.readlines()))
dat = list(map(strips, f.readlines()))
# dat = f.read().strip()

max = 0
seats = []
for i in dat:
    row = [i for i in range(128)]
    col = [i for i in range(8)]
    for j in range(7):
        if i[j] == 'F':
            row = row[:len(row)//2]
        if i[j] == 'B':
            row = row[len(row)//2:]

    for j in range(7,10):
        if i[j] == 'R':
            col = col[len(col)//2:]
        if i[j] == 'L':
            col = col[:len(col)//2]

    if row[0]*8 + col[0] > max:
        max = row[0]*8 + col[0]

    seats += [row[0]*8 + col[0]]

print("Part 1: " + str(max))


seats.sort()
for i in range(len(seats)-1):
    if seats[i] + 1 != seats[i+1]:
        print("Part 2: " + str(seats[i] + 1))