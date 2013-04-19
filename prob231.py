import time
from bitarray import bitarray
from primes import *
start = time.time()

sumz = 0
size = 10**7*2


pfactor = range(0,size+1)
for i in xrange(2,len(pfactor)):
  if pfactor[i] == i:
    for j in xrange(i*2,len(pfactor),i):
      pfactor[j] = i

def factorz(n):
  if n == 1: return 1
  return pfactor[n]+factorz(n/pfactor[n])

print "Time Taken: ", time.time() - start


sumz = 0
for i in xrange(1,size/4+1):
  sumz -= factorz(i)
for i in xrange(size * 3 /4 + 1, size+1):
  sumz += factorz(i)
print sumz
print "Time Taken: ", time.time() - start

"""
Time Taken:  20.2379760742
answer = 7526965179680
Time Taken:  58.1015560627 (on laptop)

Time Taken:  10.5234799385
7526965179680
Time Taken:  19.4148628712 (on desktop...wtf LOL)

#so the method of attack for this was compute the prime factorization of all numbers up to n using that same method that we used before.

"""
