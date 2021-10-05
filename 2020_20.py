import collections
import copy

def strips(s):
    return s.strip()

f = open("input.txt")
# f = open("test.txt")


# dat = list(map(int, f.readlines()))
dat = list(map(strips, f.readlines()))
# dat = f.read().strip()

tile_inp_size = 12

class Tile:
    def __init__(self,name,arr):
        self.title = int(name)
        self.x_size = len(arr[0])
        self.y_size = len(arr)
        self.tile = []
        for j in arr:
            self.tile.append(j)
        self.edges = self.get_edge_vals(arr)

    def orient_tile(self,edge_vals, top_val=None, left_val=None):
        '''
        :param edge_vals: array of all the edge values in the image
        :param top_val: what top value we want
        :param left_val: what left value we want
        :return: True if this tile fits the top and/or left piece(s)
        '''
        # first, check if we're currently looking for the top-left tile
        if top_val == None and left_val == None:
            return self.orient_top_left_tile(edge_vals)

        # if we're not on the left edge and we have the desired value, orient that side to the left
        if left_val is not None and self.has_edge(left_val):
            for i in range(3 - (self.edges.index(left_val) % 4)):
                self.rotate()
            if self.edges[3] == left_val:
                return True
            if self.edges[3] != left_val:
                self.flip_v()
                return True
        # if we're on the left edge, orient the top edge up
        elif left_val is None and self.has_edge(top_val):
            for i in range(4-self.edges.index(top_val)%4):
                self.rotate()
            if self.edges[0] == top_val:
                return True
            else:
                self.flip_h()
                return True

    def orient_top_left_tile(self,edge_vals):
        edge_max = -1
        found = 0
        for i,j in enumerate(self.edges):
            if j in edge_vals:
                found += 1
                if edge_max < i:
                    edge_max = i

        if found < 4:
            return False

        rot = 8-edge_max
        for i in range(rot):
            self.rotate()
        return True

    def rotate(self):
        rotated = list(zip(*self.tile[::-1]))
        self.tile = [''.join(list(elem)) for elem in rotated]
        self.edges = self.get_edge_vals(self.tile)

    def flip_v(self):
        self.tile = self.tile[::-1]
        self.edges = self.get_edge_vals(self.tile)

    def flip_h(self):
        for i in range(len(self.tile)):
            self.tile[i] = self.tile[i][::-1]
        self.edges = self.get_edge_vals(self.tile)

    def has_edge(self,edge):
        return edge in self.edges

    def bin_conv(self,row):
        str = ''
        for i in row:
            if i == ".":
                str += '0'
            if i == "#":
                str += '1'
        return(int(str,2))

    def get_edge_vals(self,arr):
        top = self.bin_conv(arr[0])
        top_rev = self.bin_conv(arr[0][::-1])
        bottom = self.bin_conv(arr[-1])
        bottom_rev = self.bin_conv(arr[-1][::-1])
        left_arr = [i[0] for i in arr]
        left = self.bin_conv(left_arr)
        left_rev = self.bin_conv(left_arr[::-1])
        right_arr = [i[-1] for i in arr]
        right = self.bin_conv(right_arr)
        right_rev = self.bin_conv(right_arr[::-1])
        return [top, right,bottom,left,top_rev,right_rev,bottom_rev,left_rev]

    def __str__(self):
        return str(self.title)

    def print_tile(self):
        for i in self.tile:
            print(i)

    def find_edge_pos(self,edge_vals):
        curr_edge_pos = []
        for edge in self.edges:
            if edge in edge_vals:
                curr_edge_pos.append(self.edges.index(edge))
        return curr_edge_pos

# make a list of all tiles
tiles = []
for i in range(0,len(dat),tile_inp_size):
    tile_arr = dat[i:i+tile_inp_size]
    tiles.append(Tile(tile_arr[0][5:9],dat[i+1:i+tile_inp_size - 1]))

# make a list of all the tile edge values
vals = []
for i in tiles:
    vals += i.edges

#edge_vals is all image edge values (at the tile level)
edge_vals = [edge for edge,count in collections.Counter(vals).items() if count == 1]

# edge_tiles is all tiles with at least 1 (they all have 2 or 4) image edge values
edge_tiles = {}
for i in edge_vals:
    for j in tiles:
        if j.has_edge(i):
            if j.title not in list(edge_tiles.keys()):
                edge_tiles[j.title] = [j]
            else:
                edge_tiles[j.title].append(j)

# corners will have 4 tile edge values (2 forward, 2 reverse). Multiply any you find to get the answer
total = 1
corners = []
for i in list(edge_tiles.keys()):
    if len(edge_tiles[i]) == 4:
        total *= i

print("Part 1:",total)

edge_size = int(len(tiles)**.5)
image = [[] for i in range(edge_size)]

# create the tile arrangement, probably mis-rotated/flipped
for row in range(edge_size):
    for col in range(edge_size):
        if row == 0:
            top_val = None
        else:
            top_val = image[row - 1][col].edges[2]

        if col == 0:
            left_val = None
        else:
            left_val = image[row][col-1].edges[1]

        for i in tiles:
            if i.orient_tile(edge_vals,top_val,left_val):
                image[row].append(i)
                tiles.remove(i)
                break

# for i in image:
#     for j in i:
#         print(j,end=' ')
#     print("")


# delete the edges of all tiles and put into single array
image_arr = []
for i in range(edge_size*8):
    image_arr.append('')

for i in range(len(image)):
    for k in range(8):
        for j in range(len(image[i])):
            image_arr[i*8 + k] += image[i][j].tile[k+1][1:9]


# use Tile class for easy rotation
image_class = Tile('0000',image_arr)

# for i in image_class.tile:
#     print(i)

def find_monsters(ic_old):
    sea_monster_hashes = [(0,18),(1,0),(1,5),(1,6),(1,11),(1,12),(1,17),(1,18),(1,19),(2,1),(2,4),(2,7),(2,10),(2,13),(2,16)]

    first_count = sum([i.count("#") for i in image_class.tile])
    ic = copy.deepcopy(ic_old)
    count = first_count
    for a in range(4):
        for i in range(len(ic.tile)-3):
            for j in range(len(ic.tile[0])-19):
                found = True
                for y,x in sea_monster_hashes:
                    if ic.tile[i+y][j+x] != "#":
                        found = False
                        break
                if found:
                    curr_list = [list(ic.tile[i]),list(ic.tile[i+1]),list(ic.tile[i+2])]

                    for y,x in sea_monster_hashes:
                        curr_list[y][j + x] = "O"

                    ic.tile[i]   = ''.join(curr_list[0])
                    ic.tile[i+1] = ''.join(curr_list[1])
                    ic.tile[i+2] = ''.join(curr_list[2])

        count = sum([i.count("#") for i in ic.tile])
        if count != first_count:
            return count

        return False

for i in range(3):
    res = find_monsters(image_class)
    if res:
        print("Part 2: " + str(res))

    image_class.rotate()

image_class.flip_h()

for i in range(3):
    res = find_monsters(image_class)
    if res:
        print("Part 2: " + str(res))
    image_class.rotate()




