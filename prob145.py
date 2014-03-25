#NOTE this really has to be cleaned... TODO

import time, string
from itertools import product
START = time.time()
#strategy i was going for was to try all numbers less than 1 billion and see if it had even digits... obviously not the best choice xD.

num_dig = 8
odds = set()
for dig in xrange(0,num_dig+1):
    for i in product('13579',repeat = dig):
        odds.add(string.join(i,''))
for i in product('13579',repeat= num_dig):
    odds.add('1'+string.join(i,''))

print len(odds)
print "Time Taken:", time.time() -START
def dig_check(n):
    return n in odds

def mult(n): 
    return 10 - abs(9-n)
    
def mult1st(n):
    if n < 10:
        return n-1
    return 19-n


count = 0

#1 digit number don't have any

#2 digit numbers have 12,14,etc. 2+4+6+8 = 20
count+=20


print count
print "Time Taken:", time.time() -START


#3 digit numbers
for dig1 in range(1,19,2):
    for dig2 in range(0,10,1):
        num = dig1*101 + dig2*20
        if str(num) in odds:
            count += mult1st(dig1)


print count
print "Time Taken:", time.time() -START


#4 digit numbers
for dig1 in range(1,19,2):
    for dig2 in range(0,19):
        num = dig1*1001 + dig2*110
        if str(num) in odds:
            count += mult1st(dig1)*mult(dig2)


print count
print "Time Taken:", time.time() -START


#5 digit numbers
for dig1 in range(1,19,2):
    for dig2 in range(0,19):
        for dig3 in range(0,10):
            num = dig1*10001 + dig2*1010+dig3*200
            if str(num) in odds:
                count += mult1st(dig1)*mult(dig2)


print count
print "Time Taken:", time.time() -START


#6 digit numbers
for dig1 in range(1,19,2):
    for dig2 in range(0,19):
        for dig3 in range(0,19):
            num = dig1*100001 + dig2*10010+dig3*1100
            if str(num) in odds:
                count += mult1st(dig1)*mult(dig2)*mult(dig3)


print count
print "Time Taken:", time.time() -START

         
#7 digit numbers
for dig1 in range(1,19,2):
    for dig2 in range(0,19):
        for dig3 in range(0,19):
            for dig4 in range(0,10):
                num = dig1*1000001 + dig2*100010+dig3*10100+dig4*2000
                if str(num) in odds:
                    count += mult1st(dig1)*mult(dig2)*mult(dig3)


print count
print "Time Taken:", time.time() -START

#8 digit numbers
for dig1 in range(1,19,2):
    for dig2 in range(0,19):
        for dig3 in range(0,19):
            for dig4 in range(0,19):
                num = dig1*10000001 + dig2*1000010+dig3*100100+dig4*11000
                if str(num) in odds:
                    count += mult1st(dig1)*mult(dig2)*mult(dig3)*mult(dig4)






print count
print "Time Taken:", time.time() -START

"""
answer: 608720
Time Taken: 6.79233717918
Time Taken: 3.46769809723 on desktop
Time Taken: 0.718245029449 by not doing more unneccesary checks than needed

Well, I hardcoded it for each case so this is horribly unsatisfying... also used (a+b) * (first dig+last dig) + (c+d)*(second dig + second lastdig) ...etc


"""
