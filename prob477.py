<<<<<<< Updated upstream
#NOTE TODO need to solve it

import time, math
from itertools import combinations as comb
START = time.time()
SIZE  = 10**6

def primeGen(size): #for each number n, return some factor of it.
  primes = []
  factors = [0,1,2] + [1,2] *(size/2-1)
  for i in xrange(3,size,2):
    if factors[i] == 1:
      for j in xrange(i**2,size,i*2):
        if factors[j] == 1:
          factors[j] = i
      factors[i] = i
      primes.append(i)
  return primes

def checkPropertyLessStupid(m, factorization):
  for factor in factorization:
    if factor == 1:
      return True
    if (m / factor + 3) % (factor - 1) != 0:
      return False
  return True
cpls = checkPropertyLessStupid

def prod(lst):
  return reduce((lambda x,y: x*y), lst, 1)

#maxNumPrimes = 6 # TODO fix this
#listOfPrimes = primeGen(int(SIZE**.5))
#
#sumz  = 0
#count = 0
#
#for numPrimes in xrange(1,maxNumPrimes):
#  for combo in comb(listOfPrimes, numPrimes):
#    count += 1
#    productOfPrimes = prod(combo)
#    if productOfPrimes < SIZE and cpls(productOfPrimes, combo):
#      print combo, productOfPrimes
#      sumz  += productOfPrimes
#    primeIndex = listOfPrimes.index(combo[0])
#    if prod(listOfPrimes[primeIndex: primeIndex+numPrimes]) > SIZE:
#      break


listOfPrimes = primeGen(int(SIZE**.5))
#posAns       = [(3,[3])] # product of primes, # factors in a list
#for prime in listOfPrimes[1:]:
#  posAns.extend([(x[0] * prime, x[1] + [prime]) for x in posAns])
#  posAns = filter((lambda x: x[0] < SIZE), posAns)
#
#posAns.sort()
#print "Time Taken:", time.time() - START
##START = time.time()
#
#sumz = 0
#count = 0
#for i in posAns:
#  if cpls(i[0], i[1]):
#    print i
#    sumz  += i[0]
#    count += 1


posAns       = [(1,[])] # product of primes, # factors in a list
for prime in listOfPrimes:
  posAns.extend([(x[0] * prime, x[1] + [prime]) for x in posAns])
  posAns = filter((lambda x: x[0] < SIZE), posAns)

posAns.append((2,[2]))
posAns.sort()
print "Time Taken:", time.time() - START
#START = time.time()

sumz = 0
count = 0
for i in posAns:
  if cpls(i[0], i[1]):
    print i
    sumz  += i[0]
    count += 1

print sumz, count, len(posAns)
print "Time Taken:", time.time() - START


"""
  Numbers that seem to work: products of primes with no repeats (aka, p^2k does not work), and no evens besides 2.

  For each prime, p, we need the number to equal:
  m = p-4 (mod p-1)

  We can figure out which multiples of primes work for a prime by using:
  m = p(p-4 + k(p-1)) for all k >= 0

  Ex: for 7, we can have...
    7((7-4) + 0(7-1)) = 21 <-- actual answer that works
    7((7-4) + 1(7-1)) = 21 + 42 + 63. <-- Doesn't work since 63 = 3^2 * 7, but it satisfies the 7 req
    7((7-4) + 2(7-1)) = 21 + 42 + 105. <--- actual answer that works

  10^2 has 5  answers
  10^3 has 9  answers
  10^4 has 15 answers
  10^5 has 36 answers
  10^6 has 84 answers
=======
import time

START = time.time()
MOD   = 10**9 + 7
SIZE  = 10**8

#   Input: Size of array
#   Output: (array of non-repeating elements, array of repeating elements)
def getNumberSequences(size):
    allNumHash  = set([0])
    numberArray   = [0]
    num         = 0
    repeatIndex = -1

    for index in xrange(2,SIZE+1):
        num = (num **2 + 45) % MOD
        if num in allNumHash:
            repeatIndex = numberArray.index(num)
            break
        allNumHash.add(num)
        numberArray.append(num)

    nonRepeatingNumArr = numberArray[:repeatIndex]
    repeatingNumArr    = numberArray[repeatIndex:]
    return (nonRepeatingNumArr, repeatingNumArr)

#   Key:   (start, end)
#   Value: max possible value
naiveDPSolverDict = dict()
def naiveDPSolver(numberArray, start = 0, end = -1):
    if end == -1: #setup
        end = len(numberArray) -1
    if end -1 == start:
        return max(numberArray[start: end])
    if (start, end) in naiveDPSolverDict:
        return naiveDPSolverDict[(start, end)]
    if len(numberArray) > 120:
        pop_first = numberArray[start] \
                + sum(numberArray[start+1:end]) \
                -  naiveDPSolver(numberArray, start + 1, end)
        naiveDPSolverDict[(start,end)] = pop_first
        return naiveDPSolverDict[(start,end)]


    pop_first = numberArray[start] \
                + sum(numberArray[start+1:end]) \
                -  naiveDPSolver(numberArray, start + 1, end)
    pop_last  = numberArray[end]   \
                +sum(numberArray[start:end-1]) \
                - naiveDPSolver(numberArray, start, end - 1)
    naiveDPSolverDict[(start,end)] = max(pop_first, pop_last)

    return naiveDPSolverDict[(start, end)]


def iterativeDPSolver(numberArray):
    probSize = len(numberArray)
    answersDict   = dict()
    numberSumDict = dict()
    for i in xrange(probSize):
        answersDict[(i,i)]   = numberArray[i]
        numberSumDict[(i,i)] = numberArray[i]

    #Computing the next row of the problem
    for lengthOfChain in xrange(2,probSize):
        print lengthOfChain
        for start in xrange(0, probSize - lengthOfChain):
            end = start + lengthOfChain -1
            answersDict[(start,end)] = max( \
                    (numberArray[start] \
                        + numberSumDict[(start+1, end)] \
                        - answersDict[  (start+1, end)]), \
                    (numberArray[start] \
                        + numberSumDict[(start, end-1)] \
                        - answersDict[(start, end-1)])
            )
            numberSumDict[(start,end)] = numberSumDict[(start,end-1)] + numberArray[end]

        #Cleaning up the previous row to avoid running out of memory
        for start in xrange(0, probSize - lengthOfChain+1):
            end = start + lengthOfChain-2
            del answersDict[(start,end)]
            del numberSumDict[(start,end)]

    return answersDict[(0, probSize-2)]


nonRepeatingNums, repeatingNums = getNumberSequences(SIZE)
print len(nonRepeatingNums), len(repeatingNums)

repeatLen        = SIZE - len(nonRepeatingNums)
wrapAround       = repeatLen % len(repeatingNums)
numRepeat        = repeatLen // len(repeatingNums)
nonRepeatingNums = nonRepeatingNums + repeatingNums[:wrapAround]
repeatingNums    = repeatingNums[:wrapAround] + repeatingNums[wrapAround:]
noRepeatCost     = iterativeDPSolver(nonRepeatingNums)
repeatOnceCost   = iterativeDPSolver(nonRepeatingNums + repeatingNums)
repeatCost       = repeatOnceCost - noRepeatCost
answer           = noRepeatCost + repeatCost * numRepeat

print "The answer is:", answer
print "Time Taken:", time.time() - START

"""
Notes:

For size = 10^8, and mod = 10^9 + 7, 
The first number to repeat is 535424698,first occuring when index = 57956, and repeats at 65205
The cycle is 7248 ints
57956 + 7248 * 13788 + 6620
    = 64576 + 7248 * 13788

>>>>>>> Stashed changes

"""
