import time
from fractions import Fraction as Fr

START  = time.time()

dieSides = [1,4,6,8,12,20]

numStart = 1

nextArr  = [0] + [Fr(1,numStart)] * numStart

iterSize = [1,4*numStart+1, 4*6+1, 4*6*8+1, 4*6*8*12+1, 4*6*8*12*20+1]

# die size iteration: 4,6,8,12,20
for i in xrange(1,5):#len(iterSize)):
  prevArr  = nextArr
  nextArr  = [0] * iterSize[i]
  dieSize  = dieSides[i]

  countArr = [0,1]
  # total number of dice being rolled
  for numDieRoll in xrange(1,len(prevArr)):
    print i, numDieRoll, len(prevArr)
    newCountArr = [0] * (dieSize * numDieRoll + 1)

    # The entry that we want to fill in for a spot
    for slot in xrange(1,len(newCountArr)-numDieRoll + 1):
      newCountArr[slot]           = sum(countArr[max(slot+1 - dieSize, 0): slot +1])
      nextArr[slot+numDieRoll-1] += newCountArr[slot] * prevArr[numDieRoll] / dieSize**numDieRoll
    countArr = newCountArr
  sqEV = sum( [j**2 * nextArr[j] for j in xrange(len(nextArr))] )
  EVsq = sum( [j * nextArr[j] for j in xrange(len(nextArr))] ) **2
  print i, sqEV, EVsq, sqEV - EVsq

sqEV = sum( [i**2 * nextArr[i] for i in xrange(len(nextArr))] )
EVsq = sum( [i * nextArr[i] for i in xrange(len(nextArr))] ) **2

print "Answer:", sqEV, EVsq, sqEV - EVsq
print "Time taken:", time.time() - START

"""
should just need to find expected value, and expected value of squaring the final die's value.
E[x^2] - E[x]^2

"""
