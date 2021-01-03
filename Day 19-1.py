# --- Day 19: Monster Messages ---

# You land in an airport surrounded by dense forest. As you walk to your high-speed train, the Elves at the Mythical Information Bureau contact you again. They think their satellite has collected an image of a sea monster! Unfortunately, the connection to the satellite is having problems, and many of the messages sent back from the satellite have been corrupted.

# They sent you a list of the rules valid messages should obey and a list of received messages they've collected so far (your puzzle input).

# The rules for valid messages (the top part of your puzzle input) are numbered and build upon each other. For example:

# 0: 1 2
# 1: "a"
# 2: 1 3 | 3 1
# 3: "b"

# Some rules, like 3: "b", simply match a single character (in this case, b).

# The remaining rules list the sub-rules that must be followed; for example, the rule 0: 1 2 means that to match rule 0, the text being checked must match rule 1, and the text after the part that matched rule 1 must then match rule 2.

# Some of the rules have multiple lists of sub-rules separated by a pipe (|). This means that at least one list of sub-rules must match. (The ones that match might be different each time the rule is encountered.) For example, the rule 2: 1 3 | 3 1 means that to match rule 2, the text being checked must match rule 1 followed by rule 3 or it must match rule 3 followed by rule 1.

# Fortunately, there are no loops in the rules, so the list of possible matches will be finite. Since rule 1 matches a and rule 3 matches b, rule 2 matches either ab or ba. Therefore, rule 0 matches aab or aba.

# Here's a more interesting example:

# 0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"

# Here, because rule 4 matches a and rule 5 matches b, rule 2 matches two letters that are the same (aa or bb), and rule 3 matches two letters that are different (ab or ba).

# Since rule 1 matches rules 2 and 3 once each in either order, it must match two pairs of letters, one pair with matching letters and one pair with different letters. This leaves eight possibilities: aaab, aaba, bbab, bbba, abaa, abbb, baaa, or babb.

# Rule 0, therefore, matches a (rule 4), then any of the eight options from rule 1, then b (rule 5): aaaabb, aaabab, abbabb, abbbab, aabaab, aabbbb, abaaab, or ababbb.

# The received messages (the bottom part of your puzzle input) need to be checked against the rules so you can determine which are valid and which are corrupted. Including the rules and the messages together, this might look like:

# 0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"

# ababbb
# bababa
# abbbab
# aaabbb
# aaaabbb

# Your goal is to determine the number of messages that completely match rule 0. In the above example, ababbb and abbbab match, but bababa, aaabbb, and aaaabbb do not, producing the answer 2. The whole message must match all of rule 0; there can't be extra unmatched characters in the message. (For example, aaaabbb might appear to match rule 0 above, but it has an extra unmatched b on the end.)

# How many messages completely match rule 0?


fpath = 'Day 19-input2.txt'

# read and parse input
with open(fpath,'r') as f:
    raw = f.readlines()

raw = [ x.replace('\n','') for x in raw ]

rules = dict()
messages = list()
for r in raw:
    if len(r) == 0: continue
    if r.find(':') > -1:
        parts = r.split(':')
        idx = int(parts[0])
        rules[idx]= parts[1].strip().replace('"','')
    else:
        messages.append(r)

import re

def buildRule( currentCode, allrules ):
    def applyOrBrackets( c ):
        result = ''
        if c.find('|') > -1: 
            parts = c.split('|')
            result = ' ( '            
            result += ' ( ' + parts[0] + ' ) | ( ' + parts[1] + ' ) '
            result += ' ) '
        else:
            result = c
        return result

    def parseCodes( r ):
        result = ''
        parsed = r.split(' ')
        for p in parsed:
            if p=='|' or p==')' or p=='(':
                result += p
            else:
                if len(p)>0:
                    if p.isalpha():
                        result += p 
                    else:
                        chk_ = allrules[ int(p) ]
                        result += applyOrBrackets( chk_  )
                        zzzzzzz =0
                        pass
            result += ' '

        return result.strip() 

    def isDigitPresent( r ):
        for c in r:
            if c.isdigit(): return True
        return False

    result_ = parseCodes( currentCode ) 
    test_ = isDigitPresent(result_)

    if test_:
        buildRule( result_, allrules )
    else:
        result_ = result_.replace(' ','')
        #print(result_)

buildRule( rules[0], rules )

rule = 'a((((aa)|(bb))((ab)|(ba)))|(((ab)|(ba))((aa)|(bb))))b'

