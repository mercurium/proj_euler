import time, math
START = time.time()
SIZE  = 10**3

arr            = [1,1]
nextCircledInt = 2

for arrIndex in xrange(1,SIZE):
  if len(arr) > SIZE:
    break
  nextNum = arr[arrIndex]
  arr.extend(xrange(nextCircledInt, nextCircledInt+int(math.sqrt(nextNum))))
  nextCircledInt += int(math.sqrt(nextNum))
  arr.append(nextNum)

arr = arr[:SIZE]

countArr = [0] * (max(arr) + 1)
for i in xrange(len(arr)):
  countArr[arr[i]] += 1


print sum(arr[:SIZE])
print "Time taken:", time.time() - START

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

target   = 10**18
upperLim = int((target * 3/2.) ** (2/3.) * 1.15)
lowerLim = int((target * 3/2.) ** (2/3.))
m = (upperLim + lowerLim)/2
prevGuess = getNum(m)
while prevGuess > target or prevGuess + int(math.sqrt(m+1)) < target:
  if prevGuess > target:
    upperLim = m
    m        = (m + lowerLim) / 2
  else:
    lowerLim = m
    m        = (m + upperLim) / 2
  prevGuess = getNum(m)

print m, prevGuess, prevGuess + int(math.sqrt(m+1)), upperLim, lowerLim
print "Time taken:", time.time() - START

"""


We can sort of use "sum(int(math.sqrt(x)) for x in xrange(1,12926)) -> 973269 (actual # is 986231)"


"""
