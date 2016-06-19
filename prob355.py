import time, math
from primes import get_primes

START = time.time()
SIZE  = 200000

def insertMaxIntoDict(valsDict, key, value):
  if key in valsDict and valsDict[key][0] > value[0]:
    return
  else:
    valsDict[key] = value

primes    = get_primes(SIZE)
prime_set = set(primes)

max_prime_pow_dict = dict()
for p in primes:
  max_prime_pow_dict[p] = p**(int(math.log(SIZE, p)))

forSureNum = set([1])
unusedNum  = set()

for index in xrange(len(primes)):
  prime = primes[index]
  if prime > SIZE / 2:
    forSureNum.add(prime)
    continue
  prime_mult = SIZE / prime

  if primes[index+1] < SIZE / prime_mult:
    forSureNum.add(max_prime_pow_dict[prime])
    continue

  unusedNum.add(prime)

print len(unusedNum)
print sum(forSureNum), len(forSureNum), len(unusedNum)

print "\n\n"

while len(unusedNum) != 0:
  print len(unusedNum)
  gainsDict = dict()
  for prime in unusedNum:
    insertMaxIntoDict(gainsDict, prime, (-1, prime, max_prime_pow_dict[prime], 0))
    for otherPrime in unusedNum:
      for otherPrimePow in xrange(1, int(math.log(SIZE, otherPrime)+1)):
        maxPow = int(math.log(SIZE/otherPrime**otherPrimePow, prime))
        prod   = prime ** maxPow * otherPrime ** otherPrimePow
        if prod > SIZE:
          break
        gain   = prod - max_prime_pow_dict[otherPrime] - max_prime_pow_dict[prime]

        insertMaxIntoDict(gainsDict, prime, (gain, otherPrime, maxPow, otherPrimePow))
        insertMaxIntoDict(gainsDict, otherPrime, (gain, prime, otherPrimePow, maxPow))

  for n in gainsDict.keys():
    otherNum = gainsDict[n][1]
    if n not in unusedNum or otherNum not in unusedNum:
      continue

    if gainsDict[n][0] <= 0:
      forSureNum.add(max_prime_pow_dict[n])
      unusedNum.remove(n)
      continue

    if gainsDict[otherNum][1] == n:
      forSureNum.add( n**gainsDict[n][2] * otherNum ** gainsDict[otherNum][2])
      #print "\t", n, "\t", otherNum, "\t", gainsDict[n][0]

      if n < SIZE**.5 and otherNum < SIZE**.5:
        print n, otherNum

      unusedNum.remove(n)
      unusedNum.remove(otherNum)

print sum(forSureNum), len(forSureNum)

print "Time taken:", time.time() - START



"""
Co(10) = {1,5,7,8,9}
Co(30) = {1,11,13,17,19,23,25,27,28,29}
CO(100) = {1, 17, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 81, 83, 88, 89, 91, 95, 97}


"""
