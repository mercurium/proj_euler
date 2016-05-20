#NOTE TODO need to solve it
import time, random
START = time.time()

numIter = 10**5
count   = 0
for iteration in range(numIter):
  L = [] # larry
  R = [] # robin
  tempCount = 0
  for i in range(50):
    randNum = random.randint(1,10)

    # larry
    if randNum in L:
      tempCount +=1
      a = L.index(randNum)
      del L[a]
    else:
      if len(L) == 5:
        L.pop(0)
    L.append(randNum)

    # Robin
    if randNum in R:
      tempCount -=1
    else:
      if len(R) == 5:
        R.pop(0)
      R.append(randNum)
  count += abs(tempCount)
print count*1.0/numIter
print "Time Taken:", time.time() - START
