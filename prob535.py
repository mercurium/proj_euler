import time, math, sys
sys.setrecursionlimit(500)

SIZE  = 10**18
START = time.time()

# Technically unused, but it's useful for computing an approximation for how high the next number in the recursion would be.
def getNum(n):
  sqrtN  = int(math.sqrt(n))
  return (sqrtN * (sqrtN-1) * (sqrtN * 2 - 1))/ 3 \
         + (sqrtN * (sqrtN - 1 )) / 2 \
         + max(0,(n + 1 - sqrtN**2)) * sqrtN
gn = getNum

# Super simple binary search function
def binSearch(func, lowerBound, upperBound, target):
  mid = (lowerBound + upperBound) / 2
  result = func(mid)
  if result > target:
    return binSearch(func, lowerBound, (lowerBound + upperBound)/2, target)
  elif func(mid+1) < target:
    return binSearch(func, (lowerBound + upperBound)/2, upperBound, target)
  else:
    return mid

def createApproxAnswerArray(size):
  arr = [size]
  for i in xrange(20):
    m = arr[-1]
    if m == 1:
      break
    arr.append(binSearch(lambda x: x + gn(x), 0, m, m))

  arr[0] = gn(arr[1])
  arr.append(1)
  arr = arr[::-1]
  return arr

def fixUpAnswerArray(arr, size):
  for k in xrange(10):
    for j in xrange(len(arr)):
      for i in xrange(1,len(arr)-1):
        getPastNumSum = lambda x: sum([gn(elem) for elem in arr[:i]]) + gn(x)
        arr[i]        = binSearch(getPastNumSum, 0, arr[i+1], arr[i+1])

        while arr[i] > sum([gn(x) for x in arr[:i-1]]) + gn(arr[i-1]+1):
          arr[i-1] +=1
        while arr[i] < sum([gn(x) for x in arr[:i]]):
          arr[i-1] -=1

    arr[-1] = size - sum(arr[:-1])
  return arr

def mainFunc(size):
  arr = createApproxAnswerArray(size)
  return fixUpAnswerArray(arr, size)

answer = sum([ x*(x+1)/2 for x in mainFunc(SIZE)])
print answer % 10**9
print "Time Taken:", time.time() - START


"""
We can sort of use "sum(int(math.sqrt(x)) for x in xrange(1,12926)) -> 973269 (actual # is 986231)"

Answer: 611778217
Time Taken: 0.133980989456

I feel like I sort of cheated... I mean, I got the right answer, and this code is solely my own, but it doesn't necessarily give the right answer for some sizes... :x


"""
