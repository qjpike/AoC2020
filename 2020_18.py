def strips(s):
    return s.strip()

f = open("input.txt")
# f = open("test.txt")
# f = open("test2.txt")

# dat = list(map(int, f.readlines()))
dat = list(map(strips, f.readlines()))
# dat = f.read().strip()

def operate(operand_1,operator,operand_2):
    if operator == "*":
        return int(operand_1) * int(operand_2)
    else:
        return int(operand_1) + int(operand_2)

def math_back(math):
    prev = math.pop()
    if len(math) == 0:
        math.append(prev)
        return
    while math[-1] != "(":
        math.append(operate(int(prev),math.pop(),int(math.pop())))
        prev = math.pop()
        if len(math) == 0:
            math.append(prev)
            return
    math.append(prev)

def math_back_2(math):
    prev = math.pop()
    if len(math) == 0:
        math.append(prev)
        return
    while math[-1] != "(":
        if math[-1] == "*":
            math.append(prev)
            return
        math.append(operate(int(prev), math.pop(), int(math.pop())))
        prev = math.pop()
        if len(math) == 0:
            math.append(prev)
            return
    math.append(prev)

nums = ['0','1','2','3','4','5','6','7','8','9']
operators = ['+','*']
parens = ["(",")"]

def part1():
    count = 0
    for i in dat:
        math = list()


        for j in i:
            if j in nums:
                #if next is a number, look for stack operand, operate on previous stack value
                if len(math) == 0:
                    math.append(j)
                else:
                    prev = math.pop()
                    if prev in operators:
                        math.append(operate(int(j),prev,int(math.pop())))
                    if prev in parens:
                        math.append(prev)
                        math.append(j)
            elif j in operators:
                math.append(j)
            elif j in parens:
                if j == "(":
                    math.append(j)
                elif j == ")":
                    while math[-2] != "(":
                        math.append(operate(math.pop(), math.pop(), math.pop()))
                    if math[-2] == "(":
                        prev = math.pop()
                        math.pop()
                        math.append(prev)
                        math_back(math)
                    else:
                        prev_3 = math.pop()
                        if prev_3 != "(":
                            if prev_3 in operators:
                                math.append(operate(prev,prev_3,math.pop()))
                        else:
                            math.append(prev_3)
                        math.append(prev)

        count += math.pop()

    print("Part 1: ", count)


def part2():
    count = 0
    for i in dat:
        math = list()
        for j in i:
            if j in nums:
                # if next is a number, look for stack operand, operate on previous stack value
                if len(math) == 0:
                    math.append(j)
                else:
                    prev = math.pop()
                    if prev in operators:
                        if prev == "+":
                            math.append(operate(int(j), prev, int(math.pop())))
                        elif prev == "*":
                            math.append(prev)
                            math.append(j)
                    if prev in parens:
                        math.append(prev)
                        math.append(j)
            elif j in operators:
                math.append(j)
            elif j in parens:
                if j == "(":
                    math.append(j)
                elif j == ")":
                    while math[-2] != "(":
                        math.append(operate(math.pop(), math.pop(), math.pop()))
                    if math[-2] == "(":
                        prev = math.pop()
                        math.pop()
                        math.append(prev)
                        math_back_2(math)
                    else:
                        prev_3 = math.pop()
                        if prev_3 != "(":
                            if prev_3 in operators:
                                if prev == "+":
                                    math.append(operate(int(j), prev, int(math.pop())))
                                elif prev == "*":
                                    math.append(prev)
                        else:
                            math.append(prev_3)
                        math.append(prev)

        math_back(math)
        count += math.pop()

    print("Part 2: ", count)

part1()
part2()