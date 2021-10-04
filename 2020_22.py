

def strips(s):
    return s.strip()

f = open("input_22.txt")
# f = open("test.txt")
dat = list(map(strips, f.readlines()))

def part1():
    p1_stack = []
    p2_stack = []

    p1p2 = 0
    for i in dat:
        if i == "Player 1:":
            continue
        elif i == "Player 2:":
            p1p2 = 1
            continue
        elif i == "":
            continue
        if p1p2 == 0:
            p1_stack.append(int(i))
        elif p1p2 == 1:
            p2_stack.append(int(i))

    while len(p1_stack) != 0 and len(p2_stack) != 0:
        p1_card = p1_stack.pop(0)
        p2_card = p2_stack.pop(0)
        if p1_card > p2_card:
            p1_stack.append(p1_card)
            p1_stack.append(p2_card)
        else:
            p2_stack.append(p2_card)
            p2_stack.append(p1_card)


    if len(p2_stack) == 0:
        m = len(p1_stack)
        count = 0
        for i in range(len(p1_stack)):
            count += p1_stack.pop(0) * m
            m -= 1
    else:
        m = len(p2_stack)
        count = 0
        for i in range(len(p2_stack)):
            count += p2_stack.pop(0) * m
            m -= 1

    print("Part 1:",count)


def part2(p1_stack,p2_stack):

    prev_decks = []
    while len(p1_stack) > 0 and len(p2_stack) > 0:
        if (str(p1_stack),str(p2_stack)) in prev_decks:
            winner = "p1"
            break
        else:
            prev_decks.append((str(p1_stack),str(p2_stack)))

        p1c = p1_stack.pop(0)
        p2c = p2_stack.pop(0)

        if len(p1_stack) >= p1c and len(p2_stack) >= p2c:
            winner = part2(p1_stack[:p1c],p2_stack[:p2c])
        else:
            if p1c > p2c:
                winner = 'p1'
            else:
                winner = 'p2'

        if winner == "p1":
            p1_stack += [p1c,p2c]
        else:
            p2_stack += [p2c,p1c]

    return winner


p1_stack = []
p2_stack = []

p1p2 = 0
for i in dat:
    if i == "Player 1:":
        continue
    elif i == "Player 2:":
        p1p2 = 1
        continue
    elif i == "":
        continue
    if p1p2 == 0:
        p1_stack.append(int(i))
    elif p1p2 == 1:
        p2_stack.append(int(i))






import time


part1()
start = time.time()
if part2(p1_stack,p2_stack) == "p1":
    print("Part 2:",sum([(len(p1_stack) - i) * x for i,x in enumerate(p1_stack)]))
else:
    print("Part 2:",sum([(len(p2_stack) - i) * x for i, x in enumerate(p2_stack)]))
end = time.time()
print("P2 Timer:",end - start)