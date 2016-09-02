import time
START = time.time()
SIZE  = 47
MOD   = 3**15

# T dictionary fields:
# (sumOfDigits, numberOfDigits) : (count, numSumTotal)
T        = dict() # T with leading 0
T[(0,0)] = (1,0)

def addToDict(valDict, key, value):
  if key not in valDict:
    valDict[key] = value
  else:
    oldCount, oldSum = valDict[key]
    valDict[key] = (oldCount + value[0], oldSum + value[1])

for nthDig in xrange(1, SIZE//2 + 1):
  for dig in xrange(10):
    for oldDigSum in xrange(0, nthDig * 9 - 8):
      count, sumTotal = T[(oldDigSum, nthDig - 1)]
      addToDict(T, \
          (oldDigSum + dig, nthDig), \
          (count, sumTotal * 10 + dig* count))


totalSum = 0

for numDig in xrange(1,SIZE+1):
  halfDig = numDig // 2
  isOdd   = numDig % 2 == 1
  for sumOfDig in xrange(0, halfDig * 9 + 1):
    # set a is the last n//2 digits, which can have leading zeroes
    aCount, aSum = T[(sumOfDig, halfDig)]
    bCount, bSum = T[(sumOfDig, halfDig)]
    if (sumOfDig, halfDig - 1) in T:
      # set b is the first n//2 digits, which can't have a leading 0
      bCount -= T[(sumOfDig, halfDig - 1)][0]
      bSum   -= T[(sumOfDig, halfDig - 1)][1]

    if isOdd:
      totalSum += (aCount * bSum * 10 ** (numDig - halfDig) \
                  + bCount * aSum) * 10  \
                  + 45 * bCount * aCount * 10**halfDig
    else:
      totalSum += (aCount * bSum * 10 **  halfDig + bCount * aSum)


print "Answer:", totalSum % MOD
print "Time taken:", time.time() - START

"""

totalSum = 0
for dig in xrange(1,SIZE+1):

187 = 98 + 89

99(9),

Congratulations, the answer you gave to problem 217 is correct.

You are the 1034th person to have solved this problem.

jchen@jchen-mbp 13:29:09 ~/Developer/proj_euler(master) % pypy prob217.py
Answer: 6273134
Time taken: 0.116122961044



"""
