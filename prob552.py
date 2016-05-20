import time, math
from primes import crt, get_primes


START     = time.time()
SIZE      = 3 * 10**5
prime_num = get_primes(SIZE)
LIM       = 3 * 10**5
prime_set = set(prime_num)

def factor(number):
  factors = []
  for prime in sorted(prime_set):
    while number % prime == 0:
      factors.append(prime)
      number /= prime
    if number == 1:
      break
  # i really don't care about larger factors
  return factors

def prod(lst):
  product = 1
  for num in lst:
    product *= num
  return product

print "There are:", len(prime_num), "primes"

product = 2
number  = 1
prime_factors = set([])

for i in xrange(2, LIM):
  number     = crt([product, prime_num[i-1]], [number, i]) % (product * prime_num[i])
  product   *= prime_num[i-1]
  factors    = set(factor(number))
  prime_set  = prime_set.difference(factors)
  prime_set.discard(prime_num[i])
  prime_factors.update(factors)
  print i, "Time Taken:", time.time() - START, len(prime_factors), len(prime_set), factors

print sorted(prime_factors)
print "Time Taken:", time.time() - START
