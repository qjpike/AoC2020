import re

def strips(s):
    return s.strip()

f = open("input.txt")
# f = open("test.txt")


# dat = list(map(int, f.readlines()))
dat = list(map(strips, f.readlines()))
# dat = f.read().strip()

rules = {}
for i in range(len(dat)):
    if dat[i] == "":
        break
    rules[dat[i].split(":")[0]] = dat[i].split(":")[1].strip()

cases = []
for j in range(i+1,len(dat)):
    cases.append(dat[j].strip())

resolved = {}
while "0" not in resolved.keys():
    for i in list(rules.keys()):

        if rules[i].startswith("\""):
            resolved[i] = list(rules[i])[1]
        else:
            parts = rules[i].split(" ")
            complete = True
            for part in parts:
                if part == "|":
                    continue

                if part not in resolved.keys():
                    complete = False

            r = ""
            if complete:
                for part in parts:
                    if part == "|":
                        r += "|"
                    else:
                        r = r + resolved[part]

                resolved[i] = "(" + r + ")"

p1 = 0
for case in cases:
    if re.fullmatch(resolved["0"], case):
        p1 += 1

print("Part 1:", p1)


p2 = set()

rules["8"] = "42 | 42 8" #patch
rules["11"] = "42 31 | 42 11 31"
while True:
    added = False
    for i in list(rules.keys()):
        if rules[i].startswith("\""):
            resolved[i] = list(rules[i])[1]
        else:
            parts = rules[i].split(" ")
            complete = True
            for part in parts:
                if part == "|":
                    continue

                if part not in resolved.keys():
                    complete = False

            r = ""
            if complete:
                for part in parts:
                    if part == "|":
                        r += "|"
                    else:
                        r = r + resolved[part]

                resolved[i] = "(" + r + ")"

    for case in cases:
        if re.fullmatch(resolved["0"], case):
            if case not in p2:
                p2.add(case)
                added = True

    if not added:
        break

print("Part 2:", len(p2))