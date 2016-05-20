import time
import collections

START = time.time()
SIZE  = 10**8
K     = 10**5


def pfactorGen(size): #for each number n, return some factor of it.
  pfactorArray = [0,1,2] + [1,2] *(size/2-1)
  for i in xrange(3,size,2):
    if pfactorArray[i] == 1:
      for j in xrange(i**2,size,i*2):
        pfactorArray[j] = i
      pfactorArray[i] = i
  return pfactorArray

pfactorArray = pfactorGen(SIZE)

def getMaxAndUpdate(deque, position):
  [value, valuePosition] = deque[0]
  while valuePosition + K <= position:
    deque.popleft()
    [value, valuePosition] = deque[0]
  return value

def insertValue(deque, newValue, newPosition):
  if newValue < 128:
    return
  while len(deque) is not 0:
    [tailValue,tailPosition] = deque[-1]
    if tailValue <= newValue:
      deque.pop()
    else:
      break
  deque.append([newValue, newPosition])

def pfactor(n):
  prime_factors = []
  while n > 1:
    prime_factors.append(pfactorArray[n])
    n /= pfactorArray[n]
  prime_factors.sort()
  return prime_factors

def computeNumDivisors(number):
  product           = 1
  currentNumber     = -1
  productMultiplier = 1
  prime_factors = pfactor(number)
  for num in prime_factors:
    if currentNumber is num:
      productMultiplier +=1
    else:
      currentNumber     = num
      product          *= productMultiplier
      productMultiplier = 2
  return product * productMultiplier

def main(size, k):
  maxValues = collections.deque()

  answerSum = 0
  for index in xrange(1,k):
    numDivisors = computeNumDivisors(index)
    insertValue(maxValues, numDivisors, index)

  for index in xrange(k,size + 1):
    numDivisors = computeNumDivisors(index)
    insertValue(maxValues, numDivisors, index)
    answerSum += getMaxAndUpdate(maxValues, index)
  print answerSum

main(SIZE,K)
print "Time Taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 485 is correct.

You are the 236th person to have solved this problem.

Answer : 51281274340
Time Taken: 335.649747133
Time Taken: 270.47121501  This was done by ignoring values that would not have been the largest value anyways.
Time Taken: 257.42475915  This was done by being even smarter about ignoring small values



"""
