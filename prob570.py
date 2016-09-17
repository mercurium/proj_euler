import time
from primes import gcd
START = time.time()
SIZE  = 5000

# (iteration, orderTriangle, orderSide1, orderSide2, orderSide3)
countDict = dict()

countDict[(1, 1, 0, 0, 0)] = 1

def insertIntoDict(valDict, key, value):
  if key[1] > 3:
    return # no op on numbers greater than 3
  if key in valDict:
    valDict[key] += value
  else:
    valDict[key] = value

def appendEntry(oldEntry):
  iteration, orderTriangle, orderSide1, orderSide2, orderSide3 = oldEntry
  count = countDict[oldEntry]

  insertIntoDict(countDict, (iteration + 1, orderTriangle, orderSide1, orderSide2, orderTriangle + 1), count)
  insertIntoDict(countDict, (iteration + 1, orderTriangle, orderSide3, orderSide2, orderTriangle + 1), count)
  insertIntoDict(countDict, (iteration + 1, orderTriangle, orderSide1, orderSide3, orderTriangle + 1), count)


  insertIntoDict(countDict, (iteration + 1, orderSide1+1, orderTriangle+1, orderSide1, orderSide1), count)
  insertIntoDict(countDict, (iteration + 1, orderSide2+1, orderTriangle+1, orderSide2, orderSide2), count)
  insertIntoDict(countDict, (iteration + 1, orderSide3+1, orderTriangle+1, orderSide3, orderSide3), count)
  
count = -6 # ignore the case where size = 2
for order in xrange(2,SIZE+1):
  for key in filter((lambda key: key[0] == order-1), countDict.keys()):
    appendEntry(key)
  val1 = sum(countDict[key] for key in filter( (lambda key: key[0] == order and key[1] == 1), countDict.keys()))
  val3 = sum(countDict[key] for key in filter( (lambda key: key[0] == order and key[1] == 3), countDict.keys()))
  count += gcd(val1, val3)
  if gcd(val1, val3) > 30:
    print order, gcd(val1, val3)


print count
print "Time Taken:", time.time() - START
