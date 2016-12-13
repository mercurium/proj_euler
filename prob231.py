import time
from primes import pfactor_gen, factor_given_pfactor
start = time.time()

SIZE = 10**7*2

pfactor = pfactor_gen(SIZE)

def factor(n):
  return sum(factor_given_pfactor(n, pfactor))

print "Time Taken: ", time.time() - start

sumz = 0
for i in xrange(1,SIZE/4+1):
  sumz -= factor(i)
for i in xrange(SIZE * 3 /4 + 1, SIZE+1):
  sumz += factor(i)
print sumz
print "Time Taken: ", time.time() - start

"""
Time Taken:  20.2379760742
answer = 7526965179680
Time Taken:  58.1015560627 (on laptop)

Time Taken:  10.5234799385
7526965179680
Time Taken:  19.4148628712 (on desktop...wtf LOL)

pypy prob231.py
Time Taken:  0.482394933701
7526965179680
Time Taken:  2.60380911827


#so the method of attack for this was compute the prime factorization of all numbers up to n using that same method that we used before.

"""
