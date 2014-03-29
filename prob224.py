#NOTE TODO need to solve it
import time
START = time.time()
from primes import *

START = time.time()

SIZE = 75 * 10**6
count = 0


for k in xrange(1,85*10**5,4):
    if k%3 == 0 or k%7 == 0 or k%11 ==0:
        continue
    possibleVals = []
    for j in xrange(k/2+1):
        if (4*j**2+1) % k == 0:
            possibleVals.append(j)
            if k != 1:
                possibleVals.append(k-j)
            if mr(k):
                break
    for j in possibleVals:
        for mult in xrange(j%2,10**6,2):
            i = mult*k+j
            a = 2*i
            if a < k:
                continue
            b = (a**2+1-k**2)/(2*k) #(k^2(4m^2 - 1) + 2mkj + j^2 -1)/ 2k
            if a > b:
                continue
            c = b+k
            if a+b+c <= SIZE:
                count +=1
            else:
                break
    print count, k, a+b+c, mult, possibleVals

print "Time Taken:", time.time() - START


"""
<<<<<<< Updated upstream
We want to solve:
a^2 +1 = 2bk+k^2
and this is satisfied when k%4 = 1
Need to make sure that since a = 2i, k|(4i^2+1)
So we need to solve the problem of finding (-1)^(1/2) mod k. Okay, cool xD.



a <= (a^2+1-k^2)/2k
2ak <= a^2 - (k^2-1)
a^2 - 2ka - (k^2-1) >= 0
(2k + (4k^2 - (4k^2-4))/2
(a-k+1)(a-k-1)  >= 0
a > k

i = mk +j
a = 2i
b = (a^2+1-k^2)/2k
b = (4i^2+1)/2k - k/2
b = (4(mk+j)^2+1)/2k - k/2
b = (4m^2k^2 +8mkj +(j^2 +1))/2k
b = 2m^2k +4mj +(j^2+1)/2k -k/2
c = 2m^2k +4mj +(j^2+1)/2k +k/2
a+b+c = 2mk+2j + 4m^2k + 8mk + (j^2+1)/k



a=a
b = (a^2+1)/2k - k/2
c = b+k
a+b+c = a+(a^2+1)/k = (a^2+ak+1)/k <= SIZE


4i^2 + 2i  = 74999999
2i(2i+1) = 74999999
a = 2x
c^2 = b^2 + a^2 +1
c^2 = b^2 + 4x^2+1
c = (b+k)

c^2 = b^2 + 2bk + k^2 = b^2 + a^2+1 = b^2+4x^2+1
k(2b+k) = 4x^2+1


2bk + k^2 = a^2 +1
k(2b+k) = 4m^2+1 
==> 4m^2 = -1 mod k


k(2b+k) = a^2+1
b > a
k(2a+k) < a^2+1
-> k < a/2


c = (b+k) --> 2bk + k^2 = 4x^2+1
k = 1
2b + 1 = 4x^2 +1
2b = 900
b = 450

(1800 +1)^2 = 1800^2 + 2(1800)+1

3601 = 2bk +k^2
k = 1
b = 1800

k(2b+k) = 4x^2 + 1
=======
c^2 = b^2 + a^2+1
c = (b+k)
c^2 = b^2 + 2bk+k^2

a^2+1 = k(2b+k)

a = a
b = (a^2+1-k^2)/2k
c = b+k

a+b+c = a+(a^2+1-k^2)/2k + (a^2+1-k^2)/k + k
a+b+c = a+(a^2+1)/k





>>>>>>> Stashed changes

"""
