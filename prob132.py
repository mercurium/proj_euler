import time
START = time.time()
from bitarray import bitarray

SIZE = 10**5
temp = bitarray('10' * SIZE)
primeLst = []
for i in xrange(3,len(temp),2):
    if temp[i] == 0:
        for j in xrange(i**2, len(temp),2*i):
            temp[j] = 1
        primeLst.append(i)


primeLst = primeLst[2:]

testLst = []
for i in xrange(10):
    for j in xrange(10):
        testLst.append(2**i*5**j)
testLst.sort()

count = 0
sumz = 0
for i in primeLst:
    if count == 40: #DONE!
        break
    for j in testLst:
        if j > i:
            break
        if pow(10,j,i) == 1:
            count +=1
            sumz += i
            print i, 'YAY', count
            break
print sumz, count

print "Time Taken:", time.time() - START

"""
Main idea, we want to find a power such that 10^i = 1 mod p.
If i is a factor of 10^9, then that means that the repeat cycle 10^i mod p can be portioned into SIZEs of 10^9. In a weird way, that means that the numbers sum up to 0 mod p, which means 1111...111 mod p == 0 mod p.

Ex: 1+2+4 = 0 mod 7. Idk why... I forgot T.T;;;

Anyways, so I just need to check 1,2,4,5,8,...etc for the powers of the numbers to see if they'll have 1111...111 (10^9 1's) = 0 mod p. Fun exercise for you if you come back and forget what we did :)

843296 40
Time Taken: 0.512022018433

"""
