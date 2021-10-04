def strips(str):
    return str.strip()


dat = open("input_24.txt").readlines()
# dat = list(map(strips, open("test.txt").readlines()))

dirs = ['e', 'se', 'sw', 'w', 'nw', 'ne']

moves = {}

moves['e'] = (+1, 0)
moves['ne'] = (1, -1)
moves['nw'] = (0, -1)
moves['w'] = (-1, 0)
moves['sw'] = (-1, +1)
moves['se'] = (0, +1)

surrounds = list(moves.values())


def part1():
    tiles = {}
    for line in dat:
        i = 0
        x_pos = 0
        y_pos = 0
        line = line.strip()
        while i < len(line):
            if line[i] in dirs:
                dir = line[i]
            else:
                dir = line[i:i + 2]
            i += len(dir)

            x, y = moves[dir]
            x_pos += x
            y_pos += y

        if (x_pos, y_pos) not in tiles:
            tiles[(x_pos, y_pos)] = 1
        else:
            tiles[(x_pos, y_pos)] += 1

    for i in list(tiles.keys()):
        if tiles[i] % 2 == 0:
            tiles.pop(i)
        else:
            tiles[i] = 1

    return tiles


def part2():
    tiles = part1()
    for i in list(tiles.keys()):
        if not tiles[i]:
            tiles.pop(i)

    for d in range(100):
        '''
        need to make a list of all possible tiles and run this logic over each one. It's another game of life thing.
        '''

        # create a list (checks: actually a dict) of all of the black tiles and all of the tiles that surround all of the black tiles
        checks = tiles.copy()

        for (x_pos, y_pos) in list(tiles.keys()):

            for x, y in surrounds:
                if (x + x_pos, y + y_pos) not in checks:
                    checks[(x + x_pos, y + y_pos)] = 0

        # test every position, if it is black, add it to a new 'tiles'
        new_tiles = {}
        for (x_pos, y_pos) in list(checks.keys()):

            count = 0
            for x,y in surrounds:
                if (x+x_pos, y+y_pos) in tiles:
                    count += 1

            # if the tile is black and count = 1, the tile stays black and should be added to new_tiles
            if checks[(x_pos, y_pos)] == 1:
                    if count == 1 or count == 2:
                        new_tiles[(x_pos, y_pos)] = 1
            elif checks[(x_pos, y_pos)] == 0:
                if count == 2:
                    new_tiles[(x_pos, y_pos)] = 1
            else:
                print("Messed this up!")
                exit()

        tiles = new_tiles.copy()

        print("Day", d + 1, ":", sum(list(tiles.values())))


# print("Part 1:",sum(list(part1().values())))
part2()