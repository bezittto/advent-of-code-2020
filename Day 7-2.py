# --- Part Two ---

# It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

# Consider again your shiny gold bag and the rules from the above example:

#     faded blue bags contain 0 other bags.
#     dotted black bags contain 0 other bags.
#     vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
#     dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.

# So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

# Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

# Here's another example:

# shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.

# In this example, a single shiny gold bag must contain 126 other bags.

# How many individual bags are required inside your single shiny gold bag?


feed = [
'light red bags contain 1 bright white bag, 2 muted yellow bags.',
'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
'bright white bags contain 1 shiny gold bag.',
'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
'faded blue bags contain no other bags.',
'dotted black bags contain no other bags.'
]
path = 'Day 7-input2.txt'
with open(path,'r') as f:
    feed = [ l.replace('\n','') for l in f.readlines() ]+['']

class Helper:
    def xtract( sentence ):
        chunks = sentence.split('contain')
        owner = chunks[0].replace(' bags ','')
        ownees_raw = chunks[1].split(',')
        ownees = list()
        volumes = list()
        for oraw in ownees_raw:
            _ = oraw.split(' ')
            if len(_) == 5: 
                ownees.append(_[2]+' '+_[3])
                volumes.append( int(_[1]) )

        return owner, ownees, volumes

class Graph:

    nodes = None

    class Node:
        directOwners = list()
        volumesByOwner = list()

        def __init__( self, title, directOwners=None, volumes=None ):
            self.title = title     

            if directOwners is None: directOwners = list() 
            self.directOwners = directOwners

            if volumes is None: volumes = list() 
            self.volumesByOwner = volumes

        def addOwner(self, owner, volume ):            
            self.directOwners.append( owner )
            self.volumesByOwner.append( volume )

    def __init__(self):
        self.nodes = list()

    def getNodeByTitle( self, title ):
        for n in self.nodes:
            if n.title == title: return n
        return None

    def addNode(self, title):
        newNode = self.Node(title,None)
        self.nodes.append(newNode)
        return newNode

    def getExistingOrCreateNewNode(self, title):
        node = self.getNodeByTitle(title)
        if node is None:            
            newNode = self.Node(title)
            self.nodes.append(newNode)
            return newNode
        return node

    def addNodeFromTitles( self, title, owner, volume ):
        node = self.getExistingOrCreateNewNode(title)
        node.addOwner( self.getExistingOrCreateNewNode(owner), volume  )
        
    def getSize(self, title):
        colors = []
        n = self.getNodeByTitle(title)
        if n is not None:
            owners = n.directOwners
            colors+= [title]
            if len(owners) == 0:                
                return colors
            for o in owners: colors += self.getSize(o.title)
        return colors

    def getVolume(self, title):
        vol = 1
        n = self.getNodeByTitle(title)
        if n is not None:
            owners = n.directOwners
            volumes= n.volumesByOwner
            if len(owners) == 0: return vol            
            for o,v in zip(owners, volumes): 
                vol += v * self.getVolume(o.title)
        return vol

g = Graph()

for f in feed:
    if len(f)>0:
        owner, owned, volumes = Helper.xtract( f )
        for ownedElement, volumesElement in zip(owned, volumes):
            # had to reverse order of owner and ownedelement passed as arugments, agaisnt -1, because despite of naming of elemnts in Graph classes, reality is vice versa, owner is owned!
            g.addNodeFromTitles( owner, ownedElement, volumesElement )

focus = 'shiny gold'

result0 = g.getVolume(focus)
print( result0-1 )