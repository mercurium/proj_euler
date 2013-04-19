import time
start = time.time()
from bitarray import bitarray
from primes import mr

prime_set = set([2])
temp = bitarray('0'*5000)
for i in xrange(3,len(temp),2):
  if temp[i] == 0:
    prime_set.add(i)
    for j in xrange(3*i,len(temp),2*i):
      temp[j] = 1
prime_lst = list(prime_set)
prime_lst.sort()
print "Time Taken: ", time.time() - start


prime_set2 = set([2])
temp = bitarray('0'*(sum(prime_lst)+1))
for i in xrange(3,len(temp),2):
  if temp[i] == 0:
    prime_set2.add(i)
    for j in xrange(3*i,len(temp),2*i):
      temp[j] = 1

lst = [0]*(sum(prime_lst)+1)
lst[0] =1

print "Time Taken: ", time.time() - start


sumz = 0
for i in xrange(0,len(prime_lst)):
  for j in xrange(sumz,-1,-1):
    lst[j+prime_lst[i]] = (lst[j] + lst[j+prime_lst[i]])%10**16
  sumz += prime_lst[i]

print "Time Taken: ", time.time() - start

sumz = 0
for i in prime_set2:
  sumz += lst[i]
  
print sumz % 10**16
print "Time Taken: ", time.time() - start

"""
Time Taken:  250.211617947 (on laptop)
Time Taken:  100.299413919 (on desktop)

Answer: 9275262564250418

Method of approach: Dynamic Programming. I made a list of length(sum of all primes < 5000), and then considered the case where we add a prime to the sum or if we don't. This is unfortunately O(n^2) where n = sum of primes <5000.. which is not pretty... T__T
"""
