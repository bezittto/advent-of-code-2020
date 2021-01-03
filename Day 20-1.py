# --- Day 20: Jurassic Jigsaw ---

# The high-speed train leaves the forest and quickly carries you south. You can even see a desert in the distance! Since you have some spare time, you might as well see if there was anything interesting in the image the Mythical Information Bureau satellite captured.

# After decoding the satellite messages, you discover that the data actually contains many small images created by the satellite's camera array. The camera array consists of many cameras; rather than produce a single square image, they produce many smaller square image tiles that need to be reassembled back into a single image.

# Each camera in the camera array returns a single monochrome image tile with a random unique ID number. The tiles (your puzzle input) arrived in a random order.

# Worse yet, the camera array appears to be malfunctioning: each image tile has been rotated and flipped to a random orientation. Your first task is to reassemble the original image by orienting the tiles so they fit together.

# To show how the tiles should be reassembled, each tile's image data includes a border that should line up exactly with its adjacent tiles. All tiles have this border, and the border lines up exactly when the tiles are both oriented correctly. Tiles at the edge of the image also have this border, but the outermost edges won't line up with any other tiles.

# For example, suppose you have the following nine tiles:

# Tile 2311:
# ..##.#..#.
# ##..#.....
# #...##..#.
# ####.#...#
# ##.##.###.
# ##...#.###
# .#.#.#..##
# ..#....#..
# ###...#.#.
# ..###..###

# Tile 1951:
# #.##...##.
# #.####...#
# .....#..##
# #...######
# .##.#....#
# .###.#####
# ###.##.##.
# .###....#.
# ..#.#..#.#
# #...##.#..

# Tile 1171:
# ####...##.
# #..##.#..#
# ##.#..#.#.
# .###.####.
# ..###.####
# .##....##.
# .#...####.
# #.##.####.
# ####..#...
# .....##...

# Tile 1427:
# ###.##.#..
# .#..#.##..
# .#.##.#..#
# #.#.#.##.#
# ....#...##
# ...##..##.
# ...#.#####
# .#.####.#.
# ..#..###.#
# ..##.#..#.

# Tile 1489:
# ##.#.#....
# ..##...#..
# .##..##...
# ..#...#...
# #####...#.
# #..#.#.#.#
# ...#.#.#..
# ##.#...##.
# ..##.##.##
# ###.##.#..

# Tile 2473:
# #....####.
# #..#.##...
# #.##..#...
# ######.#.#
# .#...#.#.#
# .#########
# .###.#..#.
# ########.#
# ##...##.#.
# ..###.#.#.

# Tile 2971:
# ..#.#....#
# #...###...
# #.#.###...
# ##.##..#..
# .#####..##
# .#..####.#
# #..#.#..#.
# ..####.###
# ..#.#.###.
# ...#.#.#.#

# Tile 2729:
# ...#.#.#.#
# ####.#....
# ..#.#.....
# ....#..#.#
# .##..##.#.
# .#.####...
# ####.#.#..
# ##.####...
# ##..#.##..
# #.##...##.

# Tile 3079:
# #.#.#####.
# .#..######
# ..#.......
# ######....
# ####.#..#.
# .#...#.##.
# #.#####.##
# ..#.###...
# ..#.......
# ..#.###...

# By rotating, flipping, and rearranging them, you can find a square arrangement that causes all adjacent borders to line up:

# #...##.#.. ..###..### #.#.#####.
# ..#.#..#.# ###...#.#. .#..######
# .###....#. ..#....#.. ..#.......
# ###.##.##. .#.#.#..## ######....
# .###.##### ##...#.### ####.#..#.
# .##.#....# ##.##.###. .#...#.##.
# #...###### ####.#...# #.#####.##
# .....#..## #...##..#. ..#.###...
# #.####...# ##..#..... ..#.......
# #.##...##. ..##.#..#. ..#.###...

# #.##...##. ..##.#..#. ..#.###...
# ##..#.##.. ..#..###.# ##.##....#
# ##.####... .#.####.#. ..#.###..#
# ####.#.#.. ...#.##### ###.#..###
# .#.####... ...##..##. .######.##
# .##..##.#. ....#...## #.#.#.#...
# ....#..#.# #.#.#.##.# #.###.###.
# ..#.#..... .#.##.#..# #.###.##..
# ####.#.... .#..#.##.. .######...
# ...#.#.#.# ###.##.#.. .##...####

# ...#.#.#.# ###.##.#.. .##...####
# ..#.#.###. ..##.##.## #..#.##..#
# ..####.### ##.#...##. .#.#..#.##
# #..#.#..#. ...#.#.#.. .####.###.
# .#..####.# #..#.#.#.# ####.###..
# .#####..## #####...#. .##....##.
# ##.##..#.. ..#...#... .####...#.
# #.#.###... .##..##... .####.##.#
# #...###... ..##...#.. ...#..####
# ..#.#....# ##.#.#.... ...##.....

