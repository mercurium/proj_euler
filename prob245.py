#NOTE TODO need to solve it
import time
from primes import mr as is_prime, factor as factor_num
START = time.time()
SIZE  = 10**6

def gcd(a,b):
  if a == 0:
    return b
  return gcd(b%a,a)

#gives you the totients of all numbers i <= size
def getTotient(size):
  lst = range(size+1)
  lst[0] = 1
  for i in xrange(2,len(lst)):
    if lst[i] == i:
      for j in xrange(i,len(lst),i):
        lst[j] = (lst[j] * (i-1))/i
  return lst

#for each number n, return some factor of it.
def pfactor_gen(size):
  stuff = [0,1,2] + [1,2] *(size/2-1)
  for i in xrange(3,size,2):
    if stuff[i] == 1:
      for j in xrange(i**2,size,i*2):
        stuff[j] = i
      stuff[i] = i
  return stuff

#simple factoring method, put one of the factors of n onto the list until we run out of factors
def factor_given_pfactor(n):
  factors = []
  while pfactor[n] != 1:
    factors.append(pfactor[n])
    n /= pfactor[n]
  return factors

def getDivisors(num):
  factors  = factor_given_pfactor(num)
  divisors = set([factors[0]])
  for factor in factors[1:]:
    newDivisors = [factor * x for x in divisors]
    divisors.update(set(newDivisors))
  return list(divisors)

totient = getTotient(SIZE+1)
pfactor = pfactor_gen(SIZE+1)
for n in xrange(3,10**3):
  if not is_prime(n):
    continue
  divisors       = getDivisors(n**2 - n + 1)
  possibilePairs = [ (x - n + 1) for x in divisors]
  probablePairs  = filter((lambda x: x > 0 and is_prime(x)), possibilePairs)
  if len(probablePairs) > 0:
    print n, n**2 - n + 1
    print "\tprobably pairs:", probablePairs

print "Time Taken:", time.time() -START

'''
n = p * q
tot(n) = (p-1)*(q-1)
n - tot(n) = p+q -1

For two primes...
    pq - 1 = (p+q-1)k
->  pq + q^2 - q - q^2 + q -1 = (p+q-1)k
->  (p+q-1)|(-q^2 + q - 1)
->  (p+q-1)|(q^2 - q + 1)
(Also true for p, so we also have...)
(p+q-1)|(p^2 - p + 1)

So we can figure out which numbers work together.

Rules:
  - Number can not be prime (given in statement)
  - Number can not have a factor that is a square
  - Number can not have 2 as a factor
  - We can figure out which numbers can possibly pair with a prime by doing...
    - (p+q-1)|(p^2-p+1)
    -> (p+q-1) can be any divisor of (p^2-p+1)

Rule 2 reasoning:
  Can never have a number with a factor squared. If we did, then...
    n = p^2k
    -> tot(n) = p(p-1) * (stuff)
    -> p|tot(n)
    -> p|(n - tot(n)
    but p does not divide n-1.

Rule 3 reasoning:
  - If we have two as a factor, then tot(n) < n/2
    (when there is more than one prime factor)
  -> n-tot(n) > n/2
  -> (n-tot(n)) can not divide (n-1)



only 47 numbers for n=10^6
  Answer: 11149065
  Time Taken: 2.69333481789

Only 110 numbers for n=10^7
  Answer: 275069018
  Time Taken: 29.9830768108


n = p*q*r
tot(n) = (p-1)*(q-1)*(r-1)
       = pqr - pq - pr - qr + q + r + p - 1

n-tot(n) = pq + pr + qr - p - q -r + 1
         = p(q+r - 1) + q(r-1) - (r+1)
'''
