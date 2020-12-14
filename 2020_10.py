import math
def strips(s):
    return s.strip()

# f = open("input.txt")
f = open("test.txt")
# f = open("test2.txt")

dat = list(map(int, f.readlines()))
# dat = list(map(strips, f.readlines()))
# dat = f.read().strip()

dat.sort()
dat.append(max(dat)+3)

jolt = 0
ones = 0
twos = 0
threes = 0
for i in dat:
    if i-jolt <= 3:
        if i-jolt == 1:
            ones += 1
        elif i-jolt == 2:
            twos += 1
        elif i-jolt == 3:
            threes += 1
        jolt = i
    else:
        break

print(ones)
print(twos)
print(threes)
print(ones * threes)



count = {}
count[0] = 1

for i in dat:
    count[i] = 0

for i in list(count.keys()):
    for j in range(1,4):
        if i + j in count:
            count[i+j] += count[i]

print(count[max(count.keys())])


len_run = 0
i = 0
mult = [1,2,4,7,13]
count = 1
while i < len(dat)-len_run:
    len_run = 0
    j = 1
    while i + j < len(dat) and dat[i+j] == dat[i] + j:
        len_run += 1
        j += 1
    print(len_run)
    count *= mult[len_run]
    i += j


print(count)