# For reference, the IDs of the above tiles are:

# 1951    2311    3079
# 2729    1427    2473
# 2971    1489    1171

# To check that you've assembled the image correctly, multiply the IDs of the four corner tiles together. If you do this with the assembled tiles from the example above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.

# Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?


import numpy as np
from copy import deepcopy

# read data
fpath = 'Day 20-input2.txt'

with open(fpath, 'r') as f:
    raw = f.read().split('\n')

def getTileNo( chars ):
    _ = chars.split(' ')
    if _[0] == 'Tile':        
        match = _[1].replace(':','')
        try:
            match = int(match)
            return match
        except:
            return None
    return None

class Tile:

    tileSize = 10

    adjacentOptions = None

    bits = None

    def __init__(self, no,bits):
        self.no = no
        if '#' in bits[0] or '.' in bits[0]:
            bits = self._encode(bits)
        self.bits = bits

        self.adjacentOptions = {
            'top': list(),
            'right': list(),
            'bottom': list(),
            'left': list()
        }

    def _encode(self, raw):
        result = np.zeros((self.tileSize,self.tileSize))        
        for i,r in enumerate(raw):
            for j,c in enumerate(r):
                if c=='#': result[i][j] = 1
        return result

    def leftBorder(self):
        return np.array( [ r[0] for r in self.bits ] )

    def rightBorder(self):
        return np.array( [ r[-1] for r in self.bits ] )

    def topBorder(self):
        return self.bits[0]
    
    def bottomBorder(self):
        return self.bits[-1]

    def flipH(self):
        s = self.bits.shape[0]
        for i in range( int(s/2) ):
            temp1 = self.bits[i].copy()
            temp2 = self.bits[-i-1].copy()
            self.bits[ i ] = temp2
            self.bits[ -i-1 ] = temp1

    def flipV(self):
        s = self.bits.shape[0]
        for i in range( s ):
            for j in range( int(s/2) ):
                temp1 = self.bits[i][j].copy()
                temp2 = self.bits[i][-j-1].copy()
                self.bits[i][j] = temp2
                self.bits[i][-j-1] = temp1

    def rotate90(self):
        newbits = np.zeros((self.tileSize, self.tileSize))
        for ri in range( self.tileSize ):
            for ci in range( self.tileSize ):
                newri = ci
                newci = self.tileSize -1 - ri
                newbits[newri][newci] = self.bits[ri][ci]
        self.bits = newbits
        
tiles = list()

currentLine = 0
while currentLine < len(raw):
    tileNo = getTileNo( raw[currentLine] )
    if tileNo is not None:
        bits_ = raw[ currentLine+1 : currentLine+1+Tile.tileSize ]
        t = Tile( tileNo, bits_ )
        tiles.append( t )

    currentLine += Tile.tileSize + 2

import math
from collections import Counter

targetSizeW = int( math.sqrt(len(tiles)) )
targetTilesCount = len(tiles)

tilesWithVariations = list()
for temp in tiles:
    t1 = deepcopy(temp)
    tilesWithVariations.append( t1 )

    t2 = deepcopy( t1 )
    t2.rotate90()
    tilesWithVariations.append( t2 )

    t3 = deepcopy( t2 )
    t3.rotate90()
    tilesWithVariations.append( t3 )

    t4 = deepcopy( t3 )
    t4.rotate90()
    tilesWithVariations.append( t4 )

    t1v = deepcopy( t1 )
    t1v.flipV()
    tilesWithVariations.append( t1v )

    t2v = deepcopy( t2 )
    t2v.flipV()
    tilesWithVariations.append( t2v )

    t3v = deepcopy( t3 )
    t3v.flipV()
    tilesWithVariations.append( t3v )

    t4v = deepcopy( t4 )
    t4v.flipV()
    tilesWithVariations.append( t4v )

matched = 0
for i in range(len(tilesWithVariations)):
    t1 = tilesWithVariations[i]
    for j in range(len(tilesWithVariations)):
        t2 = tilesWithVariations[j]        
        if t1.no == t2.no: continue
        if ( t1.topBorder() == t2.bottomBorder() ).all(): 
            t1.adjacentOptions['top'].append(t2)      
            matched += 1      
        if ( t1.bottomBorder() == t2.topBorder() ).all(): 
            t1.adjacentOptions['bottom'].append(t2)
            matched += 1      
        if ( t1.rightBorder() == t2.leftBorder() ).all(): 
            t1.adjacentOptions['right'].append(t2)
            matched += 1      
        if ( t1.leftBorder() == t2.rightBorder() ).all(): 
            t1.adjacentOptions['left'].append(t2)
            matched += 1      

    
