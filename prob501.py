import time
from primes import get_prime_count, get_primes

SIZE  = 10**12
START = time.time()

primes    = get_primes(int(SIZE**.5)*100)
primeLen  = len(primes)
print "Time Taken:", time.time() - START

numPrimesLessThanN  = [0] * (int(SIZE**.5) * 100)
primeIndex = 0
while primeIndex < len(primes)-1:
  for index in xrange(primes[primeIndex], primes[primeIndex+1]):
    numPrimesLessThanN[index] = primeIndex + 1
  primeIndex += 1
numPrimesLessThanN[primes[-1]:] = [len(primes)] * (len(numPrimesLessThanN) - primes[-1])

count = 0

# Part 1, p^7 < SIZE

count += get_prime_count(int(SIZE**(1/7.)))
print "Part 1 is:", count
print "Time Taken:", time.time() - START
START = time.time()

i = 0
while primes[i]**3*2 <= SIZE:
  maxLim     = int(SIZE * 1.0 / primes[i]**3)
  if maxLim < len(numPrimesLessThanN):
    numPrimes = numPrimesLessThanN[maxLim]
  else:
    numPrimes  = get_prime_count(maxLim)
  count     += numPrimes
  if numPrimes >= i:
    count -= 1
  i+= 1

print "Part 2 is:", count
print "Time Taken:", time.time() - START
START = time.time()

i = 0
iterations = 0
iterations2 = 0
while i < primeLen and primes[i] < SIZE**(1/3.):
  print i
  j = i + 1
  while j < primeLen and primes[j] < SIZE**.5:
    iterations += 1
    val       = SIZE / (primes[i] * primes[j])
    if val < len(numPrimesLessThanN):
      numPrimes = numPrimesLessThanN[val]
      iterations2 += 1
    else:
      numPrimes = get_prime_count(val)
    if numPrimes <= j:
      break
    count    += numPrimes - j - 1
    j += 1
  i += 1

print "Part 3 is:", count
print "num iterations:", iterations, iterations2


print "Answer is:", count
print "Time Taken:", time.time() - START


"""

8 divisors means that a number is either in the form

p^7
p^3 x q
p x q x r


p^7 case is super easy to handle. p^3 x q should also not be too bad to handle.

p x q x r might be a bit more annoying

Congratulations, the answer you gave to problem 501 is correct.

You are the 662nd person to have solved this problem.


Part 3 is: 197912312715
num iterations: 2372370 2369770
Answer is: 197912312715
Time Taken: 21.1627089977

"""
