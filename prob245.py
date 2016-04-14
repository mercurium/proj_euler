#NOTE TODO need to solve it
import time
from primes import mr as is_prime, factor as factor_num
START   = time.time()
MAX_LIM = 10**11 * 2
SIZE    = int(MAX_LIM**.5)

#for each number n, return some factor of it.
def pfactor_gen(size):
  stuff = [0,1,2] + [1,2] *(size/2-1)
  for i in xrange(3,size,2):
    if stuff[i] == 1:
      for j in xrange(i**2,size,i*2):
        stuff[j] = i
      stuff[i] = i
  return stuff

def prime_gen(size):
  primes = [2]
  stuff = [0,1,2] + [1,2] *(size/2-1)
  for i in xrange(3,size,2):
    if stuff[i] == 1:
      primes.append(i)
      for j in xrange(i**2,size,i*2):
        stuff[j] = i
      stuff[i] = i
  return primes

#simple factoring method, put one of the factors of n onto the list until we run out of factors
def factor_given_pfactor(n):
  factors = []
  while pfactor[n] != 1:
    factors.append(pfactor[n])
    n /= pfactor[n]
  return factors

def getDivisors(num):
  if num > SIZE:
    factors = factor_num(num)
  else:
    factors  = factor_given_pfactor(num)
  divisors = set([1])
  for n in factors:
    newDivisors = [n * x for x in divisors]
    divisors.update(set(newDivisors))
  return list(divisors)

def totientPrimes(lst):
  return prod([(x-1) for x in lst])

def prod(lst):
  prodVal = 1
  for num in lst:
    prodVal *= num
  return prodVal

def validatePrimeList(lst):
  return (prod(lst)- 1) % (prod(lst) - totientPrimes(lst)) == 0

pfactor = pfactor_gen(SIZE+1)
prime_nums = prime_gen(SIZE+1)
answer  = 0
count   = 0
for n in prime_nums:
  if n > MAX_LIM**.5:
    break
  divisors       = getDivisors(n**2 - n + 1)
  possibilePairs = [ (x - n + 1) for x in divisors]
  probablePairs  = filter((lambda x: x > n and is_prime(x)), possibilePairs)
  for prime2 in probablePairs:
    if validatePrimeList([n, prime2]):
      if n*prime2 < MAX_LIM:
        answer += n * prime2
        count += 1
        print n, prime2, n*prime2

print "count:", count, "answer:", answer
print "Time Taken:", time.time() -START

'''
I think I got it down for 2 factor numbers. Just need to expand it to 3/4 factor numbers
Also, it looks like I'm fine going up to ~sqrt(SIZE) for checking primes for the pairs.

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
