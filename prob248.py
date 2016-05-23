import time, math
from primes import m_r, factor, totient
START = time.time()

primeFactors = { 2: 10, 3: 5, 5: 2, 7: 1, 11: 1, 13: 1}
primes       = [13,11,7,5,3,2]
primeSets    = [set() for i in xrange(6)]
baseDict     = {1 : 0, 2 : 0, 3 : 0, 5 : 0, 7 : 0, 11 : 0, 13 : 0}
TOTIENT_VAL  = math.factorial(13)
INDEX        = 150000 -1

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
def computePossibilites(index, currentVals, product=1):

  # if at the end of the iteration, return
  if index == len(primes):
    if checkPrimePowers(currentVals, lambda x,y: x != y):
      answers.add(product)
    return

  # if we have too many powers in our product, quit.
  elif not checkPrimePowers(currentVals, lambda x,y: x < y):
    return

  # if we have too few powers...
  elif any(currentVals[prime] != primeFactors[prime] for prime in primes[:index]):
    return
  currentPrime = primes[index]

  if currentVals[currentPrime] == primeFactors[currentPrime]:
    computePossibilites(index+1, currentVals, product)
    return

  for primeNum in primeSets[index]:
    # don't want the same large prime twice
    if product % primeNum  == 0:
      continue
    dictClone = currentVals.copy()
    factorAndAddToDict(primeNum - 1, dictClone)
    if checkPrimePowers(dictClone, (lambda x,y: x < y)):
      computePossibilites(index+1, dictClone, product * primeNum)
      computePossibilites(index, dictClone, product * primeNum)

  powerDiff = primeFactors[currentPrime] - currentVals[currentPrime]
  for power in xrange(0,powerDiff+1):
    dictClone = currentVals.copy()
    factorAndAddToDict((currentPrime - 1) *currentPrime**power, dictClone)
    computePossibilites(index+1, dictClone, product * currentPrime**(power+1))

computePossibilites(0, baseDict, 1)
for answer in list(answers):
  if answer % 2 == 1:
    answers.add(answer*2)

print "Answer:", sorted(answers)[INDEX]
print "Time Taken:", time.time() -START


"""
Congratulations, the answer you gave to problem 248 is correct.

You are the 883rd person to have solved this problem.


jchen@jchen-mbp 20:23:25 ~/Developer/proj_euler(master) % pypy prob248.py
Answer     : 23507044290
Time Taken : 16.700619936

For this problem, the main thing to realize is that if n = m x k, where gcd(m,k) = 1, then:
  totient(n) = totient(m) * totient(k)
Then, from that, we can build up all numbers where totient(n) = 13! by looking at the primes that have a totient in the form 2^a x 3^b x 5^c x 7^d x 11^e x 13^f.

Anyways, need to cook for dinner then game of thrones. I solved the problem. WHOO! xD



"""
