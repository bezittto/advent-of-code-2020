# --- Part Two ---

# After some careful analysis, you believe that exactly one instruction is corrupted.

# Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)

# The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

# For example, consider the same program from above:

# nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6

# If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually find another jmp instruction and loop forever.

# However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions are visited in this order:

# nop +0  | 1
# acc +1  | 2
# jmp +4  | 3
# acc +3  |
# jmp -3  |
# acc -99 |
# acc +1  | 4
# nop -4  | 5
# acc +6  | 6

# After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last instruction in the file. With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).

# Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?


path = 'Day 8-input2.txt'

with open(path,'r') as f:
    feed = [ l.replace('\n','') for l in f.readlines() ]+['']

def parseLine( line ):
    command = line.split(' ')
    return command[0], command[1]

def engine( feed ):    
    lineCounter = { x:False for x in range(0,len(feed)) }
    accValue = 0

    currentLine = 0

    testOK = False

    while( not lineCounter[currentLine] and currentLine<len(feed)-1 ):
        lineCounter[currentLine] = True
        
        command, param = parseLine( feed[currentLine] )

        #currentLine+=1
        if command == 'nop': 
            currentLine+=1
        if command == 'acc': 
            accValue+=int(param)
            currentLine+=1
        if command == 'jmp': 
            currentLine+=int(param)
    
    if currentLine == len(feed)-1:
        testOK = True

    return accValue, testOK

lineCounter = { x:False for x in range(0,len(feed)) }
currentLine = 0
linesWithJmp = []
linesWithNop = []
while( not lineCounter[currentLine] and currentLine<len(feed)-1 ):
    lineCounter[currentLine] = True
    command, param = parseLine( feed[currentLine] )

    if command == 'jmp' and int(param)>0: linesWithJmp.append(currentLine)
    if command == 'nop' and int(param)!=0: linesWithNop.append(currentLine)

    currentLine+=1

for x in linesWithJmp:
    feed2_ = feed.copy()
    feed2_[x] = feed2_[x].replace('jmp','nop')
    
    acc, test = engine( feed2_ )
    if test: 
        result = acc
        print('jmp to nop', result)
        break

for x in linesWithNop:
    feed2_ = feed.copy()
    feed2_[x] = feed2_[x].replace('nop','jmp')

    acc, test = engine( feed2_ )
    if test: 
        result = acc
        print('nop to jmp', result)
        break
