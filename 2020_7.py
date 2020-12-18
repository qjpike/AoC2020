def strips(s):
    return s.strip()

class Rule:
    def __init__(self,line):
        rul = line.split(" contain ")
        i = rul[0].split(" ")
        self.name = i[0] + i[1]
        self.contain = {}
        for i in rul[1].split(","):
            j = i.strip()
            j = j.split(" ")
            if j[1] + j[2] == 'otherbags.':
                self.contain = {}
            else:
                self.contain[j[1]+j[2]] = int(j[0])

    def __eq__(self,other):
        if other == self.name:
            return True

f = open("input.txt")
# f = open("test.txt")


# dat = list(map(int, f.readlines()))
dat = list(map(strips, f.readlines()))
# dat = f.read().strip()

rules = []
for i in dat:
    rules.append(Rule(i))


queue = ['shinygold']
for j in queue:
    for i in rules:
        if j in i.contain:
            if i.name not in queue:
                queue.append(i.name)

print("Part 1:",len(queue)-1)

def get_weight(color):
    w = 0
    for i in rules[rules.index(color)].contain:
        w += rules[rules.index(color)].contain[i]*(1+get_weight(i))
    return w

print("Part 2:", get_weight('shinygold'))


