#NOTE TODO need to solve it

import time
START = time.time()
SIZE = 10**3
from primes import m_r


pfactor = range(0,SIZE+1)
for i in xrange(2,len(pfactor)):
    if pfactor[i] == i:
        for j in xrange(i*2,len(pfactor),i):
            pfactor[j] = i

sumz,count = 0, 0
answer = [0] * (SIZE+1)



for i in xrange(len(answer)):
    if answer[i] != 0:
        print i, answer[i]


iterCount1,iterCount2 = 0,0
primeCount = 0
worksCount = 0
notWorking = []
for p in xrange(2,SIZE):
    if p% 1024 == 0:
        print p, sumz, iterCount1, iterCount2, worksCount, primeCount
    if pfactor[p] == p:
        primeCount +=1
        x = -1
        for i in xrange(1,p/2+5):
            iterCount1+=1
            if (i**2-3*i-1) % p == 0:
                x = i
                break
        if x == -1:
            notWorking.append(p)
            continue
        y = p-x+3
        worksCount +=1
        for j in xrange(0,p/2+2):
            iterCount2 +=1
            a,b = j*p+x, j*p+y
            if (a**2-3*a-1) % p**2 == 0:
                if (p**2-a+3 < a):
                    a = p**2-a +3
                sumz += a
                print p, a,x,y, sumz, a * 1.0 / p**2
                break
            if (b**2-3*b-1) % p**2 == 0:
                sumz += b
                print p, b,x,y, sumz, b * 1.0/p**2
                break
print sumz
print "Time Taken: ", time.time() - START
print "took", iterCount1, iterCount2, "iterations"
print "Only", worksCount, "out of ", primeCount, "had this work"
print "The ones we should have skipped were:", notWorking


