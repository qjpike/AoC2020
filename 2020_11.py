from copy import deepcopy

def count_adj(field,curr,x_len,y_len):
    count = 0
    left_edge = curr % x_len == 0
    right_edge = curr % x_len == x_len - 1
    bottom = curr + x_len >= len(field)
    top = curr - x_len < 0

    if not left_edge:
        if field[curr-1] == '#':
            count += 1
    if not left_edge and not top:
        if field[curr - x_len - 1] == "#":
            count += 1
    if not left_edge and not bottom:
        if field[curr + x_len - 1] == "#":
            count += 1
    if not right_edge:
        if field[curr+1] == "#":
            count += 1
    if not right_edge and not top:
        if field[curr - x_len + 1] == "#":
            count += 1
    if not top:
        if field[curr - x_len] == "#":
            count += 1
    if not bottom:
        if field[curr + x_len] == "#":
            count += 1
    if not bottom and not right_edge:
        if field[curr + x_len + 1] == "#":
            count += 1
    return count

def chk_up(field,curr,x_len):
    if curr - x_len >= 0:
        if field[curr - x_len] == "#":
            return True
        elif field[curr - x_len] == "L":
            return False
        else:
            return chk_up(field,curr - x_len,x_len)
    else:
        return False

def chk_dn(field,curr,x_len):
    if curr + x_len < len(field):
        if field[curr + x_len] == "#":
            return True
        elif field[curr + x_len] == "L":
            return False
        else:
            return chk_dn(field,curr + x_len, x_len)
    else:
        return False

def chk_right(field,curr,x_len):
    if (curr + 1)%x_len != 0:
        if field[curr + 1] == "#":
            return True
        elif field[curr + 1 ] == "L":
            return False
        else:
            return chk_right(field,curr+1,x_len)
    else:
        return False

def chk_left(field,curr,x_len):
    if (curr)%x_len != 0:
        if field[curr - 1] == "#":
            return True
        elif field[curr - 1 ] == "L":
            return False
        else:
            return chk_left(field,curr-1,x_len)
    else:
        return False

def chk_up_lft(field,curr,x_len):
    left_edge = curr % x_len == 0
    top = curr - x_len < 0
    if not (top or left_edge):
        if field[curr - x_len - 1] == "#":
            return True
        elif field[curr - x_len - 1] == "L":
            return False
        else:
            return chk_up_lft(field,curr - x_len - 1, x_len)

def chk_up_rht(field,curr,x_len):
    right_edge = curr % x_len == x_len - 1
    top = curr - x_len < 0
    if not (top or right_edge):
        if field[curr - x_len + 1] == "#":
            return True
        elif field[curr - x_len + 1] == "L":
            return False
        else:
            return chk_up_rht(field,curr - x_len + 1, x_len)
    else:
        return False

def chk_dn_lft(field,curr,x_len):
    left_edge = curr % x_len == 0
    bottom = curr + x_len >= len(field)
    if not (bottom or left_edge):
        if field[curr + x_len - 1] == "#":
            return True
        elif field[curr + x_len - 1] == "L":
            return False
        else:
            return chk_dn_lft(field,curr + x_len - 1, x_len)
    else:
        return False

def chk_dn_rht(field,curr,x_len):
    right_edge = curr % x_len == x_len - 1
    bottom = curr + x_len >= len(field)
    if not (bottom or right_edge):
        if field[curr + x_len + 1] == "#":
            return True
        elif field[curr + x_len + 1] == "L":
            return False
        else:
            return chk_dn_rht(field, curr + x_len + 1, x_len)
    else:
        return False

def count_adj_2(field,curr,x_len,y_len):
    count = 0
    if chk_up(field,curr,x_len):
        count += 1
    if chk_dn(field,curr,x_len):
        count += 1
    if chk_right(field,curr,x_len):
        count += 1
    if chk_left(field,curr,x_len):
        count += 1
    if chk_up_lft(field,curr,x_len):
        count += 1
    if chk_up_rht(field,curr,x_len):
        count += 1
    if chk_dn_lft(field,curr,x_len):
        count += 1
    if chk_dn_rht(field,curr,x_len):
        count += 1
    return count

def strips(s):
    return s.strip()

f = open("input.txt")
# f = open("test.txt")
# f = open("test2.txt")


# dat = list(map(int, f.readlines()))
dat = list(map(strips, f.readlines()))
# dat = f.read().strip()

field = []
x_len = len(dat[0])
y_len = len(dat)



for i in dat:
    field += i

countzm1 = 9999999999
while True:
    new_field = deepcopy(field)
    for i in range(len(field)):

        if field[i] !=  ".":
            count = count_adj(field,i,x_len,y_len)
            if field[i] == "L" and count == 0:
                new_field[i] = "#"
            if field[i] == "#" and count >= 4:
                new_field[i] = "L"
    field = new_field
    if field.count("#") == countzm1:
        break
    countzm1 = field.count("#")

print("Part 1:", countzm1)



field = []
for i in dat:
    field += i

while True:
    new_field = deepcopy(field)
    for i in range(len(field)):

        if field[i] !=  ".":
            count = count_adj_2(field,i,x_len,y_len)
            if field[i] == "L" and count == 0:
                new_field[i] = "#"
            if field[i] == "#" and count >= 5:
                new_field[i] = "L"
    field = new_field
    if field.count("#") == countzm1:
        break
    countzm1 = field.count("#")


print("Part 2:", countzm1)
