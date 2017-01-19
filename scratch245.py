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


    answer  = 0
    for num in xrange(3,SIZE+1,2):
      # ignore primes
      if totient[num] == num-1:
        continue
      top = num - totient[num]
      if top/gcd(top,num-1) == 1:
        answer += num
        print "number:", num
        print "\tnumber factored\t:", factor(num)
        print "\tn - 1 factored\t:", factor(num-1)
        print "\ttotient of num\t:", totient[num]
        print "\tn - totient\t:", num - totient[num], factor(num - totient[num])

    print "Answer:", answer
