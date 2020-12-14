def strips(s):
    return s.strip()

#quickly toggle between input and test values
f = open("input.txt")
# f = open("test.txt")

# variety of input sanitations
# dat = list(map(int, f.readlines()))
dat = list(map(strips, f.readlines()))
# dat = f.read().strip()

instr_ptr = 0
accum = 0
visited = []
while True:
    if instr_ptr not in visited:
        visited.append(instr_ptr)
    else:
        break
    instr = dat[instr_ptr].split(" ")
    if instr[0] == 'acc':
        accum += int(instr[1])
        instr_ptr += 1
        instr_ptr %= len(dat)
    elif instr[0] == 'jmp':
        instr_ptr += int(instr[1])
        instr_ptr %= len(dat)
    elif instr[0] == 'nop':
        instr_ptr += 1
        instr_ptr %= len(dat)


print("Part One: " + str(accum))


chngs = {}
for i in range(len(dat)-1):
    if dat[i][:3] == 'jmp':
        chngs[i] = 'nop'
    if dat[i][:3] == 'nop':
        chngs[i] = 'jmp'

for i in list(chngs.keys().__reversed__()):

    instr_ptr = 0
    accum = 0
    visited = []
    while True:
        if instr_ptr not in visited:
            visited.append(instr_ptr)
        else:
            break
        instr = dat[instr_ptr].split(" ")
        if instr_ptr == i:
            instr[0] = chngs[i]
        if instr[0] == 'acc':
            accum += int(instr[1])
            instr_ptr += 1

        elif instr[0] == 'jmp':
            instr_ptr += int(instr[1])

        elif instr[0] == 'nop':
            instr_ptr += 1

        if instr_ptr == len(dat):
            print("Part Two: " + str(accum))
            exit()
        instr_ptr %= len(dat)

