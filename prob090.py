#answer I got was 1217... :D YESSSS IT WAS RIGHT
#...took .2 seconds because i was being lazy and bruteforcing lol...

import time
import string
from itertools import combinations as comb
start = time.time()


def test(d1,d2):
    if not ('0' in d1 and '1' in d2) and not ('1' in d1 and '0' in d2):    
        return False
    if not ('0' in d1 and '4' in d2) and not ('4' in d1 and '0' in d2): 
        return False
    if not ('0' in d1 and '9' in d2) and not ('9' in d1 and '0' in d2):    
        if not ('0' in d1 and '6' in d2) and not ('6' in d1 and '0' in d2):
            return False
    if not ('9' in d1 and '1' in d2) and not ('1' in d1 and '9' in d2):
        if not ('6' in d1 and '1' in d2) and not ('1' in d1 and '6' in d2): 
            return False
    if not ('2' in d1 and '5' in d2) and not ('5' in d1 and '2' in d2): 
        return False
    if not ('9' in d1 and '3' in d2) and not ('3' in d1 and '9' in d2):
        if not ('6' in d1 and '3' in d2) and not ('3' in d1 and '6' in d2): 
            return False
    if not ('4' in d1 and '9' in d2) and not ('9' in d1 and '4' in d2):
        if not ('4' in d1 and '6' in d2) and not ('6' in d1 and '4' in d2): 
            return False
    if not ('8' in d1 and '1' in d2) and not ('1' in d1 and '8' in d2): 
        return False
    return True

count = 0
for i in comb('0123456789',6):
    for j in comb('0123456789',6):
        if int(string.join(i,'')) >= int(string.join(j,'')) and test(i,j):
#            print i,j
            count += 1

print count
print "Time Taken:", time.time() -start
