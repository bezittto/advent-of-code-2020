# --- Part Two ---

# Now that you've isolated the inert ingredients, you should have enough information to figure out which ingredient contains which allergen.

# In the above example:

#     mxmxvkd contains dairy.
#     sqjhc contains fish.
#     fvjkl contains soy.

# Arrange the ingredients alphabetically by their allergen and separate them by commas to produce your canonical dangerous ingredient list. (There should not be any spaces in your canonical dangerous ingredient list.) In the above example, this would be mxmxvkd,sqjhc,fvjkl.

# Time to stock your raft with supplies. What is your canonical dangerous ingredient list?

fpath = 'Day21-input2.txt'

with open(fpath,'r') as f:
    raw = f.read().split('\n')

import re

findpattern = '\((contains.+)\)'

allergensList = list()
foodList = list()
data = list()

for r in raw:
    if len(r) == 0: continue

    _ = re.search( findpattern, r )
    araw = _.groups()[0]
    araw = araw[len('contains '):].replace(' ','')
    allergens = araw.split(',')

    allergensList.extend(allergens)
    
    food = r[:r.find('(')].strip().split(' ')

    foodList.extend(food)

    data.append( ( food, allergens ))

allergensList = set(allergensList)

foodListCounter = { f:{ a:0 for a in allergensList } for f in set(foodList) }
maxValuesForAllergens = { a:0 for a in allergensList }
maxValuesForAllergensFoodTag = list()

for d in data:
    for f in d[0]:
        q_ = 1/len(d[0])
        for a in d[1]:
            foodListCounter[f][a] += q_

            if maxValuesForAllergens[a] < foodListCounter[f][a]:
                maxValuesForAllergens[a] = foodListCounter[f][a]

for k,v in maxValuesForAllergens.items():
    for kk,vv in foodListCounter.items():
        if vv[k] == v: maxValuesForAllergensFoodTag.append( (kk,k, vv[k]) )


def getAllergenByI( i ):
    for t in maxValuesForAllergensFoodTag:
        if t[0] == i: return t[1]

matchedItems = dict()

while True:
    iCounter = dict()
    for t in maxValuesForAllergensFoodTag:
        if t[0] not in iCounter:
            iCounter[t[0]] = 1
        else:
            iCounter[t[0]] += 1

    matchedSomething = False
    for k,v in iCounter.items():
        if v==1:
            matchedIngredient = k
            matchedAllergen = getAllergenByI(matchedIngredient)
            matchedItems[ matchedAllergen ] = matchedIngredient
            
            toberemoved = list()
            for j in range(len(maxValuesForAllergensFoodTag)):
                    if maxValuesForAllergensFoodTag[j][1] == matchedAllergen:
                        toberemoved.append( maxValuesForAllergensFoodTag[j] )
            
            for t in toberemoved:
                maxValuesForAllergensFoodTag.remove( t )

            matchedSomething = True 

    if not matchedSomething:
        break


#print( matchedItems )

result = [ val for key, val in sorted(matchedItems.items(), key = lambda ele: ele[0]) ]

resulttext = ','.join(result) 

print(resulttext)

