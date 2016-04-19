import time, math, sys
import unittest
sys.setrecursionlimit(500)

tester = unittest.FunctionTestCase('==')

SIZE  = 10**18
START = time.time()

def slowFunc(size):
  arr            = [1,1]
  nextCircledInt = 2
  
  for arrIndex in xrange(1,size):
    if len(arr) > size:
      break
    nextNum = arr[arrIndex]
  
    # Add on the next math.sqrt(nextNum) on at a time, and increment the counter as such
    arr.extend(xrange(nextCircledInt, nextCircledInt+int(math.sqrt(nextNum))))
    nextCircledInt += int(math.sqrt(nextNum))
  
    # Append the number that we just incremented by
    arr.append(nextNum)
  
  arr = arr[:size]
  
  countArr = [0] * (max(arr) + 1)
  for i in xrange(len(arr)):
    countArr[arr[i]] += 1

  answer = []
  # This chunk is the part for finding the answer once I find the frequency of answers
  nextVal = 1
  for countVal in xrange(max(countArr), 1, -1):
    if (countVal-1) in countArr:
      nextVal = max(countArr.index(countVal-1)-1, 1)
    answer.append(nextVal)
  answer.append(len(countArr) -1)

  return answer


def getNum(n):
  sqrtN  = int(math.sqrt(n))
  return (sqrtN * (sqrtN-1) * (sqrtN * 2 - 1))/ 3 \
         + (sqrtN * (sqrtN - 1 )) / 2 \
         + max(0,(n + 1 - sqrtN**2)) * sqrtN
gn = getNum

def binSearch(func, lowerBound, upperBound, target):
  mid = (lowerBound + upperBound) / 2
  result = func(mid)
  if result > target:
    return binSearch(func, lowerBound, (lowerBound + upperBound)/2, target)
  elif func(mid+1) < target:
    return binSearch(func, (lowerBound + upperBound)/2, upperBound, target)
  else:
    return mid


def checkCorrect(arr):
  def checkFloor(arr, i):
    return arr[i] >= sum([gn(x) for x in arr[:i]])
  def checkCeil(arr, i):
    return arr[i] <= sum([gn(x) for x in arr[:i-1]]) + gn(arr[i-1]+1)
  for i in xrange(3, len(arr)):
    if not checkFloor(arr, i) or not checkCeil(arr, i):
      return False
  return True

def mainFunc(size):
  arr = [size]
  for i in xrange(20):
    m = arr[-1]
    if m == 1:
      break
    arr.append(binSearch(lambda x: x + gn(x), 0, m, m))
  
  arr[0] = gn(arr[1])
  arr.append(1)
  arr = arr[::-1]
  
  for k in xrange(10):
    for j in xrange(len(arr)):
      for i in xrange(1,len(arr)-1):
        arr[i] = binSearch(lambda x: sum([gn(elem) for elem in arr[:i]]) + gn(x), 0, arr[i+1], arr[i+1])


      for i in xrange(1,len(arr)):
        while arr[i] > sum([gn(x) for x in arr[:i-1]]) + gn(arr[i-1]+1):
          print "increasing it by 1", arr, arr[i-1]
          arr[i-1] +=1
        while arr[i] < sum([gn(x) for x in arr[:i]]):
          print "decreasing it by 1", arr, arr[i-1]
          arr[i-1] -=1

    
    arr[-1] = size - sum(arr[:-1])
    if checkCorrect(arr):
      print arr, size, checkCorrect(arr)
      return arr
    print arr, size, checkCorrect(arr)
  
  return arr

print mainFunc(SIZE)
#for i in xrange(10**4+121,10**5):
#  print i, slowFunc(i)
#  tester.assertEquals(slowFunc(i), mainFunc(i))

"""
1
2
4
8
21
79
7,557
479,532
221,618,858
2,174,801,175,768,428,548


past failed casese: 10,038, 10**5, 10,087, 10**18

"""
