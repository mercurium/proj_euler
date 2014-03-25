#NOTE TODO need to solve it
import time
from primes import m_r
START = time.time()

count = 0
SIZE = 10**7
MOD = 10**9 +7


def get_pfactor(SIZE):
    pfactor = range(0,SIZE+1)
    for i in xrange(2,len(pfactor)):
        if pfactor[i] == i:
            for j in xrange(i*2,len(pfactor),i):
                pfactor[j] = i
    return pfactor


pfactor = get_pfactor(SIZE)
print "Part 1 done!", time.time() - START

val_dict = {2:5,5:5}
for n in xrange(1,SIZE/2+1):
    k = SIZE - n
    while k != 1:
        p = pfactor[k]
        if p in val_dict:
            val_dict[p] +=1
        else:
            val_dict[p] = 1
        k /= p
    r = n;
    while r != 1:
        p = pfactor[r]
        val_dict[p] -=1
        r /= p
    prod = 1
    for factor in val_dict.keys():
        if val_dict[factor] == 0:
            del val_dict[factor]
            continue
        prod = ((1 + pow(factor, val_dict[factor],MOD)) * prod) % MOD
    count += prod*2
    if n% 100 == 0:
        print n, time.time() - START
count -= prod
print (count - pow(2,SIZE,MOD)+2) % MOD
print "Time Taken:", time.time() - START
