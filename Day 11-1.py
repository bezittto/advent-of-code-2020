# --- Day 11: Seating System ---

# Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

# By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

# The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

# L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL

# Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

#     If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
#     If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
#     Otherwise, the seat's state does not change.

# Floor (.) never changes; seats don't move, and nobody sits on the floor.

# After one round of these rules, every seat in the example layout becomes occupied:

# #.##.##.##
# #######.##
# #.#.#..#..
# ####.##.##
# #.##.##.##
# #.#####.##
# ..#.#.....
# ##########
# #.######.#
# #.#####.##

# After a second round, the seats with four or more occupied adjacent seats become empty again:

# #.LL.L#.##
# #LLLLLL.L#
# L.L.L..L..
# #LLL.LL.L#
# #.LL.LL.LL
# #.LLLL#.##
# ..L.L.....
# #LLLLLLLL#
# #.LLLLLL.L
# #.#LLLL.##

# This process continues for three more rounds:

# #.##.L#.##
# #L###LL.L#
# L.#.#..#..
# #L##.##.L#
# #.##.LL.LL
# #.###L#.##
# ..#.#.....
# #L######L#
# #.LL###L.L
# #.#L###.##

# #.#L.L#.##
# #LLL#LL.L#
# L.L.L..#..
# #LLL.##.L#
# #.LL.LL.LL
# #.LL#L#.##
# ..L.L.....
# #L#LLLL#L#
# #.LLLLLL.L
# #.#L#L#.##

# #.#L.L#.##
# #LLL#LL.L#
# L.#.L..#..
# #L##.##.L#
# #.#L.LL.LL
# #.#L#L#.##
# ..L.L.....
# #L#L##L#L#
# #.LLLLLL.L
# #.#L#L#.##

# At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

# Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?


# seatsMapRaw = [
#     'L.LL.LL.LL',
#     'LLLLLLL.LL',
#     'L.L.L..L..',
#     'LLLL.LL.LL',
#     'L.LL.LL.LL',
#     'L.LLLLL.LL',
#     '..L.L.....',
#     'LLLLLLLLLL',
#     'L.LLLLLL.L',
#     'L.LLLLL.LL',
# ]

