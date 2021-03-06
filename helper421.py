import time
start = time.time()
from bitarray import bitarray

debug = True
size = 10000
prime_array = bitarray('0'*(size+1))
prime_lst = []
for i in xrange(3,size+1,2):
  if prime_array[i] == 0:
    for j in xrange(i**2,size+1,i):
      prime_array[j] = 1;
    prime_lst.append(i)

#vals = {6:[],7:[],8:[],9:[],10:[]}
vals = {2:[],3:[],4:[]}
big_sum = 0
for i in prime_lst:
  sumz,count = 0,0
  for j in range(1,i):
    if pow(j,15,i) == i-1:
      count+=1
      sumz+=j
  big_sum += sumz
  if debug:
    if count == 5:
      print "Sum =", sumz,"number shown=", count,"prime=", i, "sum/i=", sumz/i
      vals[sumz/i] += [i]
      
      
print big_sum
print vals[2]
print "Time Taken:", time.time() - start

"""

#print "Sum =", sumz,"number shown=", count,"prime=", i, "sum/i=", sumz/i


if count = 1
only numbers that work for that prime are those that are p-1 mod p.

if count = 3
the sum of the numbers that work for that prime is 2*p

if count = 5
the sum of the numbers that work for that prime is either 2p, 3p or 4p...

if count = 15...
the sum is 6p,7p, 8p,9p, or 10p... wat





okay
so we want to find the distinct prime factors of n^15 + 1
aka
we want n^15 = -1 mod p
for all primes < 10^8

and since we're iterating through 1 <= n <= 10^11
we want to know the sum of all numbers such that n^15 = -1 mod p
well
we know that n^(p-1) = 1 mod p
so then
n^(p-16) = -1 mod p as well
and similarly, n^(p-31) = 1 mod p
and we can keep reducing down to either
so that we either have 1,3,5, or 15 numbers such that n^15 = -1 mod p
now i had a conjecture
that if there were 3 numbers satisfying this
the sum of the numbers m such that m^15 = -1 mod p is 2 * p
and if there were 5 such m
it would be 3 * p
unfortunately this conjecture does not hold.
well
it holds for the boring case where there are 3 numbers and when there is one number
but not for 5 or 15
xD
did that make sense? :x

since we know n^15 = -1
and n^(p-1) = 1 mod p
then
n^(p-16) = -1 as well
or mainly
since n^15 = -1, we know n^30 = 1 mod p
and so we can find gcd(30,p-1) = d
and n^d = -1 as well
err
n^d = 1
then
how to explain it ._.
d can be 1,2,3,5,6,10,15, or 30
if it has a factor of 2
if d > 15
then we know that d-15 = e also has n^e = -1 mod p
if d < 15, then we know that 15-d = f also has n^f = -1 mod p
we know the first statement because n^15 * n^e = n^(15+e) = n^(15+d-15) = n^d = 1
second one same logic

"""
