# --- Part Two ---

# As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

# You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

# Using the same example as above:

# abc

# a
# b
# c

# ab
# ac

# a
# a
# a
# a

# b

# This list represents answers from five groups:

#     In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
#     In the second group, there is no question to which everyone answered "yes".
#     In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
#     In the fourth group, everyone answered yes to only 1 question, a.
#     In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.

# In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

# For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?


#path = 'Day 6-input.txt'
path = 'Day 6-input2.txt'

with open(path,'r') as f:
    lines = [ l.replace('\n','') for l in f.readlines() ]+['']

questions_sub = dict()
line_no = 1
questions_count = 0
linesblock = 0

for l in lines:
    if l == '':
        for k,v in questions_sub.items():
            if len(v) == linesblock: questions_count += 1
        
        linesblock = 0
        questions_sub = dict()
    else:
        for c in l:
            if c in questions_sub:
                questions_sub[c].append( line_no )
            else:
                questions_sub[c] = [ line_no ]
        linesblock +=1 

    line_no +=1 

print(questions_count)
