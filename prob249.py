import time
from primes import get_primes

START = time.time()
MOD   = 10**16

prime_lst = sorted(get_primes(5000))
print "Time Taken: ", time.time() - START


prime_set2 = set([2])
temp = [0] * (sum(prime_lst)+1)
for i in xrange(3,len(temp),2):
  if temp[i] == 0:
    prime_set2.add(i)
    for j in xrange(3*i,len(temp),2*i):
      temp[j] = 1

lst = [1] + [0]*(sum(prime_lst))

print "Time Taken: ", time.time() - START

sumz = 0
for i in xrange(0,len(prime_lst)):
  for j in xrange(sumz,-1,-1):
    index = j + prime_lst[i]
    lst[index] = (lst[j] + lst[index]) % MOD
  sumz += prime_lst[i]

print "Time Taken: ", time.time() - START

answer = sum([lst[key] for key in prime_set2])

print answer % MOD
print "Time Taken: ", time.time() - START

"""
Time Taken:  250.211617947 (on laptop)
Time Taken:  100.299413919 (on desktop)
Time Taken:  5.43030786514 (on palantir mac laptop using pypy)


Answer: 9275262564250418

Method of approach: Dynamic Programming. I made a list of length(sum of all primes < 5000), and then considered the case where we add a prime to the sum or if we don't. This is unfortunately O(n^2) where n = sum of primes <5000.. which is not pretty... T__T
"""
