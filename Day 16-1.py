# --- Day 16: Ticket Translation ---

# As you're walking to yet another connecting flight, you realize that one of the legs of your re-routed trip coming up is on a high-speed train. However, the train ticket you were given is in a language you don't understand. You should probably figure out what it says before you get to the train station after the next flight.

# Unfortunately, you can't actually read the words on the ticket. You can, however, read the numbers, and so you figure out the fields these tickets must have and the valid ranges for values in those fields.

# You collect the rules for ticket fields, the numbers on your ticket, and the numbers on other nearby tickets for the same train service (via the airport security cameras) together into a single document you can reference (your puzzle input).

# The rules for ticket fields specify a list of fields that exist somewhere on the ticket and the valid ranges of values for each field. For example, a rule like class: 1-3 or 5-7 means that one of the fields in every ticket is named class and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3 and 5 are both valid in this field, but 4 is not).

# Each ticket is represented by a single line of comma-separated values. The values are the numbers on the ticket in the order they appear; every ticket has the same format. For example, consider this ticket:

# .--------------------------------------------------------.
# | ????: 101    ?????: 102   ??????????: 103     ???: 104 |
# |                                                        |
# | ??: 301  ??: 302             ???????: 303      ??????? |
# | ??: 401  ??: 402           ???? ????: 403    ????????? |
# '--------------------------------------------------------'

# Here, ? represents text in a language you don't understand. This ticket might be represented as 101,102,103,104,301,302,303,401,402,403; of course, the actual train tickets you're looking at are much more complicated. In any case, you've extracted just the numbers in such a way that the first number is always the same specific field, the second number is always a different specific field, and so on - you just don't know what each position actually means!

# Start by determining which tickets are completely invalid; these are tickets that contain values which aren't valid for any field. Ignore your ticket for now.

# For example, suppose you have the following notes:

# class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50

# your ticket:
# 7,1,14

# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12

# It doesn't matter which position corresponds to which field; you can identify invalid nearby tickets by considering only whether tickets contain values that are not valid for any field. In this example, the values on the first nearby ticket are all valid for at least one field. This is not true of the other three nearby tickets: the values 4, 55, and 12 are are not valid for any field. Adding together all of the invalid values produces your ticket scanning error rate: 4 + 55 + 12 = 71.

# Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?



