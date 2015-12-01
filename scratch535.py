import time, math,sys
sys.setrecursionlimit(50)

START = time.time()
SIZE  = 10**4

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

print sum(arr[:SIZE])
print "Time taken:", time.time() - START

# This chunk is the part for finding the answer once I find the frequency of answers
nextVal = 1
for countVal in xrange(max(countArr), 1, -1):
  if (countVal-1) in countArr:
    nextVal = max(countArr.index(countVal-1)-1, 1)
  print str(countVal) + ":", nextVal, '\t'
print "1:", len(countArr) -1, '\t'
# This chunk is the part for finding the answer once I find the frequency of answers


print "Time taken:", time.time() - START
START = time.time()

def getNum(n):
  sqrtN  = int(math.sqrt(n))
  return (sqrtN * (sqrtN-1) * (sqrtN * 2 - 1))/ 3 \
         + (sqrtN * (sqrtN - 1 )) / 2 \
         + max(0,(n + 1 - sqrtN**2)) * sqrtN + n
gn = getNum

def getAnsFunc(n):
  print "going two levels deeper on:", n
  getNumResult = getNum(n)
  oneLvlLower = binSearch(getAnsFunc2, 0, n, n)
  print "The getNum result for", n, "is:", getNumResult, n, oneLvlLower
  return getNumResult + oneLvlLower

def getAnsFunc2(n):
  print "going one level deeper on:", n
  getNumResult = getNum(n)
  oneLvlLower = binSearch(getNum, 0, n, n)
  print "The getNum2 result for", n, "is:", getNumResult, n, oneLvlLower
  return getNumResult + oneLvlLower

def successFunc(func, target, num):
  funcResult = func(num)
  print "Num:", num, funcResult
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

#upperBound = int((SIZE * 3/2.) ** (2/3.))
#lowerBound = int((SIZE * 3/2.) ** (2/3.) * .2)
#print "Lower bound:", lowerBound, "Upper Bound:", upperBound
#mid        = binSearch(getNum, lowerBound, upperBound, SIZE)
#print mid
#print "\n\n"
#mid        = binSearch(getAnsFunc, lowerBound, upperBound, SIZE)
#print mid
#
#print "Time taken:", time.time() - START

