import string
import math
from math import factorial as fa
import time
START = time.time()



def fact_sumz(n):
    if n == 0: return 0 #base case
    return fa(n%10) + fact_sumz(n/10)
    

sumz = 0
for i in range(3,10**6):
    if fact_sumz(i) ==i:
        sumz += i
        print i, sumz

print sumz

print "Time Taken:", time.time() - START
