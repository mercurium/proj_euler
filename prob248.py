import time, math
from primes import m_r, factor, totient
START = time.time()

primeFactors = { 2: 10, 3: 5, 5: 2, 7: 1, 11: 1, 13: 1}
primes       = [13,11,7,5,3,2]
primeSets    = [set() for i in xrange(6)]

possiblePrimes   = set()
possibleTotients = set([1])

for prime in primeFactors.keys():
  newSet = set()
  for power in xrange(1, primeFactors[prime]+1):
    newSet.update(set([ prime**power * num for num in possibleTotients]))
  possibleTotients.update(newSet)

for num in possibleTotients:
  if m_r(num+1):
    possiblePrimes.add(num+1)

# Arrange products into sets based on their largest prime factor
for num in list(possiblePrimes):
  for pIndex in xrange(len(primes)):
    if (num - 1) % primes[pIndex] == 0:
      primeSets[pIndex].add(num)
      break

def factorAndAddToDict(num, valueDict):
  factors = factor(num)
  for num in factors:
    valueDict[num] += 1

def checkPrimePowers(valDict, func):
  for prime in primeFactors.keys():
    if func(primeFactors[prime], valDict[prime]):
      return False
  return True

answers = set()
iterations = [0]
def computePossibilites(index, currentVals, product=1):

  if index >= len(primeFactors):
    if not checkPrimePowers(currentVals, lambda x,y : x != y):
      answers.add(product)
    return

  prime = primes[index]

  # if we have more powers than we should, it's an invalid number
  if currentVals[prime] > primeFactors[prime]:
    return
  # if we have exactly the right number of powers for that factor, skip this part
  elif currentVals[prime] == primeFactors[prime]:
    return computePossibilites(index + 1, currentVals, product)

  elif index >= len(primes) - 1:
    twoPow = primeFactors[2] - currentVals[2]
    if m_r(2**twoPow +1):
      answers.add((2**twoPow + 1) * product)
    return

  for num in primeSets[index]:
    iterations[0] += 1
    dictClone = currentVals.copy()
    factorAndAddToDict(num - 1, dictClone)
    if checkPrimePowers(dictClone, (lambda x,y : x > y)):
      continue
    computePossibilites(index + 1, dictClone, product * num)

baseDict = {1 : 0, 2 : 0, 3 : 0, 5 : 0, 7 : 0, 11 : 0, 13 : 0}
computePossibilites(0, baseDict, 1)

for answer in list(answers):
  if answer % 2 == 1:
    answers.add(answer*2)

count    = 0
badCount = 0
for answer in answers:
  if totient(answer) == math.factorial(13):
    count += 1
  else:
    print math.factorial(13) / totient(answer), totient(answer) / math.factorial(13)
    badCount += 1

print count, badCount
print "Time Taken:", time.time() -START


"""
totient(n) = 8 for n  = 15, 16, 20, 24, 30

totient(3) = 2
totient(5) = 4
totient(17) = 16
totient(4) = 2

totient(n) = 16 for n  = 17, 32, 34, 40, 48, 60

totient(n) = 12 for n = 13, 21, 26, 28, 36, 42

totient(n) = 6 for n  = 7, 9

6 x 2
2 x 2 x 3
4 x 3




"""
