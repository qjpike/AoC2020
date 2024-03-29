

def strips(s):
    return s.strip()

f = open("input.txt")
# f = open("test.txt")
dat = list(map(strips, f.readlines()))

ing = []
database = {}
for i in dat:
    for cont in [j[:-1] for j in i.split("(contains ")[1].split()]:
        if cont not in database:
            database[cont] = [set(i.split("(")[0].split())]
        else:
            database[cont].append(set(i.split("(")[0].split()))
    ing += i.split("(")[0].split()

found = {}
for i in list(database.keys()):
    found_new = {}
    s1 = set()
    # if len(database[i]) > 1:
    database[i] = database[i][0].intersection(*database[i])
    if len(list(database[i])) == 1:
        found[i] = list(database[i])[0]



might = []
for i in list(database.keys()):
    might += list(database[i])

# not_ing = list(set(ing) - set(might))

print("Part 1:", [x for x in ing if x not in might].__len__())


# database lists the allergens & the ingredients and can be solved by hand.

found = []

while found.__len__() < database.__len__():
    for i in database.keys():
        if len(database[i]) == 1 and i not in found:
            s = database[i]
            found.append(i)

    for j in found:
        for k in database.keys():
            if database[k].__len__() > 1:
                database[k] -= database[j]

found.sort()

out = ""
for i in found:
    s = []
    out += database[i].pop()
    out += ","


print("Part 2: " + out[:out.__len__()-1])


