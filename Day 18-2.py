# --- Part Two ---

# You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when they reach the next section: advanced math.

# Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with. Instead, addition is evaluated before multiplication.

# For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now as follows:

# 1 + 2 * 3 + 4 * 5 + 6
#   3   * 3 + 4 * 5 + 6
#   3   *   7   * 5 + 6
#   3   *   7   *  11
#      21       *  11
#          231

# Here are the other examples from above:

#     1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
#     2 * 3 + (4 * 5) becomes 46.
#     5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
#     5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
#     ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.

# What do you get if you add up the results of evaluating the homework problems using these new rules?


import re

def evaluateBlock( block ):
    
    while True:
        plusPositions = [ x.start() for x in re.finditer( '\+' , block)]
        if len(plusPositions)>0:
            p = plusPositions[0]  

            subL  = block[:p]
            offsetL = -len(subL)
            for i in range(len(subL)):
                try:
                    if subL[-i-1] == '*': 
                        offsetL = -i
                        break
                except:
                    pass
            
            subR  = block[p+1:]
            offsetR = len(subR)
            for i in range(len(subR)):
                try:
                    if subR[i+1] == '*': 
                        offsetR = i+1
                        break
                except:
                    pass

            toevaluate = block[ p+offsetL:p+1+offsetR ]

            z = eval( toevaluate )        
            last = str(z)
            block = block[ :p+offsetL ]+ last +block[ p+1+offsetR: ]
        else: 
            break
    
    return str( eval(block) )

def solve( block ):
    block = block.replace(' ','')
    while True:
        theMostInnerBracketBlock = re.finditer(r"\([0-9.\+\*]*\)", block )
        theMostInnerBracketBlockPos = [ (i.start(), i.end() ) for i in theMostInnerBracketBlock ]  
        for b in theMostInnerBracketBlockPos[:1]:
            temp_ = block[ b[0]+1 : b[1]-1 ]
            e = evaluateBlock(temp_)
            block = block[ :b[0] ] + e + block[ b[1]: ]

        if len(theMostInnerBracketBlockPos) == 0: 
            block = evaluateBlock(block)
            break

        del(theMostInnerBracketBlockPos)
        del(theMostInnerBracketBlock)

    return int(block)

# tests = [
#     solve( '1 + 2 * 3 + 4 * 5 + 6') == 231
#      ,solve( '1 + (2 * 3) + (4 * (5 + 6))' ) == 51
#      ,solve( '2 * 3 + (4 * 5)' ) == 46
#      ,solve( '5 + (8 * 3 + 9 + 3 * 4 * 3)' ) == 1445
#      , solve( '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))' ) == 669060
#     , solve( '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2' ) == 23340
# ]

# print(tests)
# print(sum(tests))

result = 0
with open('Day 18-input.txt','r') as f:
    raw = f.readlines()

for l in raw:
    _ = l.replace('\n','')
    result+=solve(_)

print(result)

