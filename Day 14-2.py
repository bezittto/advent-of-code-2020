# --- Part Two ---

# For some reason, the sea port's computer system still can't communicate with your ferry's docking program. It must be using version 2 of the decoder chip!

# A version 2 decoder chip doesn't modify the values being written at all. Instead, it acts as a memory address decoder. Immediately before a value is written to memory, each bit in the bitmask modifies the corresponding bit of the destination memory address in the following way:

#     If the bitmask bit is 0, the corresponding memory address bit is unchanged.
#     If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
#     If the bitmask bit is X, the corresponding memory address bit is floating.

# A floating bit is not connected to anything and instead fluctuates unpredictably. In practice, this means the floating bits will take on all possible values, potentially causing many memory addresses to be written all at once!

# For example, consider the following program:

# mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000X0XX
# mem[26] = 1

# When this program goes to write to memory address 42, it first applies the bitmask:

# address: 000000000000000000000000000000101010  (decimal 42)
# mask:    000000000000000000000000000000X1001X
# result:  000000000000000000000000000000X1101X

# After applying the mask, four bits are overwritten, three of which are different, and two of which are floating. Floating bits take on every possible combination of values; with two floating bits, four actual memory addresses are written:

# 000000000000000000000000000000011010  (decimal 26)
# 000000000000000000000000000000011011  (decimal 27)
# 000000000000000000000000000000111010  (decimal 58)
# 000000000000000000000000000000111011  (decimal 59)

# Next, the program is about to write to memory address 26 with a different bitmask:

# address: 000000000000000000000000000000011010  (decimal 26)
# mask:    00000000000000000000000000000000X0XX
# result:  00000000000000000000000000000001X0XX

# This results in an address with three floating bits, causing writes to eight memory addresses:

# 000000000000000000000000000000010000  (decimal 16)
# 000000000000000000000000000000010001  (decimal 17)
# 000000000000000000000000000000010010  (decimal 18)
# 000000000000000000000000000000010011  (decimal 19)
# 000000000000000000000000000000011000  (decimal 24)
# 000000000000000000000000000000011001  (decimal 25)
# 000000000000000000000000000000011010  (decimal 26)
# 000000000000000000000000000000011011  (decimal 27)

# The entire 36-bit address space still begins initialized to the value 0 at every address, and you still need the sum of all values left in memory at the end of the program. In this example, the sum is 208.

# Execute the initialization program using an emulator for a version 2 decoder chip. What is the sum of all values left in memory after it completes?

from os import read
import re
import itertools

mask = ''
mem = {}

BITS = 36

def decimalToBinary(n):
    val =  bin(n).replace('0b','')
    prefix = ''.join( [ '0' for i in range( 0, BITS-len(val) ) ] )
    return prefix+val

def binaryToDecimal( value ):
    return int( value, 2)

def applyMask( pattern, value ):
    def do(x, y):
        if x=='0': return y
        if x=='1': return '1'
        return x

    temp = map( do, pattern, value) 
    temp = ''.join(list(temp))
    return temp

def getOptions(pattern,value):
    
    def replace(positions, chars, txt):
        txt = list(txt)
        for i,p in enumerate(positions):
            txt[p] = str(chars[i])
        return ''.join(txt)

    result = list()

    masked = applyMask(pattern,value)

    Xpositions = [x.start() for x in re.finditer('X', masked)]

    n = len(Xpositions)
    options = list(itertools.product([0, 1], repeat=n))

    for o in options:
        temp_ = replace(Xpositions, o, masked)
        result.append( temp_ )

    return result

with open('Day 14 - input.txt','r') as f:
    lines = f.read()
lines = lines.split('\n')

for l in lines:
    chk_ = l[:3]
    if chk_ == 'mas':
        newmask = l[7:]
        mask = newmask
    if chk_ == 'mem':        
        temp_ =  l.split('=')
        mvalue = int(temp_[1])
        idx1 = temp_[0].index('[')
        idx2 = temp_[0].index(']')
        mindx = int( temp_[0][idx1+1:idx2] )
        #
        a = decimalToBinary (mindx) 
        alloptions = getOptions(mask, a)
        for o in alloptions:
            
            d = binaryToDecimal( o )
            mem[d] = mvalue



result = 0
for k,v in mem.items(): result+=v

print(result)


