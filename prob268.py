#NOTE TODO need to solve it
import time
START = time.time()
from itertools import combinations


SIZE = 10**2.
LIM = 4

primes = [2, 3, 5 , 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
sumz = 0
for numFactor in xrange(LIM):
    for combo in combinations(xrange(len(primes)),numFactor):
        count = SIZE

        for i in xrange(len(primes)):
            if i in combo:
                count /= primes[i]
            else:
                count = (count * (primes[i]-1))/primes[i]
        sumz+= count
    print sumz, numFactor
print sumz

print "Time Taken:", time.time() - START
