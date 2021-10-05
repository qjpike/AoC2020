import copy

def print_field(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            for k in range(len(field[i][j])):
                print(field[i][j][k], end="")
            print("")
        print("")

def check_surrounds(field,point):
    pl,ro,co = point
    curr = field[pl][ro][co]
    count = -1*field[pl][ro][co].count("#")
    for i in range(-1,2):
        for j in range(-1,2):
            count += field[pl + i][ro + j][co-1:co+2].count("#")
    return count

def check_surrounds_4d(field,point):
    po,pl,ro,co = point
    curr = field[po][pl][ro][co]
    count = -1*field[po][pl][ro][co].count("#")

    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                count += field[po + i][pl + j][ro + k][co-1:co+2].count("#")
    return count


def strips(s):
    return s.strip()

f = open("input.txt")
#f = open("test.txt")
# f = open("test2.txt")

# dat = list(map(int, f.readlines()))
dat = list(map(strips, f.readlines()))
# dat = f.read().strip()

field = []
f = open("input.txt")
# f = open("test.txt")
# f = open("test2.txt")


# dat = list(map(int, f.readlines()))
dat = list(map(strips, f.readlines()))
# dat = f.read().strip()

''' Part 1 '''
threed_field = []
for i in range(40):
    plane = list()
    for j in range(20):
        plane.append(["." for i in range(20)])
    threed_field.append(plane)


start_plane = len(threed_field)//2
start_col = len(plane)//2 - len(dat)//2
start_row = len(plane[0])//2 - len(dat[0])//2

row_delta = 0
for i in dat:
    col_delta = 0
    for j in i:
        threed_field[start_plane][start_row+row_delta][start_col+col_delta] = j
        col_delta += 1
    row_delta += 1

def count_active(field):
    count = 0
    for pl in range(len(field)):
        for co in range(len(field[pl])):
            count += field[pl][co].count("#")
    return count

for i in range(6):
    tmp_field = copy.deepcopy(threed_field)
    for pl in range(1,len(threed_field)-1):
        for ro in range(1,len(threed_field[pl]) - 1):
            for co in range(1,len(threed_field[pl][ro]) - 1):
                surr = check_surrounds(threed_field,(pl,ro,co))
                if threed_field[pl][ro][co] == "#" and not 2 <= surr <=3:
                    tmp_field[pl][ro][co] = "."
                elif threed_field[pl][ro][co] == "." and surr == 3:
                    tmp_field[pl][ro][co] = "#"

    threed_field = tmp_field

print("Part 1: ", count_active(threed_field))



''' Part 2 '''
fourd_field = []
for i in range(20):
    pocket = list()
    for j in range(40):
        plane = list()
        for k in range(20):
            plane.append(["." for i in range(20)])
        pocket.append(plane)
    fourd_field.append(pocket)


start_plane = len(fourd_field[0])//2
start_col = len(plane)//2 - len(dat)//2
start_row = len(plane[0])//2 - len(dat[0])//2
start_pocket = len(fourd_field)//2

row_delta = 0
for i in dat:
    col_delta = 0
    for j in i:
        fourd_field[start_pocket][start_plane][start_row+row_delta][start_col+col_delta] = j
        col_delta += 1
    row_delta += 1

def count_active_4d(field):
    count = 0
    for po in range(len(field)):
        for pl in range(len(field[po])):
            for ro in range(len(field[po][pl])):
                count += field[po][pl][ro].count("#")
    return count

for i in range(6):
    tmp_field = copy.deepcopy(fourd_field)
    for po in range(1,len(fourd_field)-1):
        for pl in range(1,len(fourd_field[po]) - 1):
            for ro in range(1,len(fourd_field[po][pl]) - 1):
                for co in range(1,len(fourd_field[po][pl][ro])-1):
                    surr = check_surrounds_4d(fourd_field,(po,pl,ro,co))
                    if fourd_field[po][pl][ro][co] == "#" and not 2 <= surr <=3:
                        tmp_field[po][pl][ro][co] = "."
                    elif fourd_field[po][pl][ro][co] == "." and surr == 3:
                        tmp_field[po][pl][ro][co] = "#"

    fourd_field = tmp_field

print("Part 2: ", count_active_4d(fourd_field))

