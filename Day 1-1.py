# --- Day 1: Report Repair ---

# After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

# The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

# To save your vacation, you need to get all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

# For example, suppose your expense report contained the following:

# 1721
# 979
# 366
# 299
# 675
# 1456

# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

# Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?


# numberstocheck = [ 1721, 979, 366, 299, 675, 1456 ]

numberstocheck = [
1036,
1897,
1256,
1080,
1909,
1817,
1759,
1883,
1088,
1841,
1780,
1907,
1874,
1831,
1932,
1999,
1989,
1840,
1973,
1102,
1906,
1277,
1089,
1275,
1228,
1917,
1075,
1060,
1964,
1942,
2001,
1950,
1181,
1121,
1854,
1083,
1772,
1481,
1976,
1805,
1594,
1889,
1726,
1866,
798,
1739,
1709,
1946,
1948,
1808,
1836,
1849,
1465,
1066,
1943,
664,
1894,
1993,
1061,
1225,
1589,
1916,
1885,
1998,
1470,
1668,
1666,
1499,
1437,
1986,
1127,
1875,
1132,
1888,
1877,
1046,
1982,
1265,
1757,
1848,
1786,
1638,
1958,
1015,
1013,
1552,
1742,
1850,
1016,
1839,
558,
1826,
1261,
1988,
1545,
1078,
1963,
1967,
1951,
1086,
1947,
1880,
1903,
1994,
1167,
1736,
1041,
1652,
1040,
1033,
1179,
1844,
1861,
1488,
1962,
1135,
1347,
1187,
1777,
1598,
1803,
1147,
1760,
1926,
1898,
1923,
1865,
1313,
1924,
1023,
1576,
1715,
1391,
1346,
1882,
2000,
1024,
1143,
1065,
1560,
1029,
1119,
1966,
1022,
1931,
1512,
1049,
1929,
1312,
1069,
1159,
1053,
1249,
1074,
1983,
1761,
1868,
195,
24,
1331,
1636,
1020,
1034,
1671,
708,
1699,
1900,
1927,
1829,
301,
1832,
1042,
1896,
1928,
1032,
1992,
2005,
1955,
1047,
1068,
1001,
1052,
1744,
1845,
1208,
1018,
1859,
1342,
1823,
1758,
2007,
1241,
1893,
1876,
1984,
1655,
1534,
1150,
1789,
1870
]

def check(a, b):
    if a + b == 2020: return a*b
    return None

def detect(numbers):
    for i,v1 in enumerate( numbers ):        
        for j in range( i+1, len(numbers) ):
            t1 = check( numbers[i], numbers[j] )
            if t1 is not None: return t1
            t2 = check( numbers[ -(i+1) ], numbers[-(j+1)] )
            if t2 is not None: return t2         

result = detect(numberstocheck)

print( result )
