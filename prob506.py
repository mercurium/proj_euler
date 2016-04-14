import time, math
START = time.time()
SIZE  = 10**6
MOD   = 11111**2

def pow10(power):
  base = 1 + (10**5-1) * (power // 5) % MOD
  return (base * 10**(power % 5)) % MOD

seq         = [1,2,3,4,3,2]
seqLen      = 6

startPos    = [0,0,1,2,3,4,0,3,5,3,0,4,3,2,1,0]
endPos      = [0,1,2,3,4,0,3,5,3,0,4,3,2,1,0]
startSeqSum = [0,0,14,12,9,5,0,9,2,9,0,5,9,12,14]


startSeq   = [
    0,
    0, \
    23432, \
    3432, \
    432, \
    32, \
    0, \
    432, \
    2, \
    432, \
    0, \
    32, \
    432, \
    3432, \
    23432, \
]
endSeq     = [
    0, \
    1, \
    12, \
    123, \
    1234, \
    0, \
    123, \
    12343, \
    123, \
    0, \
    1234, \
    123, \
    12, \
    1, \
    0, \
]

prevCost    = startSeq[:]

# =================================================================================
prevCost   = startSeq[:]
costDict   = {}

seqPointer = 0
totalSum   = 0
adjustment = 16 + (SIZE % 15)

# could probably integrate 1-15 as well, but it's a hassle
for n in xrange(1, min(15,SIZE+1)):
  numSum = 0
  digSum = 0
  while numSum < n:
    numSum     += seq[seqPointer]
    digSum      = (digSum * 10) % MOD
    digSum     += seq[seqPointer]
    seqPointer  = (seqPointer + 1) % seqLen
  totalSum += digSum

for n in xrange(15, min(adjustment+15, SIZE+1)):
  k          = n % 15
  # start of seq
  digSum  = prevCost[k]

  # mid of seq, repeating 123432...etc
  if n - startSeqSum[k] >= 15:
    digSum = (digSum * 10**6 + 123432) % MOD
  prevCost[k] = digSum

  # end of seq
  digSum    = digSum * 10**endPos[k] + endSeq[k] % MOD
  totalSum += digSum

  # keeping track of beginning costs to be more efficient later
  if n >= adjustment:
    numStepReq = endPos[k] # since we need to adjust by the number of elements at the end... this part counts
    prevCostEndPos, seqEndCost,count = 0,0,0
    if numStepReq in costDict:
      prevCostEndPos, seqEndCost, count = costDict[numStepReq]
    prevCostEndPos       += prevCost[k]
    seqEndCost           += endSeq[k]
    costDict[numStepReq]  = (prevCostEndPos, seqEndCost, count+1)


for key in costDict.keys():
  prevCostEndPos, seqEndCost, count = costDict[key]
  numTimesApplied = SIZE//15 - 2

  for multiplier in xrange(SIZE//15 - 2):
    prevCostEndPos = (prevCostEndPos * 10**6 + 123432 * count) % MOD

    digSum    = prevCostEndPos * 10**key + seqEndCost % MOD
    totalSum += digSum

print "Answer:", totalSum % MOD
time1 = time.time() - START
print "Time taken:", time1

# =================================================================================
# reset conditions
START      = time.time()
prevCost   = startSeq[:]
costDict   = {}

seqPointer = 0
totalSum   = 0
adjustment = 16 + (SIZE % 15)

# could probably integrate 1-15 as well, but it's a hassle
for n in xrange(1, min(15,SIZE+1)):
  numSum = 0
  digSum = 0
  while numSum < n:
    numSum     += seq[seqPointer]
    digSum      = (digSum * 10) % MOD
    digSum     += seq[seqPointer]
    seqPointer  = (seqPointer + 1) % seqLen
  totalSum += digSum

for n in xrange(15, min(adjustment+15, SIZE+1)):
  k          = n % 15
  # start of seq
  digSum  = prevCost[k]

  # mid of seq, repeating 123432...etc
  if n - startSeqSum[k] >= 15:
    digSum = (digSum * 10**6 + 123432) % MOD
  prevCost[k] = digSum

  # end of seq
  digSum    = digSum * 10**endPos[k] + endSeq[k] % MOD
  totalSum += digSum

  # keeping track of beginning costs to be more efficient later
  if n >= adjustment:
    numStepReq = endPos[k] # since we need to adjust by the number of elements at the end... this part counts
    prevCostEndPos, seqEndCost,count = 0,0,0
    if numStepReq in costDict:
      prevCostEndPos, seqEndCost, count = costDict[numStepReq]
    prevCostEndPos       += prevCost[k]
    seqEndCost           += endSeq[k]
    costDict[numStepReq]  = (prevCostEndPos, seqEndCost, count+1)


numTimesApplied = SIZE//15 - 2

for key in costDict.keys():
  prevCostEndPos, seqEndCost, count = costDict[key]
  headCost        = prevCostEndPos * pow10(numTimesApplied * 6)

  multiplier    = 0
  for power in xrange(0,5):
    k = pow(10,power)
    b = (numTimesApplied + 1 - power) / 5
    a = 10**5 - 1

    multiplier += k * b + 9 * k * b * a + 54 * k * (b * (b+1)/2) * a

  digSum = multiplier * prevCostEndPos + seqEndCost * b
  # todo: still missing the mid section...

  for multiplier in xrange(SIZE//15 - 2):
    prevCostEndPos = (prevCostEndPos * 10**6 + 123432 * count) % MOD

    digSum    = prevCostEndPos * 10**key + seqEndCost % MOD
    totalSum += digSum

print "Answer:", totalSum % MOD
time2 = time.time() - START
print "Time taken:", time2
print "Second method is faster by a factor of:", time1 / time2

'''
10^5k = (10^5 - 1) * k + 1 % 11,111^2


123454321 = 41**2 * 271**2
1234321   = 11**2 * 101**2

10**5 % (41 * 271) = 1
10**55555 % 123454321 = 1
'''

