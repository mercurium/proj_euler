import time, math
from primes import get_primes, factor

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

# filter out large numbers that can't be part of a product pq
for index in xrange(len(primes)):
  prime = primes[index]
  if prime > SIZE / 2:
    forSureNum.add(prime)
    continue

  if primes[index+1] < SIZE / (SIZE // prime):
    forSureNum.add(max_prime_pow_dict[prime])
    continue

  unusedNum.add(prime)

print sum(forSureNum), len(forSureNum), len(unusedNum)
print "\n"

merged = set()
while len(unusedNum) != 0:
  print len(unusedNum)
  gainsDict = dict()
  for prime in unusedNum:
    insertMaxIntoDict(gainsDict, prime, (-1, prime, max_prime_pow_dict[prime], 0))
    for otherPrime in unusedNum:
      maxPow =  int(math.log(SIZE*1.0/otherPrime, prime))
      prod   = prime ** maxPow * otherPrime
      if prod > SIZE:
        break
      gain   = prod - max_prime_pow_dict[otherPrime] - max_prime_pow_dict[prime]

      insertMaxIntoDict(gainsDict, prime, (gain, otherPrime, maxPow, 1))
      insertMaxIntoDict(gainsDict, otherPrime, (gain, prime, 1, maxPow))
  
  for n in gainsDict.keys():
    otherNum = gainsDict[n][1]
    if n not in unusedNum or otherNum not in unusedNum:
      continue

    if gainsDict[n][0] <= 0:
      forSureNum.add(max_prime_pow_dict[n])
      unusedNum.remove(n)
      continue

    if gainsDict[otherNum][1] == n:
      merged.add( n**gainsDict[n][2] * otherNum ** gainsDict[otherNum][2])
      unusedNum.remove(n)
      unusedNum.remove(otherNum)

errors = True
while errors:
  errors = False
  for m1 in sorted(merged):
    if m1 not in merged:
      continue
    for m2 in sorted(merged):
      if m2 not in merged or m1 not in merged:
        continue

      f1 = factor(m1)
      f2 = factor(m2)
      m11, m12 = f1[0], f1[-1]
      m21, m22 = f2[0], f2[-1]
      m21Pow =  int(math.log(SIZE*1.0/m12, m21))
      m11Pow =  int(math.log(SIZE*1.0/m22, m11))
  
      if m1 + m2 < m11**m11Pow * m22 + m21 ** m21Pow * m12:
        errors = True
        merged.remove(m1)
        merged.remove(m2)
        merged.add(m11**m11Pow * m22)
        merged.add(m21**m21Pow * m12)
        print "Fixed:", m1, m2, m11, m12, m21, m22


print sum(forSureNum) + sum(merged)
print sum(forSureNum) + sum(merged) - 1726544591
print "Time taken:", time.time() - START



"""
Co(10) = {1,5,7,8,9}
Co(30) = {1,11,13,17,19,23,25,27,28,29}
CO(100) = {1, 17, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 81, 83, 88, 89, 91, 95, 97}



Congratulations, the answer you gave to problem 355 is correct.

You are the 354th person to have solved this problem.

Answer: 1726545007
Time taken: 0.53054189682


"""