rule='((((((b((((a((a)|(b))((a((a)|(b)))|(bb)))|(b((a((ba)|(ab)))|(bab))))b)|(((((aaa)|(b((b((a)|(b)))|(ab))))a)|(((bba)|(a((aa)|(ab))))b))a)))|(a((a((b((((ba)|(a((a)|(b))))a)|(((ba)|(bb))b)))|(a((b((a)|(b))((a)|(b)))|(aba)))))|(b((b((a((ba)|(bb)))|(b((a)|(b))((a)|(b)))))|(a((aab)|(b((aa)|(ab))))))))))b)|(((b((a((((aba)|(abb))b)|(((aaa)|(abb))a)))|(b((((((a((a)|(b)))|(bb))b)|(((ba)|(bb))a))b)|(((a((aa)|(b((a)|(b)))))|(bab))a)))))|(a((((b((aba)|(aab)))|(a((bba)|(bab))))a)|(((b((a((ba)|(bb)))|(b((ba)|(a((a)|(b)))))))|(a((b((a((a)|(b)))|(bb)))|(a((a)|(b))((a)|(b))))))b))))a))a)|(((((a((((b((b((ba)|(a((a)|(b)))))|(aab)))|(a((((a((a)|(b)))|(bb))a)|(aab))))a)|(((((a((aa)|(ab)))|(b((ba)|(a((a)|(b))))))a)|(((baa)|(abb))b))b)))|(b((((a((b((aa)|(b((a)|(b)))))|(aba)))|(b((bbb)|(a((ba)|(ab))))))a)|(((b((b((aa)|(b((a)|(b)))))|(aba)))|(a((aab)|(bab))))b))))a)|(((b((a((b((b((ba)|(ab)))|(a((aa)|(b((a)|(b)))))))|(a((aba)|(aab)))))|(b((b((b((ba)|(ab)))|(a((aa)|(b((a)|(b)))))))|(a((a)|(b))((aa)|(b((a)|(b)))))))))|(a((a((b((b((a((a)|(b)))|(bb)))|(aaa)))|(a((a((a((a)|(b)))|(bb)))|(b((ba)|(bb)))))))|(b((((a((ba)|(a((a)|(b)))))|(bab))b)|(((((aa)|(b((a)|(b))))b)|(((ba)|(ab))a))a))))))b))b))((((((b((((a((a)|(b))((a((a)|(b)))|(bb)))|(b((a((ba)|(ab)))|(bab))))b)|(((((aaa)|(b((b((a)|(b)))|(ab))))a)|(((bba)|(a((aa)|(ab))))b))a)))|(a((a((b((((ba)|(a((a)|(b))))a)|(((ba)|(bb))b)))|(a((b((a)|(b))((a)|(b)))|(aba)))))|(b((b((a((ba)|(bb)))|(b((a)|(b))((a)|(b)))))|(a((aab)|(b((aa)|(ab))))))))))b)|(((b((a((((aba)|(abb))b)|(((aaa)|(abb))a)))|(b((((((a((a)|(b)))|(bb))b)|(((ba)|(bb))a))b)|(((a((aa)|(b((a)|(b)))))|(bab))a)))))|(a((((b((aba)|(aab)))|(a((bba)|(bab))))a)|(((b((a((ba)|(bb)))|(b((ba)|(a((a)|(b)))))))|(a((b((a((a)|(b)))|(bb)))|(a((a)|(b))((a)|(b))))))b))))a))a)|(((((a((((b((b((ba)|(a((a)|(b)))))|(aab)))|(a((((a((a)|(b)))|(bb))a)|(aab))))a)|(((((a((aa)|(ab)))|(b((ba)|(a((a)|(b))))))a)|(((baa)|(abb))b))b)))|(b((((a((b((aa)|(b((a)|(b)))))|(aba)))|(b((bbb)|(a((ba)|(ab))))))a)|(((b((b((aa)|(b((a)|(b)))))|(aba)))|(a((aab)|(bab))))b))))a)|(((b((a((b((b((ba)|(ab)))|(a((aa)|(b((a)|(b)))))))|(a((aba)|(aab)))))|(b((b((b((ba)|(ab)))|(a((aa)|(b((a)|(b)))))))|(a((a)|(b))((aa)|(b((a)|(b)))))))))|(a((a((b((b((a((a)|(b)))|(bb)))|(aaa)))|(a((a((a((a)|(b)))|(bb)))|(b((ba)|(bb)))))))|(b((((a((ba)|(a((a)|(b)))))|(bab))b)|(((((aa)|(b((a)|(b))))b)|(((ba)|(ab))a))a))))))b))b))((((a((((a((((abb)|(b((a((a)|(b)))|(bb))))a)|(((((ba)|(bb))a)|(((ba)|(a((a)|(b))))b))b)))|(b((a((bbb)|(((aa)|(b((a)|(b))))a)))|(b((b((b((a)|(b)))|(ab)))|(abb))))))a)|(((b((((a((bb)|(aa)))|(bba))a)|(((((ab)|(bb))b)|(((ba)|(bb))a))b)))|(a((a((b((aa)|(ab)))|(aba)))|(b((bba)|(a((b((a)|(b)))|(ab))))))))b)))|(b((((((((bbb)|(((aa)|(b((a)|(b))))a))a)|(((b((ba)|(ab)))|(a((ba)|(a((a)|(b))))))b))a)|(((a((a)|(b))((aa)|(b((a)|(b)))))|(b((aaa)|(((ba)|(a((a)|(b))))b))))b))a)|(((((((a((ba)|(ab)))|(b((ba)|(a((a)|(b))))))a)|(((((a((a)|(b)))|(bb))b)|(aaa))b))b)|(((aabb)|(((((a((a)|(b)))|(bb))b)|(aaa))a))a))b))))b)|(((((b((b((((((aa)|(b((a)|(b))))a)|(((ab)|(bb))b))b)|(((((a((a)|(b)))|(bb))b)|(aaa))a)))|(a((((b((a)|(b))((a)|(b)))|(aba))a)|(((aba)|(bba))b)))))|(a((a((((a)|(b))((aa)|(ab))b)|(((bbb)|(aaa))a)))|(b((((baa)|(a((a((a)|(b)))|(bb))))a)|(((((aa)|(ab))b)|(baa))b))))))b)|(((((a((((baa)|(abb))a)|(((baa)|(bbb))b)))|(b((a((b((a)|(b))((a)|(b)))|(a((aa)|(ab)))))|(b((bab)|(((aa)|(ab))a))))))b)|(((b((a((b((a)|(b))((a)|(b)))|(a((ba)|(ab)))))|(b((b((aa)|(b((a)|(b)))))|(aab)))))|(a((((b((b((a)|(b)))|(ab)))|(a((a((a)|(b)))|(bb))))b)|(((b((aa)|(b((a)|(b)))))|(a((ba)|(a((a)|(b))))))a))))a))a))a))'

counter = 0
for m in messages:
    test = re.fullmatch( rule, m )
    if test: counter+=1
   

print(counter)