seatsMapRaw = [
'LLLLLL.LLL.LLLL.LLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLL.LLL.LLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLL..L.LLLLLL',
'LLLLLLLLLL..LLL.LLLLLLL.LLLLLLLLLLLLLLLLLL.LLL.LL.LLLLLLLL.LLLLLLLL.L.LLLLL.LLLLLLLL.LLLLL.LLLLLLLL',
'LLLLLLLLLL.LL.LLLLLLLLLLLLLLLLLLL.L.LLLLLL.LLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL',
'LLLLLLLLLLLLLLL.LLLLLLL.L.LLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLLL.L.LLLLLL',
'LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLL.LLL.LLLL.LLLLLLLL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL',
'LLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLLLLL.LL.LLL.LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLL.LLL.LLLLLLLLLL.LLLLLLLL',
'.LLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLL.LLL.LL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.L.LLLLLLLL.LLLL.LLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLLLL',
'LLLLLLLLLL.L.LL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL..LLLLLLLLLLLLL.LLL.LLLL',
'..LL....L.LL........L...L......LL..L.L........L....L..........L..L.........LLLL..L.L.L..LL...LL....',
'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LL.LL.LLLLLLLL',
'LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLL..LLLLLLLL.LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLL.LLLLL.LL',
'LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LL.LLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LL.LLLLL.LLLLLLLL',
'L.L.........L..L..L.L....LLLL...LL..L....L.L..L..L.L.L.L........LL.L...........L........L..LLL...LL',
'LLLLLLLLLL.LLLLLLLLLLL.LL.LLLLLLLLL.LLLLLL.LLLL..LLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLL.L',
'LLLLLLLLLL.LLL..LLLLLLLLLLLLLLLLLLL..LLLLL.LLLLLLLLLLLLLLL.LLLLLLLL.LLLLL.L.LLLLL..L.LLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLL.LLLLLL.LL.LLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLL.L.LLLLLLLL',
'LLLLLLLLLL.LLLL..LLLL.LLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLL..LLLLLLLLLLLLLLL.LLLLLLLL.LLLLL.LLLLL.L.',
'LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLL.LL.LLL.LLLLLL.LLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL',
'LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLL.L..LLLL.LLL.LLLLLL..LLLLLLLL.LLLLL..LLLLLL.',
'LLLLLLLLLL.LLLLLLL.LLLLLLLLLL.LLLLL.LLLLLLLLLLLLL..LLLLLLL.L.LLLLLLLLLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLL..LLLLLLLL.LLLLLLLLLLLLLLLL.L.LL.LLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL',
'LLLLLLLLLLLLLLL..LLLLLL.L.LL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL',
'LL...L.LL....L.LL.L.....L.LL......L.......L...........L.L..L.LL....LL..LLL.L.LL...........L...LLLL.',
'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL..LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL',
'LLLLLLLLLLLLLLL.LL.LLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.L..LLLLLLLL.LLLLLL.LLLLLLLL.LLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLL.L.LLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL',
'LLLLLLLLLLLLLL..LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL',
'LLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLL.LLLLLL.L',
'LLLLLLLLLLLLLL..LLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLL.LL..LLLL.LLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLL.LLLLLLLLL.LL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL.L.LLLLLL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL',
'...LL.LL.L....L....LLL..LL..L.....................L....LL..L...LL..L........LL.....L...........L..L',
'LLLLLLLLLL.LLLL..LLL.LLLL.LLLLLLLLL.LLLLLL..LLLLL.LLLLLLLL.LLLLLLLLLLLLLLL...LLLLLLLLLLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.L.LLLLLLLLLL.L.LLLLLLLL',
'LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLL.L.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLL.LLLL',
'LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLL.LL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL',
'LLLLLLLLLL.LLL..LLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLL.LLLL.LLLLLL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLL.LL.LLL.LLL.LLLLLLLLLLL.LLLLLLLL.L.LLLLL.LLLLLLLL..LLLL.LLLLLLLL',
'LLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLL.LLLLLL.LLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL',
'.......LL.L.LL.....LL.L...L.L..LL..L...L..L.......LLLL....LL..LL.L...L...L...L..L.L.LL..L...L....L.',
'L.LLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL..LL..LLL.LLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLL.LLLLLLLLLL.LLLLLLLL.LLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL',
'LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLL.LLLLLLLL.LLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL',
'LLLLLLLLLL.LLLL..LLLLLLLL.LLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLL',
'LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL..LLLLLLLLLLLLL',
'LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLL.LLLL.L.LLLLLLLLLLLL.L.LLLLLLLL',
'L..LLL..L........L.LL......L........LL.....L.L..LL...L......L...LL......L.L.....LL..L......L...L.LL',
'LL.LLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLL..LLL..LLLLLLLL',
'LLLLLLLLLLLLLL..LLLL.LLLLLLLLLL.LLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLLLL',
'.L...L...L..LLLLLLL.L.L..............L.LL..L.L..LLL...L......LL.L...LL.L.L.L..L....L..LLL..LL.L....',
'LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLL.L.LLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL',
'LLLLLLLLLL.LLLLLLLLL.LLLL.LL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.L.LLLLL.LLLLL.LLLLLLLL',
'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL.L.LLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLL.LLLL.LLL.LLLLLLLL.LLLLLLLLLLLLLLLLL.LLLL.LLLLLLLL',
'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL..LLLLLLLLLLL..LL.LLLLLLL..LLLLLLL.LLLLLL.L.LLLLL.LLLLLLLL',
'LLLLLLLLLL.LL.L.LLLLLLLLLLL.LLLLLLL.LLLLLL.LL.LLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLL.LL.LLLLLLLL',
'LLLLLLLLLL.LLLLLLLLL.LLLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLL..LLLLLLL.LLLLLLL.LLLLLLLLLLLL.L.L.LLLLLL',
'LLLLLLLLLL.LLLLLLLLLLLLLL..LLLLLLLLLLLL.LL.LLLLLL.LLLLLLLL.LLLLLLLL.LL..LLL.LLLLLLLL.LLLLLLLLLLLLL.',
'....L.L..L......L.LL..L.L.LLL.L...L....LL.L..LL....LL.LL...LLL........L.LL..L...L..LL.LL..L...L...L',
'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLL.L',
'L.LLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLL.L.LLLLLLLLLLLLLLLLLLLLLLLL.LL.LLLL.LL.LLL.L.LLLLLLL.LLLLLL',
'LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.L.LLLLLLLLL.LLLLLLLLLL.LLLLLL.L',
'LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLL.LLL.LLLLLL.LLLLLLLLLLLL.LL.LL.LLLLL.LLLLLLL..LLLLLLLLLLLLL.LLLLLLLL',
'LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL',
'LLL.L.L.L..L...L...LL.L........LL..L..L.....L..L.LLL..L.L.L.L.LL..LLLL.L............L..........L...',
'LLLLLL.LLL.LLLL.L.LLLLLLLLLLLLLLLLL..LLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLL.L..LLLL.L.LLLLLL',
'LLLLLLLLLL.L.LLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL.L..LLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLL.L',
'LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLL.',
'LLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLL..LLLLL.LLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLL.L',
'L.LLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LL.LLL.LLLLLL.LLLLLLLL.LLLLLLLL.LLL.LLL.LLLLLLLL.LLLLLL.LLLLLLL',
'LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLL.LLLL.LLL.LLL.LLLL.LLLLLL..LLLLLLLLLLLLLL.LLLLLLLL',
'.....L..LLLL..LL....LLLL.LL..L..L...L.L...LL.L...L.........L.L..........L...L....L.L.LL.LL..LL.LL.L',
'LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLL.LL.LLLLLL.LLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLL.LLL',
'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLL.L.LLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL',
'LLLLLLLLLL.LLLL.LLL.LL.LLLLLLLLLLLLLLL.LLL..LLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL',
'.L.LL........L...LL.LLL...............LL....L...L....LL.LLL...............L....L...L...L....L...L..',
'LLLLLLLLLLLLLLL.LLL.LLLLL.L.LLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLL.LL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLL.LLLLLLLLLLLLL..LLLLLLLL',
'LLLLLLL.L..LLLL.LLLLLLLLL..LLLLL.LL.LLLLLL.LLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLL.L.LLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLL.LLLLLLLL.LLLLL.LL.LLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLL..LLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL',
'LLLLLL..LL.L.L..LL.LL....LL..LL.LLL...L..LL...L..L....L......L.L..LLL.L....LLLL.LL....LL.LL.....L.L',
'LLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLL',
'LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLL.LL.LLLLLLL.LLLLLLLL.LLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLLLLLLL.LLL.LLLLLL..LLLLLLLL.LLLLL.LLLLLLLL',
'LLLLLLLLLL.LLLL.LLL.LLLLL.LLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLL.LL.LLLLL.LLLLLLLLLL.LLLLLLLLL.L.LLLLLLLL',
'.LLLLL.LLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL',
]