def traverse( currentT ):
    global grid,usedNos,fromNos, recWall

    code_ = str(currentT)
    if code_ not in recWall:
        recWall[ code_ ] = 0
    recWall[ code_ ] +=1
    if recWall[ code_ ] > 500: return

    tofollowup = list()

    match_ = np.where(grid == currentT.no)
    atY = match_[0][0]
    atX = match_[1][0]

    for direction,v in currentT.adjacentOptions.items():
        if len(v)>1: print('More items!',len(v))
        if len(v)>0:
            currentX = atX
            currentY = atY

            if direction == 'top': currentY = atY - 1
            if direction == 'bottom': currentY = atY + 1 
            if direction == 'right': currentX = atX + 1
            if direction == 'left': currentX = atX - 1

            if currentX<0:
                currentX = 0
                grid = np.pad( grid, ((0,0),(1,0)), 'constant' )
                atX = 1

            if currentY<0:
                currentY = 0
                grid = np.pad( grid, ((1,0),(0,0)), 'constant' )
                atY = 1

            if currentY==grid.shape[0]:
                grid = np.pad( grid, ((0,0),(1,0)), 'constant' )
                
            if currentX==grid.shape[1]:
                grid = np.pad( grid, ((0,0),(0,1)), 'constant' )
                
            if v[0].no in usedNos and usedNos[v[0].no] != v[0]:
                return

            if grid[ currentY ][ currentX ] == 0 or (
                grid[ currentY ][ currentX ]==v[0].no 
                and usedNos[v[0].no]==v[0]
                and fromNos[v[0].no]!=currentT
                ):
                grid[ currentY ][ currentX ] = v[0].no
                usedNos[ v[0].no ] = v[0]
                fromNos[ v[0].no ] = currentT
                tofollowup.append( v[0] )
            else:
                return        

            # check if all ok, or we are finished!
            if len(usedNos) == targetTilesCount: 
                print('Done!')
                print(grid)
                return


    for tf in tofollowup:
        traverse( tf )
    
for t in tilesWithVariations:
    print(t.no)
    print('---')

    usedNos = dict()
    fromNos = dict()
    usedNos[t.no] = t
    fromNos[t.no] = None
    recWall = dict()

    grid = np.zeros((targetSizeW,targetSizeW))
    grid[0][0] = t.no
    traverse( t)

# Done
# [[3373. 1783. 2011. 3863. 1021. 3691. 3359. 3329. 2749. 1597. 2383. 3187.     0.    0.    0.    0.]
#  [3617. 1733. 2143. 3181. 1553. 1277. 3877. 3643. 2609. 2687. 1877. 1831.     0.    0.    0.    0.]
#  [2819. 2837. 3163. 2389. 1049. 1741. 1031. 2971. 1433. 3533. 2129. 3947.     0.    0.    0.    0.]
#  [3119. 1423. 1151. 2111. 2693. 3251. 2203. 2017. 3823. 3023. 3221. 3449.     0.    0.    0.    0.]
#  [3217. 1307. 1609. 3083. 2089. 1559. 2659. 2131. 1543. 2767. 3917. 1663.     0.    0.    0.    0.]
#  [3203. 2917. 1667. 1381. 1187. 2521. 3001. 1291. 2237. 3907. 1153. 2557.     0.    0.    0.    0.]
#  [2539. 1361. 3089. 1657. 1061. 2473. 1627. 3209. 2273. 1549. 1453. 1429.     0.    0.    0.    0.]
#  [3413. 3067. 2927. 1511. 1459. 1493. 1181. 3923. 3919. 2333. 1979. 1289.     0.    0.    0.    0.]
#  [3697. 1697. 1019. 2953. 1447. 3593. 2677. 1907. 2339. 2081. 2399. 2719.     0.    0.    0.    0.]
#  [1069. 2063. 1619. 1373. 2531. 3571. 1879. 2861. 3331. 3851. 1129. 2069.     0.    0.    0.    0.]
#  [1009. 3253. 2999. 2251. 2897. 1097. 1901. 1399. 2833. 2801. 2113. 2803.     0.    0.    0.    0.]
#  [1567. 1321. 3037. 3457. 2029. 3539. 3041. 3881. 3677. 2137. 3541. 3847.     0.    0.    0.    0.]
#  [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
#      0.    0.    0.    0.]
#  [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
#      0.    0.    0.    0.]
#  [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
#      0.    0.    0.    0.]
#  [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
#      0.    0.    0.    0.]
#  [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
#      0.    0.    0.    0.]
#  [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
#      0.    0.    0.    0.]
#  [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
#      0.    0.    0.    0.]
#  [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
#      0.    0.    0.    0.]
#  [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
#      0.    0.    0.    0.]
#  [   0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
#      0.    0.    0.    0.]]


# multiply no in corners 
# 3373 x 1567 x  3187 x 3847 = 64802175715999 is the answer 

