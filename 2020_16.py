import copy

def strips(s):
    return s.strip()

f = open("input_16.txt")
# f = open("test.txt")
# f = open("test2.
# txt")


# dat = list(map(int, f.readlines()))
dat = list(map(strips, f.readlines()))
# dat = f.read().strip()

class Rule():
    def __init__(self,dat):
        txt = dat.split(":")
        self.name = txt[0]
        self.r1 = txt[1].split(" or ")[0].strip()
        self.r2 = txt[1].split(" or ")[1].strip()
        self.r1_min = int(self.r1.split("-")[0])
        self.r1_max = int(self.r1.split("-")[1])
        self.r2_min = int(self.r2.split("-")[0])
        self.r2_max = int(self.r2.split("-")[1])

    def valid(self,val):
        if self.r1_min <= val <= self.r1_max:
            return True
        if self.r2_min <= val <= self.r2_max:
            return True
        return False

i = 0
rules = []
while dat[i] != '':
    rules.append(Rule(dat[i]))
    i+=1

i += 2

t = dat[i].split(",")
your_tick = []
for k in t:
    your_tick.append(int(k))


i += 3
other_ticks = []
while i < len(dat):
    other_ticks.append(dat[i])
    i += 1

error_count = 0
for i in other_ticks:
    for j in i.split(","):
        valid_count = 0
        for k in rules:
            if k.valid(int(j)):
                valid_count += 1
        if valid_count == 0:
            error_count += int(j)

print("Part 1: ", error_count)


#remove bad tickets
error_count = 0
ot_temp = copy.deepcopy(other_ticks)
for i in ot_temp:
    for j in i.split(","):
        valid_count = 0
        for k in rules:
            if k.valid(int(j)):
                valid_count += 1

        if valid_count == 0:
            other_ticks.remove(i)


#for every ticket, check which rules fit it, eliminating bad ones
rules_len = len(other_ticks[0].split(","))
field = {}
for i in range(rules_len):
    tmp = []
    for j in other_ticks:
        tmp.append(j.split(",")[i])

    field[i] = tmp

alignment = {}
# for each ticket field
for rule in rules:
    for tik_field in range(len(field)):
        valid = True
        for val in field[tik_field]:
            if not rule.valid(int(val)):
                valid = False
                break
        if valid:
            if rule.name not in alignment:
                alignment[rule.name] = [tik_field]
            else:
                alignment[rule.name].append(tik_field)

# This is where I found my answer - I took the alignment dict and figured out the 1:1 alignment by hand
# print(your_tick[2]*your_tick[14]*your_tick[4]*your_tick[16]*your_tick[7]*your_tick[11])

for i in alignment.keys():
    max_l = len(alignment[i])
    for j in alignment.keys():
        if i != j and len(alignment[j]) < max_l:
            alignment[i] = list(set(alignment[i]) - set(alignment[j]))

ans = 1
for i in alignment:
    if "departure" in i:
       ans *= your_tick[alignment[i][0]]
print("Part 2: ", ans)

