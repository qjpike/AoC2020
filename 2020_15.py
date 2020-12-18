order = [8,11,0,19,1,2]
# order = [0,3,6]

rank = {}

for i in order:
    rank[i] = order.index(i) + 1

next = 0
last_zm1 = rank[next]

rank[next] = len(order) + 1

for i in range(len(order) + 2,2021):
    last = next
    next = i - 1 - last_zm1
    if next not in rank:
        last_zm1 = i
    else:
        last_zm1 = rank[next]
    rank[next] = i


print("Part 1: ", next)

''' Part 2 '''

order = [8,11,0,19,1,2]
# order = [0,3,6]

rank = {}

for i in order:
    rank[i] = order.index(i) + 1

next = 0
last_zm1 = rank[next]

rank[next] = len(order) + 1

for i in range(len(order) + 2,30000001):
    last = next
    next = i - 1 - last_zm1
    if next not in rank:
        last_zm1 = i
    else:
        last_zm1 = rank[next]
    rank[next] = i

print("Part 2: ", next)



