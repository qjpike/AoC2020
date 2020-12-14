def strips(s):
    return s.strip()

f = open("input.txt")
# f = open("test2.txt")
# f = open("test.txt")


# dat = list(map(int, f.readlines()))
dat = list(map(strips, f.readlines()))
# dat = f.read().strip()

mask_on = 0
mask_off = 0xFFFFFFFFF
mem = {}
for i in dat:
    if i[:4] == "mask":
        mask_on = 0
        mask_off = 0xFFFFFFFFF
        mask_raw = i.split("=")[1].strip()
        for j in range(len(mask_raw)):
            if mask_raw[j] == "1":
                mask_on = mask_on ^ 1<<(35-j)
            if mask_raw[j] == "0":
                mask_off = mask_off ^ 1 << (35-j)
    else:
        mem_addr = int(i.split("[")[1].split("]")[0])
        # print(bin(int(i.split("=")[1].strip()) & mask_on))
        val = int(i.split("=")[1].strip())
        val |= mask_on
        val &= mask_off
        mem[mem_addr] = val
        #
        # print("  " + mask_raw)
        # print(format(int(i.split("=")[1].strip()),'38b'))
        # print(format(mem[mem_addr],'38b'))
        # print(format(mask_on,'38b'))
        # print(format(mask_off,'38b'))
print(sum(mem.values()))

mem = {}
for i in dat:
    if i[:4] == "mask":
        mask_on = 0
        dcs = []
        mask_raw = i.split("=")[1].strip()
        for j in range(len(mask_raw)):
            if mask_raw[j] == "1":
                mask_on = mask_on ^ 1<<(35-j)
            elif mask_raw[j] == 'X':
                dcs.append(35-j)
    else:
        val = int(i.split("=")[1].strip())
        mem_addr = int(i.split("[")[1].split("]")[0])

        tmp_mem_addr = mem_addr
        tmp_mem_addr |= mask_on
        tmal = list(format(tmp_mem_addr,'#038b'))[2:]

        for i in range(2**len(dcs)):
            mask_on_dcs = 0

            mask_lst = list(format(i,'#0{}b'.format(len(dcs)+2)))[2:]
            for j in range(len(dcs)):
                tmal[35-dcs[j]] = mask_lst[j]
                mem_addr = int("".join(tmal),2)
                mem[mem_addr] = val

print(sum(mem.values()))

