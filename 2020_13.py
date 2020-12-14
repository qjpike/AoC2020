import re
import math
# import numpy


def strips(s):
    return s.strip()

f = open("input.txt")
# f = open("test.txt")


# dat = list(map(int, f.readlines()))
dat = list(map(strips, f.readlines()))
# dat = f.read().strip()

best = int(dat[0])
times = dat[1].split(",")
lis = []
for i in times:
    if i != 'x':
        lis.append(int(i))

lis.sort()
wait_min = 9999
bus_id = 0
for i in lis:
    j = 1
    while i*j < best:
        j += 1
    if i*j - best < wait_min:
        wait_min = i*j - best
        bus_id = i

print("Part One: " + str(wait_min * bus_id))

lis_2 = dat[1].split(",")
res = {}
busses = []
j = 0
for i in lis_2:
    res[j] = i
    if re.match("[0-9]+",i):
        busses.append(int(i))

offsets = [lis_2.index(str(a)) for a in busses]

period = 1
strt = 1
for i in range(len(busses)):
    while (strt + offsets[i]) % busses[i] != 0:
        strt += period
    period = period * busses[i]

print("Part Two: " + str(strt))