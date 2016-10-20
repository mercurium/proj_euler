import time
from primes import *

START    = time.time()
startVal = 724709891
endVal   = 729909891 + 1
endDig   = 56789

# 09891 * 56789 = ...XX99999

for index in xrange(startVal, endVal, 10**5):
  if mr(index):
    print "Answer:", int((index-1) * 4.5)
    break

print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 358 is correct.

You are the 1069th person to have solved this problem.

jchen@jchen-mbp 14:13:41 ~/Developer/proj_euler % pypy -i prob358.py
Answer    : 3284269560
Time Taken: 0.000118017196655


"""
