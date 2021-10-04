#
#
# inp = '614752839'
# inp = '389125467'
#
# curr_arr = inp
# for i in range(10):
#     curr_cup = curr_arr[i%9]
#     pick_up = (curr_arr*2)[i%10+1:i%10+4]
#     dest = int(curr_cup) - 1
#     tmp_arr = curr_arr[:i%9+1] + curr_arr[i%9+4:]
#     while str(dest) not in tmp_arr:
#         dest = (dest - 1)%10
#     dest_index = tmp_arr.index(str(dest))
#     if dest_index != 0:
#         curr_arr = tmp_arr[:dest_index+1] + pick_up + tmp_arr[dest_index+1:]
#     else:
#         curr_arr = pick_up[2] + tmp_arr[dest_index+1:] + str(dest) + pick_up[:2]
#
# print(curr_arr)

s = "614752839"

cups = list(map(int,s))

for i in range(100):
    move = cups[1:4]
    dest = cups[0] - 1
    new_cups = cups[:1] + cups[4:]
    while dest not in new_cups:
        dest = (dest - 1) % 10
    new_cups = new_cups[:new_cups.index(dest)+1] + move + new_cups[new_cups.index(dest) + 1:]
    cups = new_cups[1:] + new_cups[:1]

print("".join(map(str,cups[cups.index(1)+1:] + cups[:cups.index(1)])))

import time
start = time.time()

class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next


lookup = {}

nodes = [Node(int(c)) for c in s]

cur = 10
while len(nodes) < 1000000:
    nodes.append(Node(cur))
    cur += 1

for a,b in zip(nodes,nodes[1:]):
    a.next = b

nodes[-1].next = nodes[0]

lookup = {}
for node in nodes:
    lookup[node.val] = node

cur = nodes[0]

for i in range(10000000):
    move1 = cur.next
    move2 = move1.next
    move3 = move2.next
    cur.next = move3.next
    used = {cur.val,move1.val,move2.val,move3.val}
    curr = cur.val
    while curr in used:
        curr = (curr - 1) % 1000000
    if curr == 0:
        curr = 1000000
    new_insert = lookup[curr]
    insert_next = new_insert.next

    new_insert.next = move1
    move3.next = insert_next

    cur = cur.next

cup1 = lookup[1]
a = cup1.next
b = a.next

end = time.time()

print(a.val * b.val)

print(end - start)