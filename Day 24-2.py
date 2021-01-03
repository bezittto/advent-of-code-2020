# --- Part Two ---

# The tile floor in the lobby is meant to be a living art exhibit. Every day, the tiles are all flipped according to the following rules:

#     Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
#     Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.

# Here, tiles immediately adjacent means the six tiles directly touching the tile in question.

# The rules are applied simultaneously to every tile; put another way, it is first determined which tiles need to be flipped, then they are all flipped at the same time.

# In the above example, the number of black tiles that are facing up after the given number of days has passed is as follows:

# Day 1: 15
# Day 2: 12
# Day 3: 25
# Day 4: 14
# Day 5: 23
# Day 6: 28
# Day 7: 41
# Day 8: 37
# Day 9: 49
# Day 10: 37

# Day 20: 132
# Day 30: 259
# Day 40: 406
# Day 50: 566
# Day 60: 788
# Day 70: 1106
# Day 80: 1373
# Day 90: 1844
# Day 100: 2208

# After executing this process a total of 100 times, there would be 2208 black tiles facing up.

# How many tiles will be black after 100 days?

fpath = 'Day 24-input2.txt'

with open(fpath,'r') as f:
    instructions = f.read().split('\n')

DIRECTIONS = {
    'e': (1.0,0.0),
    'se': (.5,-1.0),
    'sw': (-.5,-1.0),
    'w': (-1.0,0.0),
    'nw': (-.5,1.0),
    'ne': (.5,1.0)
}

def parseInstructions( code ):    
    result = list()
    
    while len(code)>0:       
        chk2_ =  code[:2]
        chk1_ = code[:1]
        if chk2_ in DIRECTIONS:
            result.append( chk2_ )
            code = code[2:]

        elif chk1_ in DIRECTIONS:
            result.append( chk1_ )
            code = code[1:]

    return result

def moveAround( steps ):
    x = 0
    y = 0

    for s in steps:
        deltax = DIRECTIONS[s][0]
        deltay = DIRECTIONS[s][1]
        x += deltax
        y += deltay

    xy = str(x)+','+str(y)
         
    return xy

def getAdjacent( xycode ):
    temp = xycode.split(',')
    x = float(temp[0])
    y = float(temp[1])
    result = list()
    for k,v in DIRECTIONS.items():
        x_ = x + v[0]
        y_ = y + v[1]
        x_y_ = str(x_) + ',' + str(y_)
        result.append( x_y_ )

    return result

def getColor( xycode, space ):
    if xycode in space:
        return space[xycode]
    else:
        return 'w'

def getblacks( d ):
    countb = 0
    for k,v in d.items():
        if v == 'b': countb+=1
    
    return countb

# Day 0
visited = dict()
for i in instructions:
    steps_ = parseInstructions( i )
    xy_ = moveAround( steps_ )

    if xy_ not in visited: visited[xy_] = 0
    visited[xy_] += 1

floor = dict()
for k,v in visited.items():
    if v % 2 == 0:
        c = 'w'
    else:
        c = 'b'

    floor[k] = c

# Day N
N = 100
for x in range(N):

    newfloor = floor.copy()
    for k,v in floor.items():
        adjacent = getAdjacent(k)          
        for a in adjacent:
            if a not in floor: newfloor[a] = 'w'

    newfloor2 = newfloor.copy()

    for k,v in newfloor.items():
        adjacent = getAdjacent(k)    
        whites = 0
        blacks = 0    
        for a in adjacent:
            c_ = getColor(a, newfloor)
            if c_=='w': whites += 1
            if c_=='b': blacks += 1
        
        if v == 'w':
            if blacks == 2: newfloor2[k] = 'b'
        if v == 'b':
            if blacks == 0 or blacks>2: newfloor2[k] = 'w'

    floor = newfloor2


result = getblacks(floor)
print(result)

