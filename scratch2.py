import time, math, sys
sys.setrecursionlimit(500)

SIZE  = 10**9
START = time.time()

if SIZE <= 10**7:
  arr            = [1,1]
  nextCircledInt = 2
  
  for arrIndex in xrange(1,SIZE):
    if len(arr) > SIZE:
      break
    nextNum = arr[arrIndex]
  
    # Add on the next math.sqrt(nextNum) on at a time, and increment the counter as such
    arr.extend(xrange(nextCircledInt, nextCircledInt+int(math.sqrt(nextNum))))
    nextCircledInt += int(math.sqrt(nextNum))
  
    # Append the number that we just incremented by
    arr.append(nextNum)
  
  arr = arr[:SIZE]
  
  countArr = [0] * (max(arr) + 1)
  for i in xrange(len(arr)):
    countArr[arr[i]] += 1
  print "Time taken:", time.time() - START
  
  # This chunk is the part for finding the answer once I find the frequency of answers
  nextVal = 1
  for countVal in xrange(max(countArr), 1, -1):
    if (countVal-1) in countArr:
      nextVal = max(countArr.index(countVal-1)-1, 1)
    print str(countVal) + ":", nextVal, '\t'
  print "1:", len(countArr) -1, '\t'
  # This chunk is the part for finding the answer once I find the frequency of answers
  print sum(arr[:SIZE])
  print "Time taken:", time.time() - START
  START = time.time()


def getNum(n):
  sqrtN  = int(math.sqrt(n))
  return (sqrtN * (sqrtN-1) * (sqrtN * 2 - 1))/ 3 \
         + (sqrtN * (sqrtN - 1 )) / 2 \
         + max(0,(n + 1 - sqrtN**2)) * sqrtN
gn = getNum

def successFunc(func, target, num):
  funcResult = func(num)
  #print "Num:", num, funcResult
  if funcResult > target:
    return 1
  elif func(num+1) < target:
    return -1
  return 0

def binSearch(func, lowerBound, upperBound, target):
  mid = (lowerBound + upperBound) / 2
  result = successFunc(func, target, mid)
  if result == 0:
    return mid
  elif result < 0:
    return binSearch(func, (lowerBound + upperBound)/2, upperBound, target)
  else:
    return binSearch(func, lowerBound, (lowerBound + upperBound)/2, target)

arr2 = [SIZE]
for i in xrange(20):
  m = arr2[-1]
  if m == 1:
    break
  arr2.append(binSearch(lambda x: x + gn(x), 0, m, m))

arr2[0] = gn(arr2[1])
arr2.append(1)
arr2 = arr2[::-1]
print arr2


for k in xrange(5):
  for j in xrange(len(arr2)):
    rollingSum = 1
    for i in xrange(1,len(arr2)-1):
      arr2[i] = binSearch(lambda x: rollingSum + gn(x), 0, arr2[i+1], arr2[i+1])
      rollingSum += gn(arr2[i])
  
  print sum(arr2)
  arr2[-1] = arr2[-1] - (sum(arr2) - SIZE)
  print arr2

print arr2
print sum([ x*(x+1)/2 for x in arr2])
print "Time taken:", time.time() - START
