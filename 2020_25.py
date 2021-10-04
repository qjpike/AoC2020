card_pk = 9232416
door_pk = 14144084

def transform(subNum, publicKey):
    j = 1
    loopSize = 0
    while j != publicKey:
        j = (j*subNum)%20201227
        loopSize += 1
    return loopSize

def decrypt(subNum, loopsize):
    j = 1
    for i in range(loopsize):
        j = (j*subNum)%20201227
    return j


door_ls = transform(7,door_pk)

print("Part 1:",decrypt(card_pk,door_ls))