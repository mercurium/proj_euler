import time, math
START = time.time()
SIZE  = 10**3

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

"""
Sum of floored square roots from 1 to n, where m = int(sqrt(n)) is:
  1 * (2 * 1 + 1) + 2 * (2 * 2 + 1) + ... + m * (2*m +1) + (m+1) * (leftovers)
  = sum(i=1 to m)( 2m^2 + m) + leftovers
  -> 2 * (m * (m+1) * (2*m+1))/6 + m(m+1)/2 + leftovers
  -> m * (m+1) * (2m+1)/3 + m(m+1)/2 + leftovers
"""
def getNum(n):
  sqrtN  = int(math.sqrt(n))
  return (sqrtN * (sqrtN-1) * (sqrtN * 2 - 1))/ 3 \
         + (sqrtN * (sqrtN - 1 )) / 2 \
         + max(0,(n + 1 - sqrtN**2)) * sqrtN

def successFunc(target, num):
  if getNum(num) > target:
    return 1
  elif getNum(num) + int(math.sqrt(num+1)) < target:
    return -1
  return 0

def binSearch(lowerBound, upperBound, target):
  mid = (lowerBound + upperBound) / 2
  result = successFunc(target, mid)
  if result == 0:
    return mid
  elif result < 0:
    return binSearch((lowerBound + upperBound)/2, upperBound, target)
  else:
    return binSearch(lowerBound, (lowerBound + upperBound)/2, target)

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

target     = 10**2
upperBound = int((target * 3/2.) ** (2/3.) * 1.15)
lowerBound = int((target * 3/2.) ** (2/3.))
mid        = binSearch(lowerBound, upperBound, target)
print mid

print "Time taken:", time.time() - START

"""


We can sort of use "sum(int(math.sqrt(x)) for x in xrange(1,12926)) -> 973269 (actual # is 986231)"


"""
