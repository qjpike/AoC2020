def strips(a):
    return a.strip()

f = open("input.txt")
# f = open("test.txt")
dat = list(map(strips,f.readlines()))


x_loc = 0
y_loc = 0
dir = 0 # 0,1,2,3 = [E,S,W,N]
for i in dat:
    if i[0] == 'F':
        if dir % 2 == 0:
            x_loc += int(i[1:])*(-1)**(dir//2)
        else:
            y_loc += int(i[1:])*(-1)**((dir+1)//2)
    elif i[0] == 'E':
        x_loc += int(i[1:])
    elif i[0] == 'N':
        y_loc += int(i[1:])
    elif i[0] == 'W':
        x_loc -= int(i[1:])
    elif i[0] == 'S':
        y_loc -= int(i[1])
    elif i[0] == 'R':
        dir += int(i[1:])//90
        dir %= 4
    elif i[0] == 'L':
        dir -= int(i[1:])//90
        dir %= 4


print(abs(x_loc) + abs(y_loc))

x_loc = 0
y_loc = 0
x_loc_wp = 10 #relative to ship's position
y_loc_wp = 1
dir = 0 # 0,1,2,3 = [E,S,W,N]
for i in dat:
    if i[0] == 'F':
        x_loc += x_loc_wp*int(i[1:])
        y_loc += y_loc_wp * int(i[1:])
    elif i[0] == 'E':
        x_loc_wp += int(i[1:])
    elif i[0] == 'N':
        y_loc_wp += int(i[1:])
    elif i[0] == 'W':
        x_loc_wp -= int(i[1:])
    elif i[0] == 'S':
        y_loc_wp -= int(i[1])
    elif i[0] == 'R':
        ''' to set x_pos_wp, y_pos_wp
            if changing 0->1, (y_pos_wp,-x_pos_wp)
            if changing 1->2, (y_pos_wp,-x_pos_wp)
            if changing 2->3, (y_pos_wp,-x_pos_wp)
            if          3->4, (y_pos_wp,-x_pos_wp)'''

        for j in range(int(i[1:])//90):
            tmp = x_loc_wp
            x_loc_wp = y_loc_wp
            y_loc_wp = -tmp

    elif i[0] == 'L':
        for j in range(int(i[1:]) // 90):
            tmp = x_loc_wp
            x_loc_wp = -y_loc_wp
            y_loc_wp = tmp


print(abs(x_loc) + abs(y_loc))