#NOTE have not cleaned up this file yet.. T_T...
import time
from primes import *
from itertools import combinations as comb
START = time.time()


for dig in comb('12345',2):
    a,b,c = 10**int(dig[0]), 10**int(dig[1]), 1
    for i in xrange(0,10):
        ai = i * a
        for j in xrange(0,10):
            bj = j * b
            for k in xrange(0,10):
                ck = k
                count = 0
                multiplier = 111111 - a - b -c
                for val in xrange(0,10):
                    if m_r(val * multiplier + ai + bj + ck):
                        count += 1
                if count == 8:
                    print ai+bj+ck, count

print "Time Taken:", time.time() - START
