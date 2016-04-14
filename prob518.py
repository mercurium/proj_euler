import time, math
START = time.time()
SIZE  = 10**4*6
# Problem size = 10^8

def get_primes_less_than(size):
  primes = []
  stuff = [0,1,2] + [1,2] *(size/2-1)
  for i in xrange(3,size,2):
    if stuff[i] == 1:
      for j in xrange(i**2,size,i*2):
        stuff[j] = i
      stuff[i] = i
      primes.append(i)
  return stuff, primes

def factor(n):
  factors = dict()
  while pfactorList[n] > 1:
    nextFactor = pfactorList[n]
    if nextFactor in factors:
      factors[nextFactor] += 1
    else:
      factors[nextFactor] = 1
    n /= pfactorList[n]
  # all primes need to have a factor of two, so we can ignore one power
  factors[2] -= 1
  #factors[1] = 2
  return factors

def getAllSquareFactors(n):
  factors = factor(n)
  squareFactors = [1]
  for primeFactor in factors.keys():
    for power in xrange(1,factors[primeFactor]/2+1):
      squareFactors = squareFactors + map(lambda x: x * primeFactor**2, squareFactors)
  return squareFactors


def slowSolution(size):
  pfactorList, primesList = get_primes_less_than(SIZE)
  primeSet                = set(primesList)
  primesSum               = 0
  answers                 = set()

  for i in xrange(len(primesList)):
    for j in xrange(i):
      c,b = primesList[i], primesList[j]
      if (b+1)**2 % (c+1) == 0 and ((b+1)**2 / (c+1) - 1) in primeSet:
        a = (b+1)**2 / (c+1) - 1
        primesSum += a + b + c
        answers.add(tuple(sorted([a,b,c])))
  print primesSum
  return answers

def fastExperimentalSolution(size):
  pfactorList, primesList = get_primes_less_than(SIZE)
  primeSet                = set(primesList)
  primesSum               = 0
  answers                 = set()

  for p in primesList:
    p1 = p+1
    squareFactors = getAllSquareFactors(p1)

    # need to try all squares that divide p+1, not just prime factors... TODO
    for squareFactor in squareFactors:
      ratio    = int(math.sqrt(squareFactor))
      upperLim = int(math.sqrt(SIZE * squareFactor / p1)  )

      for upperPart in xrange(1, upperLim+1):
        if (upperPart == ratio):
          continue
        b = (p1    * upperPart) / ratio - 1
        c = ((b+1) * upperPart) / ratio - 1
        if b in primeSet and c in primeSet:
          primesSum += p+b+c
          answers.add(tuple(sorted([p,b,c])))
  print primesSum
  return answers

print answers2.difference(answers)
print answers.difference(answers2)

primesSum = sum([x[0] + x[1] + x[2] for x in answers2])
print primesSum
print "Time Taken:", time.time() - START


"""

  a,b,c
  b/a = r
  c/b = r
  b^2 = a * c

  a = k
  b = kr
  c = kr^2

Optimizations:
  - If we know 'b', we only have to check other primes 'c' where (c+1) | (b+1)^2
    - Might be much faster than iterating through each prime > 'b'.
    - Worst case, still O(n^2). Probably drops it closer to O(8n) though.
    - Still probaby worth doing...
  - Try out using k and r rather than a,b,c
    - If r is big, we don't need to test as many numbers.

  10^2: 1035
  10^3: 75019
  10^4: 4225228

"""
