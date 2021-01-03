# --- Day 21: Allergen Assessment ---

# You reach the train's last stop and the closest you can get to your vacation island without getting wet. There aren't even any boats here, but nothing can stop you now: you build a raft. You just need a few days' worth of food for your journey.

# You don't speak the local language, so you can't read any ingredients lists. However, sometimes, allergens are listed in a language you do understand. You should be able to use this information to determine which ingredient contains which allergen and work out which foods are safe to take with you on your trip.

# You start by compiling a list of foods (your puzzle input), one food per line. Each line includes that food's ingredients list followed by some or all of the allergens the food contains.

# Each allergen is found in exactly one ingredient. Each ingredient contains zero or one allergen. Allergens aren't always marked; when they're listed (as in (contains nuts, shellfish) after an ingredients list), the ingredient that contains each listed allergen will be somewhere in the corresponding ingredients list. However, even if an allergen isn't listed, the ingredient that contains that allergen could still be present: maybe they forgot to label it, or maybe it was labeled in a language you don't know.

# For example, consider the following list of foods:

# mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)

# The first food in the list has four ingredients (written in a language you don't understand): mxmxvkd, kfcds, sqjhc, and nhms. While the food might contain other allergens, a few allergens the food definitely contains are listed afterward: dairy and fish.

# The first step is to determine which ingredients can't possibly contain any of the allergens in any food in your list. In the above example, none of the ingredients kfcds, nhms, sbzzf, or trh can contain an allergen. Counting the number of times any of these ingredients appear in any ingredients list produces 5: they all appear once each except sbzzf, which appears twice.

# Determine which ingredients cannot possibly contain any of the allergens in your list. How many times do any of those ingredients appear?

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
        if vv[k] == v: maxValuesForAllergensFoodTag.append( kk )


diff = set(foodList) - set(maxValuesForAllergensFoodTag)
#print( diff)

result = 0
for f in foodList:
    for d in diff:
        if d == f: result+=1
print(result)