import copy

seatsMapIteration0 = []
for y, r in enumerate(seatsMapRaw):
    _ = []
    for x, c in enumerate(r): _.append(c)
    seatsMapIteration0.append(_)

def isOccupied(seat):
    if seat is None: return False
    if seat =='.': return False
    if seat == '#': return True
    return False

def checkAdjacentOccupacy(x,y, seatsMap):
    neighbors = list()
    for deltay in [-1,0,1]:
        for deltax in [-1,0,1]:
            if deltay == 0 and deltax == 0: continue

            xindex_ = x + deltax
            yindex_ = y + deltay

            if xindex_< 0: continue
            if yindex_< 0: continue

            try:
                neighbors.append(seatsMap[yindex_][xindex_])
            except:
                pass

    result = 0
    for s in neighbors:
        result+=isOccupied(s)
    return result

def prettyPrint( printMap ):
    for r in printMap: print(r)

def iterate( prevStateMap ):
    newStateMap = copy.deepcopy( prevStateMap )

    for y in range(0, len(prevStateMap)):
        for x in range(0, len(prevStateMap[0])):        
            checkedSeat_ = prevStateMap[y][x]
            if checkedSeat_!='.':
                if checkAdjacentOccupacy(x,y, prevStateMap) == 0 and not isOccupied(checkedSeat_):
                    newSeatValue_ = '#'
                elif checkAdjacentOccupacy(x,y, prevStateMap) >= 4 and isOccupied(checkedSeat_):
                    newSeatValue_ = 'L'
                else:
                    newSeatValue_ = prevStateMap[y][x]

                newStateMap[y][x] = newSeatValue_

    return newStateMap

def areMapsIdentical(mapA, mapB):
    for y in range(0, len(mapA)):
        for x in range(0, len(mapA[0])):
            if mapA[y][x] != mapB[y][x]: return False
    return True

def totalOccupancy(checkMap):
    result = 0
    for y in range(0, len(checkMap)):
        for x in range(0, len(checkMap[0])):
           if isOccupied( checkMap[y][x] ): result+=1
    return result

testIfChanged = False
focusIteration = seatsMapIteration0

i = 0
while not testIfChanged:
    newIterationMap = iterate( focusIteration )

    testIfChanged = areMapsIdentical(focusIteration, newIterationMap)

    focusIteration = newIterationMap

    i+=1

print('Occupancy stopped at',totalOccupancy(focusIteration))
print('No change after',str(i-1),'th')