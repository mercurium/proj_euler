import time
START = time.time()
SIZE  = 5

cache = dict()
def count(numDig, currentNum, numSum, numOccur=0):
  if (numDig, currentNum, numSum, numOccur) in cache:
    return cache[(numDig, currentNum, numSum, numOccur)]
  if numSum == 0:
    print numDig, currentNum, numSum, numOccur
    return 1
  if numSum < 0 or currentNum == 0 or numDig == 0:
    return 0
  ans = count(numDig, currentNum - 1, numSum, 0) * (numOccur+1) \
       + count(numDig-1, currentNum, numSum - currentNum, numOccur +1)
  cache[(numDig, currentNum, numSum, numOccur)] = ans
  return ans

print count(2,5,5)


T    = dict() # T with leading 0s
TnL0 = dict() # T with no leading 0s


for numLen in xrange(0, SIZE/2):
  for numSum in xrange(0,numLen * 9):
    pass
    #T[(numLen, numSum)] = count(numLen, currentNum, numSum, numOccur)
