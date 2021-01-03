# --- Part Two ---

# Impressed, the Elves issue you a challenge: determine the 30000000th number spoken. For example, given the same starting numbers as above:

#     Given 0,3,6, the 30000000th number spoken is 175594.
#     Given 1,3,2, the 30000000th number spoken is 2578.
#     Given 2,1,3, the 30000000th number spoken is 3544142.
#     Given 1,2,3, the 30000000th number spoken is 261214.
#     Given 2,3,1, the 30000000th number spoken is 6895259.
#     Given 3,2,1, the 30000000th number spoken is 18.
#     Given 3,1,2, the 30000000th number spoken is 362.

# Given your starting numbers, what will be the 30000000th number spoken?

def speak( numbers, targetPoistion ):
    def updatePositions( lst, i ):
        lst.append(i)
        if len(lst)>2: return lst[-2:]
        return lst

    firstTimers = dict()
    spoken = list()
    for i,n in enumerate( numbers ):
        spoken.append(n)
        firstTimers[n] = [ i+1 ]

    for i in range( len(numbers)+1, targetPoistion+1 ):
        if i%1000000 ==0: print('Status pct', str(i/(targetPoistion+1)*100))
        
        focus_ = spoken[-1]
        if focus_ not in firstTimers: 
            spoken.append(0)
            firstTimers[ 0 ] = updatePositions( firstTimers[ 0 ], i )
        elif focus_ in firstTimers:
            if len( firstTimers[ focus_ ] ) == 1:
                spoken.append(0)

                if 0 in firstTimers:
                    firstTimers[0] = updatePositions( firstTimers[0], i )
                else:
                    firstTimers[0]=[i]         
            else:
                delta = firstTimers[focus_][1] - firstTimers[focus_][0]
                spoken.append(delta)
                if delta in firstTimers:
                    firstTimers[delta] = updatePositions( firstTimers[delta], i )
                else:
                    firstTimers[delta]=[i]

    return spoken[-1]

#tests = list()
#tests.append( speak( [0,3,6], 30000000) == 175594 )
# tests.append( speak( [1,3,2], 30000000) == 2578 )
# tests.append( speak( [2,1,3], 30000000) == 3544142 )
# tests.append( speak( [1,2,3], 30000000) == 261214 )
# tests.append( speak( [2,3,1], 30000000) == 6895259 )
# tests.append( speak( [3,2,1], 30000000) == 362 )
# tests.append( speak( [3,1,2], 30000000) == 1836 )
#print(tests)
#print( sum(tests)==len(tests) )

test2 = speak([13,0,10,12,1,5,8], 30000000)
print(test2)