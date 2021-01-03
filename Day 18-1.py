# --- Day 18: Operation Order ---

# As you look out the window and notice a heavily-forested continent slowly appear over the horizon, you are interrupted by the child sitting next to you. They're curious if you could help them with their math homework.

# Unfortunately, it seems like this "math" follows different rules than you remember.

# The homework (your puzzle input) consists of a series of expressions that consist of addition (+), multiplication (*), and parentheses ((...)). Just like normal math, parentheses indicate that the expression inside must be evaluated before it can be used by the surrounding expression. Addition still finds the sum of the numbers on both sides of the operator, and multiplication still finds the product.

# However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition, the operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.

# For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows:

# 1 + 2 * 3 + 4 * 5 + 6
#   3   * 3 + 4 * 5 + 6
#       9   + 4 * 5 + 6
#          13   * 5 + 6
#              65   + 6
#                  71

# Parentheses can override this order; for example, here is what happens if parentheses are added to form 1 + (2 * 3) + (4 * (5 + 6)):

# 1 + (2 * 3) + (4 * (5 + 6))
# 1 +    6    + (4 * (5 + 6))
#      7      + (4 * (5 + 6))
#      7      + (4 *   11   )
#      7      +     44
#             51

# Here are a few more examples:

#     2 * 3 + (4 * 5) becomes 26.
#     5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
#     5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
#     ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.

# Before you can help with the homework, you need to understand it yourself. Evaluate the expression on each line of the homework; what is the sum of the resulting values?


import re

def evaluateBlock( block ):
    block = block.replace(' ','')

    operationsPositions = [0]+sorted( [ x.start() for x in re.finditer( '\+' , block)] + [x.start() for x in re.finditer( '\*' , block)] )

    last = ''

    for i,o in enumerate(operationsPositions):
        if i+1<len(operationsPositions):
            until = operationsPositions[i+1]
        else:
            until = len(block)

        toevaluate = last+block[ o : until ]
        z = eval( toevaluate )        
        last = str(z)
    
    return last

def solve( block ):
    block = block.replace(' ','')
    while True:
        theMostInnerBracketBlock = re.finditer(r"\([0-9.\+\*]*\)", block )
        theMostInnerBracketBlockPos = [ (i.start(), i.end() ) for i in theMostInnerBracketBlock ]  
        for b in theMostInnerBracketBlockPos[:1]:
            temp_ = block[ b[0]+1 : b[1]-1 ]
            e = evaluateBlock(temp_)
            block = block[:b[0]] + e + block[ b[1]: ]

        if len(theMostInnerBracketBlockPos) == 0: 
            block = evaluateBlock(block)
            break

        theMostInnerBracketBlockPos = None
        theMostInnerBracketBlock = None

    return int(block)

tests = [
    solve( '1 + 2 * 3 + 4 * 5 + 6') == 71,
    solve( '1 + (2 * 3) + (4 * (5 + 6))' ) == 51,
    solve( '2 * 3 + (4 * 5)' ) == 26,
    solve( '5 + (8 * 3 + 9 + 3 * 4 * 3)' ) == 437,
    solve( '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))' ) == 12240,
    solve( '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2' ) == 13632
]

# print(tests)
# print(sum(tests))

result = 0
with open('Day 18-input.txt','r') as f:
    raw = f.readlines()

for l in raw:
    _ = l.replace('\n','')
    result+=solve(_)

print(result)