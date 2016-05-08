import time, math
from primes import m_r
START               = time.time()
LIM                 = 10**12
validHammingNumbers = set()
validPrimes         = set()


for i in xrange(0,int(math.log(LIM, 2)) +1):
  for j in xrange(0,int(math.log(LIM / 2**i, 3)) + 1):
    for k in xrange(0,18):
      if 2**i * 3**j * 5**k > LIM:
        break
      validHammingNumbers.add(2**i * 3**j * 5**k)

# Figure out which primes p have the property totient(p) = hammingNumber
for hammingNumber in validHammingNumbers:
  if m_r(hammingNumber +1):
    validPrimes.add(hammingNumber +1)

validPrimes = validPrimes.difference(set([2,3,5])) # these are included in hamming numbers already
validPrimes = sorted(validPrimes)[::-1]

validHammingNumbers.remove(1) # unnecessary, and causes slowdown
validHammingNumbers = sorted(validHammingNumbers)[::-1]

# compute every single product of primes ignoring 2,3,5 which results in totient(product) = hammingNumber
newSet = set([1])
for prime in validPrimes:
  oldSet = newSet.union(set())
  for oldNumber in oldSet:
    if oldNumber * prime <= LIM:
      newSet.add(prime * oldNumber)

validPrimeMultiples = sorted(newSet)

print "done computing prime multiples"
print "Time taken:", time.time() - START

# include 2,3,5 in the product
for hammingNumber in validHammingNumbers:
  newSet.add(hammingNumber)
  for number in validPrimeMultiples:
    if hammingNumber * number > LIM:
      break
    newSet.add(hammingNumber * number)

print "Answer is:", sum(newSet) % 2**32
print "Time taken:", time.time() - START

"""

Answer is: 939087315
Time taken: 18.9860980511



Congratulations, the answer you gave to problem 516 is correct.

You are the 662nd person to have solved this problem.

Nice work, mercurium, you've just advanced to Level 11 .
633 members (0.11%) have made it this far.

You have earned 1 new award:

  The Archivist: Solve half of the problems in the archives


"""