input_data = {
'rules': {
    'departure location': [ ( 44,825 ),( 849,962 ) ],
    'departure station': [ ( 26,296 ),( 316,965 )],
    'departure platform':[ ( 46,889 ),( 896,949 )],
    'departure track':[(  48,351 ),( 369,960 )],
    'departure date':[ ( 25,869 ),( 884,966 )],
    'departure time':[ ( 31,217 ),( 232,956 ) ],
    'arrival location':[ ( 32,559 ),( 574,967)],
    'arrival station': [ ( 50,383 ),( 394,952 )],
    'arrival platform': [ ( 29,128 ),( 150,962 )],
    'arrival track':[ ( 30,630 ),( 647,957 )],
    'class': [ ( 45,262 ),( 277,966 )],
    'duration': [ ( 35,602 ),( 619,965 )],
    'price':  [ ( 41,913 ),( 926,966 )],
    'route': [ ( 38,191 ),( 212,950 )],
    'row':[ (  25,509 ),( 523,965 )],
    'seat': [ ( 39,783 ),( 802,973 )],
    'train': [ ( 36,64 ),( 80,969 )],
    'type': [ (  42,750 ),( 767,974 )],
    'wagon': [ ( 29,803 ),( 821,974 )],
    'zone': [ ( 47,659 ),( 672,968 )] 
},
'your ticket': [ 157,101,107,179,181,163,191,109,97,103,89,113,167,127,151,53,83,61,59,173 ],
'nearby tickets': [ 
 [252,432,61,105,442,938,451,676,141,598,236,255,157,328,424,746,379,688,478,181],
[317,559,396,106,435,554,324,55,260,245,126,540,13,775,675,346,296,931,121,107],
[699,862,476,178,548,546,711,889,529,441,929,286,335,258,339,934,377,598,756,591],
[119,906,423,316,949,494,88,458,741,285,260,707,601,296,598,94,766,535,82,710],
[181,868,105,595,471,136,292,238,414,427,537,348,718,442,324,656,938,452,488,648],
[234,487,554,290,886,479,214,692,413,720,949,430,656,96,104,797,446,480,409,449],
[908,401,896,856,116,550,455,438,580,242,802,629,58,342,867,423,58,542,583,800],
[88,437,585,113,428,853,555,945,548,295,262,628,436,718,472,775,931,446,402,996],
[906,906,487,942,433,912,673,901,822,416,482,496,894,440,712,698,912,674,673,321],
[258,86,748,695,770,586,509,178,561,530,735,716,351,649,652,215,710,151,931,714],
[99,822,451,400,290,556,80,862,600,856,83,767,938,464,258,853,295,225,239,406],
[780,114,857,165,602,581,244,672,489,69,586,80,725,104,58,51,888,91,215,375],
[232,724,166,469,546,701,783,673,166,506,706,126,682,255,897,942,252,101,2,157],
[485,158,160,703,543,930,248,474,912,452,101,840,623,287,463,235,625,654,213,529],
[863,801,277,681,408,732,778,348,159,322,694,463,82,528,405,706,186,901,768,626],
[461,551,406,170,532,160,576,257,942,22,181,85,480,526,85,169,594,80,349,290],
[441,345,495,598,102,649,171,156,744,497,459,740,463,999,215,187,683,850,465,911],
[157,454,345,465,253,481,279,945,468,101,498,93,467,477,724,652,75,216,452,285],
[253,161,718,939,406,374,231,479,327,536,904,87,50,680,930,475,287,233,590,119],
[91,340,492,321,688,797,720,475,488,491,341,744,541,621,587,115,508,779,701,320],
[189,739,102,84,230,182,727,749,402,731,928,253,911,81,351,403,935,455,898,887],
[100,435,943,246,288,117,369,865,700,932,852,947,852,410,620,698,96,563,425,189],
[940,778,286,322,693,410,541,781,709,232,215,405,120,505,459,61,455,659,769,365],
[106,579,449,942,683,544,150,740,66,395,177,483,185,415,680,853,402,423,316,166],
[161,476,357,257,400,861,395,343,714,86,866,64,183,106,733,55,901,61,697,685],
[159,459,770,577,594,53,497,5,250,476,54,372,281,542,445,493,655,317,933,247],
[860,109,418,282,429,585,949,16,933,948,593,949,704,599,496,447,863,236,320,99],
[505,470,896,414,233,182,433,770,734,898,57,296,942,450,777,411,373,107,296,915],
[445,902,718,60,908,747,408,57,189,96,689,322,177,588,256,684,167,287,938,892],
[550,283,56,948,479,80,452,927,433,295,195,482,702,906,80,744,724,453,689,426],
[376,906,701,689,324,709,453,461,202,437,897,913,244,459,620,472,318,178,291,159],
[343,653,410,473,54,716,629,770,607,371,782,123,556,466,408,738,926,771,452,282],
[325,462,681,155,902,770,547,558,774,102,326,542,595,235,858,331,523,765,377,899],
[745,278,128,250,928,397,889,472,596,454,248,996,60,99,783,465,376,586,122,405],
[243,932,495,330,323,454,698,683,503,295,470,583,300,592,437,120,408,104,487,345],
[406,943,778,468,554,246,429,739,550,715,531,761,538,111,538,900,884,483,258,824],
[212,655,110,618,425,323,657,774,723,98,281,456,465,743,482,378,549,495,375,110],
[477,97,478,435,779,67,406,93,657,330,540,248,52,403,441,128,547,214,929,550],
[351,158,590,942,376,858,480,684,159,175,105,162,668,683,686,423,92,581,941,658],
[372,179,861,438,182,340,849,531,708,425,509,379,731,119,336,333,94,872,334,463],
[582,201,374,675,698,168,825,683,334,175,86,852,248,82,383,576,456,473,866,654],
[540,397,316,236,685,128,203,681,96,932,864,348,913,689,672,900,425,346,400,725],
[698,706,212,947,151,572,577,543,125,929,928,454,64,889,158,408,106,659,339,899],
[382,508,592,100,339,5,403,733,769,556,63,288,857,575,214,659,601,911,189,179],
[906,506,259,577,463,907,214,372,174,905,395,824,323,988,256,347,54,472,622,686],
[913,52,167,446,288,441,238,452,908,439,502,913,398,704,159,884,570,501,401,859],
[942,64,217,483,255,618,544,282,726,904,825,432,655,409,378,709,394,673,748,602],
[251,716,931,53,888,528,755,494,686,350,728,81,694,537,541,216,173,112,165,412],
[590,339,931,50,930,731,383,437,397,577,400,743,925,381,108,902,931,338,777,600],
[896,548,395,60,403,941,580,155,696,945,349,377,612,687,900,422,723,296,508,700],
[284,472,524,647,476,254,685,317,873,553,112,679,690,479,649,154,346,555,943,86],
[155,748,764,339,775,51,686,767,471,260,770,586,445,591,585,173,857,579,435,119],
[945,325,932,595,532,931,341,121,326,54,217,821,245,647,627,932,796,621,331,374],
[674,159,528,782,259,531,88,407,503,317,245,975,583,217,910,727,704,97,884,476],
[473,942,215,781,933,383,702,86,776,222,102,554,420,317,255,262,173,452,598,411],
[182,770,733,863,600,208,339,281,689,328,858,246,179,291,232,291,63,444,724,108],
[704,595,115,60,936,910,476,939,61,533,946,53,422,444,335,742,783,654,549,839],
[739,116,289,63,681,889,338,600,479,479,901,648,601,743,806,418,154,430,235,350],
[238,344,898,429,396,242,138,114,684,318,340,56,97,705,292,679,453,172,120,258],
[88,524,283,284,944,50,706,164,461,347,728,597,357,863,413,255,885,865,259,247],
[416,933,258,735,455,704,450,88,543,748,620,282,763,191,156,777,284,326,901,684],
[172,138,717,678,475,287,595,623,710,948,127,243,92,941,772,111,291,91,927,948],
[648,261,525,497,113,308,115,243,910,216,533,859,374,243,171,401,554,107,379,181],
[855,152,702,592,675,117,9,496,383,124,246,782,688,92,889,215,125,679,405,339],
[904,931,884,531,869,683,871,782,501,779,528,559,730,373,327,244,486,346,419,180],
[420,680,398,944,989,630,475,247,486,418,731,862,524,864,254,432,619,456,732,261],
[548,233,383,747,629,113,398,404,825,587,467,775,74,412,80,822,749,692,374,651],
[864,103,507,394,931,161,818,862,413,426,100,217,437,651,707,687,435,770,472,62],
[180,61,333,99,495,108,282,450,112,759,459,497,656,99,319,455,729,458,675,344],
[101,185,737,418,712,594,887,750,742,245,108,346,232,729,945,199,935,903,428,748],
[653,750,782,730,95,103,823,109,975,56,459,321,734,580,242,889,51,382,771,62],
[424,508,437,237,240,449,584,251,679,852,744,252,516,487,589,476,506,705,723,482],
[782,856,940,62,337,167,378,708,176,214,435,675,84,422,596,617,578,940,938,555],
[456,899,450,215,282,99,154,395,499,397,346,554,58,485,847,436,189,582,293,712],
[250,453,425,254,739,328,76,157,885,237,627,676,825,98,856,169,911,749,691,407],
[429,651,942,479,105,280,558,772,213,478,932,483,583,181,516,190,187,933,259,381],
[127,575,93,904,726,164,862,329,904,286,81,414,126,933,394,822,206,727,769,585],
[279,408,65,937,106,289,424,158,283,716,333,748,127,496,528,409,128,886,177,189],
[706,162,437,457,86,749,658,699,167,80,53,852,350,492,53,483,293,283,821,221],
[419,162,870,403,177,650,726,239,213,777,867,703,370,419,743,783,497,262,127,337],
[851,333,153,718,183,647,556,490,713,300,889,655,625,623,860,745,911,98,903,344],
[296,405,261,107,991,861,154,499,171,821,155,902,747,464,279,782,449,115,676,543],
[493,413,86,58,863,532,678,855,656,235,256,654,334,319,783,172,429,828,289,578],
[548,498,257,289,63,124,896,261,587,262,884,218,399,170,575,402,381,731,900,906],
[784,627,212,458,946,234,170,466,394,154,346,289,382,182,913,115,166,745,469,911],
[278,850,246,234,325,741,689,382,424,169,680,104,423,326,177,488,238,110,861,141],
[491,63,771,862,105,825,189,986,187,497,597,490,60,477,900,447,900,121,906,295],
[496,498,859,319,743,993,378,156,860,588,398,330,719,732,52,547,528,342,293,423],
[897,716,687,125,324,576,507,713,365,947,99,489,153,369,88,652,338,700,215,175],
[127,249,687,483,52,489,127,737,599,481,910,328,737,932,621,254,420,602,993,415],
[550,163,597,853,602,438,803,72,695,887,498,692,502,171,485,506,477,592,292,469],
[396,943,92,681,702,599,376,509,673,247,864,849,701,553,106,747,987,504,394,415],
[127,782,412,450,262,596,316,206,345,597,437,541,261,350,851,394,928,187,863,180],
[557,287,741,572,747,630,370,185,558,503,153,244,292,624,158,122,347,475,427,422],
[868,20,317,728,778,449,334,454,323,472,912,947,376,719,63,581,319,340,172,947],
[169,245,406,428,593,524,710,126,114,571,734,482,690,471,588,163,712,153,862,335],
[456,164,727,182,470,98,498,84,710,379,431,58,867,948,336,821,598,479,69,292],
[446,415,904,415,740,117,83,288,167,777,334,740,325,866,949,858,472,416,523,562],
[691,775,805,474,464,533,460,653,90,630,278,781,493,236,944,705,825,466,707,773],
[188,258,831,743,729,322,690,528,153,338,687,588,910,489,188,730,768,587,251,480],
[452,677,849,127,147,904,626,555,857,576,250,248,777,685,685,438,729,708,277,282],
[282,932,911,122,886,527,446,342,293,794,825,424,478,339,235,732,532,489,453,884],
[59,150,782,944,536,398,575,293,698,500,434,82,186,770,852,988,255,261,179,344],
[675,93,854,861,725,543,677,506,469,933,110,535,424,428,367,529,725,483,281,350],
[128,488,370,702,174,501,157,601,453,371,253,278,424,597,620,499,399,681,395,877],
[884,540,582,84,340,480,283,288,841,536,598,426,657,252,684,410,173,254,179,151],
[744,458,566,620,82,404,802,495,476,97,126,190,550,738,241,438,191,83,860,658],
[652,433,575,484,410,479,239,718,328,491,9,383,97,538,455,622,928,623,623,463],
[931,538,216,63,855,336,234,283,153,179,90,686,320,183,256,908,383,732,328,755],
[452,115,285,783,943,325,855,377,592,892,648,768,655,417,620,939,213,176,502,715],
[126,191,153,161,847,889,319,326,232,239,127,398,911,347,911,942,863,750,158,470],
[235,749,372,251,406,460,410,551,344,549,151,928,482,411,22,577,732,577,745,378],
[124,102,285,61,709,489,773,97,803,681,623,191,284,14,55,102,450,692,620,398],
[864,628,738,737,692,742,154,748,433,247,168,696,94,534,873,189,726,247,444,128],
[775,335,771,61,294,54,116,983,468,900,739,503,590,234,213,469,775,770,701,234],
[619,802,56,672,898,191,866,458,620,235,411,239,568,317,339,377,732,938,582,396],
[773,850,477,110,928,527,284,681,900,602,247,505,50,686,486,254,899,22,398,319],
[59,529,380,290,334,763,374,373,574,417,906,674,850,594,596,395,373,707,260,320],
[778,344,373,327,657,109,186,935,935,897,720,326,794,403,123,419,382,576,585,162],
[182,103,713,908,900,83,687,324,334,601,241,346,339,679,703,932,299,937,246,706],
[262,184,733,328,310,377,649,494,487,96,378,347,769,380,803,683,448,403,693,115],
[532,855,93,142,738,81,256,781,529,324,288,216,216,94,715,731,155,449,233,163],
[377,526,440,591,733,906,89,629,113,696,505,413,696,153,89,325,772,309,849,577],
[866,88,614,103,680,280,900,395,316,709,737,94,702,159,735,382,727,896,333,851],
[96,926,549,428,627,415,542,936,913,133,742,161,855,369,540,589,734,585,861,524],
[500,350,163,782,101,341,184,81,511,421,543,778,383,97,942,936,160,850,481,465],
[128,440,382,111,462,941,351,748,867,822,496,330,390,259,905,316,343,88,51,629],
[525,347,330,398,477,535,293,724,654,282,471,691,264,911,531,494,723,405,339,939],
[650,405,499,320,462,177,738,861,679,652,524,853,882,886,772,743,948,746,350,943],
[247,123,675,860,454,574,377,505,585,317,372,743,17,451,863,243,424,402,552,594],
[599,938,489,540,647,889,171,596,679,552,329,673,981,99,442,437,128,749,912,163],
[80,498,888,154,156,860,56,685,718,253,475,778,978,941,885,590,507,323,494,509],
[864,173,116,588,383,426,5,600,164,261,739,945,406,398,945,289,443,622,539,320],
[580,854,737,430,532,557,95,188,948,334,949,605,382,702,821,468,62,340,172,256],
[154,188,243,320,214,97,376,491,122,421,378,626,674,692,509,114,321,613,465,180],
[947,398,322,380,911,743,718,499,403,396,150,396,815,941,478,598,87,673,743,164],
[887,177,203,535,461,720,477,449,482,673,700,449,619,714,326,580,736,91,54,112],
[889,523,735,64,852,379,179,723,348,579,94,312,60,94,858,672,212,857,482,507],
[593,772,737,947,858,291,891,628,783,886,946,242,552,126,346,118,897,496,926,722],
[803,907,747,937,672,507,863,548,674,150,294,721,496,105,310,414,436,164,699,507],
[61,776,722,441,561,943,821,869,126,113,376,593,286,860,93,157,117,287,247,705],
[768,694,254,719,462,532,212,377,488,64,122,210,293,526,896,628,83,768,705,470],
[459,674,60,937,884,451,503,692,740,95,239,334,461,415,647,723,111,894,905,94],
[860,404,779,449,293,902,445,712,277,95,689,291,338,741,335,658,475,91,942,70],
[432,690,447,422,802,899,248,908,340,540,249,448,582,822,536,343,453,623,999,460],
[771,574,778,381,724,854,350,397,932,502,262,898,459,888,914,802,884,548,446,378],
[588,233,126,627,491,862,262,545,418,776,484,582,928,912,98,420,230,484,596,411],
[540,543,138,598,292,744,176,767,487,749,597,725,683,577,903,397,190,190,100,721],
[528,931,507,902,192,440,783,486,888,83,377,325,153,743,401,61,701,650,156,331],
[584,164,659,675,575,742,834,478,447,908,730,456,121,854,656,737,552,535,888,887],
[593,108,451,735,373,824,94,62,942,463,715,932,338,418,224,480,776,336,702,90],
[722,454,652,482,335,911,720,348,299,288,533,457,589,943,857,401,710,596,375,619],
[685,184,212,683,772,935,562,477,505,696,332,771,465,399,328,477,482,407,628,929],
[704,69,869,858,191,159,179,328,934,416,278,507,685,899,700,853,589,781,448,462],
[216,81,51,677,457,463,94,281,294,687,909,773,166,294,430,147,295,52,493,122],
[342,450,747,203,382,95,160,595,557,348,406,868,589,526,112,373,947,191,446,429],
[479,57,232,247,232,473,908,887,80,472,783,477,221,371,685,260,532,720,53,506],
[451,476,628,490,773,937,163,674,157,648,580,471,539,717,194,628,552,777,942,536],
[245,103,687,328,420,443,54,707,494,546,249,648,583,602,729,325,321,149,702,103],
[658,351,690,889,942,911,778,167,240,190,728,980,451,480,51,445,52,910,159,685],
[430,901,213,423,892,189,497,170,705,441,697,698,738,375,551,181,855,939,929,109],
[163,126,523,117,119,465,373,911,339,417,859,241,295,694,372,461,438,155,681,669],
[730,376,435,90,157,946,543,931,550,58,948,909,912,421,600,531,619,206,105,652],
[686,777,529,908,429,528,502,60,779,408,88,111,345,398,335,420,111,283,138,93],
[678,856,238,692,108,324,849,622,172,609,459,707,251,98,110,738,123,724,724,487],
[541,292,426,576,729,856,107,292,582,57,436,799,347,591,428,714,474,243,501,179],
[769,478,411,910,899,499,944,500,336,182,946,427,655,455,763,419,152,702,748,551],
[530,730,601,887,233,81,377,866,20,251,371,115,454,332,98,379,865,825,347,256],
[856,339,936,795,175,699,468,171,726,126,446,124,947,321,528,592,99,497,91,555],
[279,417,673,458,485,12,102,529,317,458,234,730,155,106,537,651,678,61,478,598],
[909,464,417,327,868,731,178,414,884,857,348,287,402,544,887,728,60,326,610,535],
[440,554,627,181,294,345,249,902,106,828,489,776,380,853,349,108,539,239,673,595],
[694,546,907,450,651,153,488,980,253,557,528,165,627,577,290,557,289,783,101,864],
[675,437,246,446,419,402,116,897,399,356,487,708,330,868,170,346,413,109,127,374],
[460,285,677,449,755,486,249,941,554,773,371,349,52,235,724,467,677,317,429,173],
[278,257,408,690,591,153,860,714,186,253,414,377,476,782,742,78,250,214,437,907],
[624,621,318,287,327,552,119,850,402,625,734,294,943,583,788,886,775,57,906,523],
[768,726,172,901,602,58,722,992,652,64,574,593,902,293,497,715,117,439,898,340],
[461,116,860,150,124,283,652,158,621,202,154,213,601,447,853,593,656,583,253,717],
[493,164,83,57,542,624,690,538,63,237,246,184,294,102,618,709,588,687,688,748],
[734,770,451,909,93,408,439,500,426,455,696,622,999,597,503,934,899,417,401,857],
[821,729,477,529,487,102,176,850,499,375,351,320,434,173,319,162,317,775,87,518],
[824,233,602,428,713,508,374,165,186,108,868,332,467,417,485,783,481,62,59,615],
[583,680,691,938,13,126,397,725,587,896,116,500,242,97,253,503,409,340,929,450],
[627,83,499,939,604,156,150,555,944,703,58,782,733,158,457,85,717,625,852,479],
[934,929,396,884,58,112,178,557,578,153,553,475,458,551,408,998,740,163,120,342],
[349,439,903,583,802,859,702,58,416,492,773,724,140,381,61,906,343,254,856,464],
[451,677,128,52,625,294,585,648,743,774,739,686,770,581,822,125,379,734,647,199],
[468,507,559,58,188,154,9,259,52,911,583,543,904,423,155,322,462,449,530,291],
[686,739,50,64,413,317,452,181,123,678,416,176,170,701,412,15,707,458,695,449],
[334,285,114,933,432,672,216,680,890,902,450,700,259,779,343,748,537,182,439,181],
[480,549,547,456,624,184,746,793,908,176,151,488,490,555,736,464,428,862,719,94],
[162,106,328,369,103,461,504,382,51,481,101,376,457,344,731,296,132,680,112,331],
[344,348,536,586,411,113,442,345,774,897,444,133,421,293,741,574,675,653,704,335],
[254,296,54,703,901,458,734,317,923,184,127,555,255,488,861,286,318,598,397,457],
[464,652,910,249,861,931,768,716,686,120,171,164,777,504,860,19,803,89,443,926],
[439,253,601,456,449,153,884,714,64,885,336,540,827,585,61,163,888,779,821,167],
[694,396,719,912,215,673,313,161,101,492,775,908,823,470,333,498,554,342,884,529],
[701,930,343,690,283,707,865,929,820,97,328,538,701,649,488,714,161,242,658,322],
[415,739,313,281,742,898,707,905,328,743,245,782,538,288,507,493,582,532,943,680],
[210,911,851,376,487,595,378,95,528,110,328,726,93,464,109,430,732,379,536,188],
[529,775,496,246,852,676,214,410,857,770,770,676,183,859,780,115,154,626,652,314],
[374,624,151,860,714,940,852,656,188,502,582,65,945,659,772,153,455,945,429,530],
[244,469,932,534,284,429,290,473,901,436,63,588,197,484,156,415,115,339,727,296],
[684,485,490,574,66,438,460,251,216,556,700,351,380,913,81,910,403,494,672,379],
[281,864,430,679,538,472,187,182,90,424,59,743,523,182,892,427,503,397,329,465],
[83,702,918,334,674,691,286,215,598,933,622,944,395,150,260,497,124,434,172,454],
[424,399,468,72,851,657,780,717,170,398,550,374,340,183,253,503,823,949,650,370],
[106,557,428,185,396,930,609,694,217,257,651,698,728,278,475,859,328,743,405,489],
[659,63,549,498,931,246,975,549,444,234,437,455,402,913,287,372,852,410,440,398],
[178,87,251,582,176,945,235,726,681,453,332,699,296,371,143,319,850,377,254,374],
[741,252,682,658,281,740,336,349,167,436,943,233,191,380,507,379,507,723,799,108],
[409,185,374,911,125,601,154,505,708,403,543,583,416,624,677,403,470,927,1,579],
[591,597,15,535,417,896,248,901,431,526,251,458,869,370,58,333,374,260,383,175],
[544,588,580,126,85,483,932,989,647,574,480,936,545,258,558,720,495,418,539,351],
[120,533,976,327,466,80,724,251,64,727,899,579,620,897,421,865,943,869,372,424],
[400,851,85,351,656,705,709,677,20,151,124,550,782,437,555,244,348,254,347,692],
[592,583,330,495,744,543,154,898,527,624,578,714,927,253,565,93,88,580,95,734],
[462,431,734,771,946,532,987,466,931,326,685,403,468,289,372,683,409,59,420,434],
[179,709,374,860,115,903,58,580,214,417,383,484,243,497,70,454,258,109,280,941],
[687,628,340,756,113,329,913,416,588,937,186,771,402,419,438,440,576,487,857,691],
[455,547,262,422,775,107,672,161,792,243,589,182,654,93,716,474,115,239,595,652],
[496,698,177,588,777,107,528,731,648,490,294,493,467,591,249,933,331,795,850,778],
[584,492,630,948,343,106,7,441,473,318,63,425,480,903,677,88,743,822,687,429],
[557,600,338,932,738,449,177,586,232,591,260,277,723,414,271,693,885,338,534,462],
[930,493,679,948,529,116,581,849,681,709,375,685,397,527,536,480,160,112,556,810],
[928,245,111,885,398,855,4,630,113,735,112,256,931,653,213,281,399,431,86,250],
[936,509,229,150,239,703,734,695,370,904,582,906,282,153,948,586,337,675,824,240],
[343,680,716,430,539,865,825,397,447,374,551,436,404,991,862,858,730,684,343,590],
[285,185,244,703,794,443,657,236,329,331,453,525,734,281,407,600,471,260,683,506],
[711,682,691,451,444,61,555,191,764,345,57,502,628,382,555,595,163,728,783,52],
[383,467,890,779,381,803,524,377,554,259,491,410,478,478,906,115,428,725,469,868],
[551,167,158,911,248,597,698,747,335,242,463,158,727,80,436,411,824,74,99,287],
[238,779,933,335,212,545,792,737,112,673,84,89,597,93,244,595,341,407,578,724],
[57,865,708,555,191,106,260,708,218,853,261,113,93,948,285,261,440,733,850,327],
[152,188,943,586,728,540,901,692,419,875,98,63,326,455,345,698,381,290,463,496],
[926,101,115,156,408,59,359,445,939,558,185,651,60,343,898,747,443,286,504,340],
[343,732,678,554,124,601,730,624,862,155,428,570,658,236,480,466,865,417,907,480],
[82,81,788,555,94,286,128,729,508,705,590,547,782,454,523,778,400,712,647,110],
[732,151,436,241,160,602,581,112,442,722,96,658,60,326,662,462,174,161,413,678],
[456,180,599,174,413,491,686,488,501,246,548,602,587,619,649,587,612,779,404,286],
[691,736,530,162,802,154,383,898,459,172,349,412,768,470,701,540,901,100,196,375],

  ]
}


validnumbers = set()

for k,v in input_data['rules'].items():
    _ = v
    for i in v:
        sub_ = set( list( range(i[0], i[1]+1) ) )
        validnumbers.update( sub_ )

invalid_values = list()
for t in input_data['nearby tickets']:
    for n in t:
        if n not in validnumbers: 
            invalid_values.append( n )

print(sum(invalid_values))
