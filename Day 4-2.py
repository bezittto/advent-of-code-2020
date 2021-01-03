# --- Part Two ---

# The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!

# You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

#     byr (Birth Year) - four digits; at least 1920 and at most 2002.
#     iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#     eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#     hgt (Height) - a number followed by either cm or in:
#         If cm, the number must be at least 150 and at most 193.
#         If in, the number must be at least 59 and at most 76.
#     hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#     ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#     pid (Passport ID) - a nine-digit number, including leading zeroes.
#     cid (Country ID) - ignored, missing or not.

# Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:

# byr valid:   2002
# byr invalid: 2003

# hgt valid:   60in
# hgt valid:   190cm
# hgt invalid: 190in
# hgt invalid: 190

# hcl valid:   #123abc
# hcl invalid: #123abz
# hcl invalid: 123abc

# ecl valid:   brn
# ecl invalid: wat

# pid valid:   000000001
# pid invalid: 0123456789

# Here are some invalid passports:

# eyr:1972 cid:100
# hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

# iyr:2019
# hcl:#602927 eyr:1967 hgt:170cm
# ecl:grn pid:012533040 byr:1946

# hcl:dab227 iyr:2012
# ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

# hgt:59cm ecl:zzz
# eyr:2038 hcl:74454a iyr:2023
# pid:3556412378 byr:2007

# Here are some valid passports:

# pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f

# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022

# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719

# Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?

import re

mandatory1 = set( ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid'] )

#path = 'Day 4-input.txt'
path = 'Day 4-input2.txt'

with open(path,'r') as f:
    lines = [ l.replace('\n','') for l in f.readlines() ]

person_data = dict()
line_no = 1
valid_passports = 0
for l in lines:
    # collect
    for element in l.split(' '):
        if l =='': continue
        chunks = element.split(':')
        person_data[ chunks[0] ] = chunks[1].replace(' ','')

    if l == '' or line_no == len(lines):         
        # validate what was collected
        is_valid_ = True
        reasons_not_valid = list()

        gap = mandatory1 - set(person_data.keys())
        if len(gap)>0 and 'cid' not in gap: 
            is_valid_ = False
            reasons_not_valid.append('Missing parameter for common country')
        if len(gap)>1 and 'cid' in gap: 
            is_valid_ = False
            reasons_not_valid.append('Missing parameter for none-cid country')
       
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if 'byr' in person_data:
            try:
                if len(person_data['byr'])!=4 : 
                    is_valid_ = False
                    reasons_not_valid.append('byt str is not 4')
                
                checkbyr = int(person_data['byr'])
                if checkbyr < 1920 or checkbyr > 2002: 
                    is_valid_ = False
                    reasons_not_valid.append('byr not in allowed range')
            except:
                print('exception byr',line_no)
                is_valid_ = False

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if 'iyr' in person_data:
            try:
                if len(person_data['iyr'])!=4 : 
                    is_valid_ = False
                    reasons_not_valid.append('iyr str not 4')

                checkiyr = int(person_data['iyr'])
                if checkiyr < 2010 or checkiyr > 2020: 
                    is_valid_ = False
                    reasons_not_valid.append('iyr not in range')
            except:
                print('exception iyr',line_no)
                is_valid_ = False

        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if 'eyr' in person_data:
            try:
                if len(person_data['eyr'])!=4 : 
                    is_valid_ = False
                    reasons_not_valid.append('eyr str not 4')

                checkeyr = int(person_data['eyr'])
                if checkeyr < 2020 or checkeyr > 2030: 
                    is_valid_ = False
                    reasons_not_valid.append('eyr not in range')
            except:
                print('exception eyr',line_no)
                is_valid_ = False

        # hgt (Height) - a number followed by either cm or in:
        #     If cm, the number must be at least 150 and at most 193.
        #     If in, the number must be at least 59 and at most 76.
        if 'hgt' in person_data:
            try:
                checkhgt = person_data['hgt']

                if checkhgt.find('in')==-1 and checkhgt.find('cm')==-1:
                    is_valid_ = False
                    reasons_not_valid.append('in and cm not found')

                idx = checkhgt.find('cm') 
                if idx > -1:                    
                    checkhgtvalue = int(checkhgt[:idx])
                    if checkhgtvalue < 150 or checkhgtvalue > 193: 
                        is_valid_ = False
                        reasons_not_valid.append('hgt as cm not in range')
                idx = checkhgt.find('in')                
                if idx > -1:                    
                    checkhgtvalue = int(checkhgt[:idx])
                    if checkhgtvalue < 59 or checkhgtvalue > 76: 
                        is_valid_ = False
                        reasons_not_valid.append('hgt as inch not in range')
            except:
                print('exception hgt',line_no)
                is_valid_ = False

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if 'ecl' in person_data:
            try:
                checkecl = person_data['ecl']
                if len(checkecl)!=3 : 
                    is_valid_ = False
                    reasons_not_valid.append('ecl str len not 3')
                if checkecl not in [ 'amb','blu','brn','gry','grn','hzl','oth' ]: 
                    is_valid_ = False
                    reasons_not_valid.append('ecl not allowed')
            except:
                print('exception ecl',line_no)
                is_valid_ = False

        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        if 'pid' in person_data:
            try:
                checkpid = person_data['pid']
                pattern = '\d{9}'
                if len(checkpid)!=9 : 
                    is_valid_ = False
                    reasons_not_valid.append('pid str not 9')
                if not re.match(pattern, checkpid):
                    is_valid_ = False
                    reasons_not_valid.append('pid pattern mismatch')
                
            except:
                print('exception pid',line_no)
                is_valid_ = False

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if 'hcl' in person_data:
            try:
                checkhcl = person_data['hcl']
                pattern = '^#[a-f0-9]{6}'
                if len(checkhcl)!=7 : 
                    is_valid_ = False
                    reasons_not_valid.append('hcl str len not 7')
                if not re.match(pattern, checkhcl): 
                    is_valid_ = False
                    reasons_not_valid.append('hcl pattern mismatch')
                
            except:
                print('exception hcl',line_no)
                is_valid_ = False

        # cid (Country ID) - ignored, missing or not.
        pass

        valid_passports+=is_valid_

        # move to next
        person_data = dict()
        reasons_not_valid = list()

    line_no +=1 

print(valid_passports)

