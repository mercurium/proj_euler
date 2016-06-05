import time
START = time.time()
SIZE  = 10**6 *60 + 1

def addToDict(valsDict, key, value):
  if key in valsDict:
    valsDict[key] = (valsDict[key][0]+1,valsDict[key][1] + value)
  else:
    valsDict[key] = (1,value)

numDivisors = [0,1] + [2] * (SIZE-1)
for i in xrange(2,SIZE+1):
  for j in xrange(i*2, SIZE+1, i):
    numDivisors[j] += 1

print "Time Taken:", time.time() - START

triNumDivisors = [0] * SIZE
for i in xrange(1,SIZE):
  if i % 2 == 0:
    triNumDivisors[i] = numDivisors[i/2] * numDivisors[i+1]
  else:
    triNumDivisors[i] = numDivisors[i] * numDivisors[(i+1)/2]

del numDivisors
print "Time Taken:", time.time() - START

largestVal  = max(triNumDivisors)
valCount    = dict()
numGreater  = [0] * len(triNumDivisors)
answerCount = 0

for index in xrange(SIZE-1,0,-1):
  for n in xrange(0, triNumDivisors[index]):
    if n in valCount:
      # valCount[n][0] is the number of k where f(k) = n and k > index
      # valCount[n][1] is the number of pairs f(j) < f(k) = n < f(index) where index < k < j
      numGreater[index] += valCount[n][0]
      answerCount       += valCount[n][1]

  addToDict(valCount,triNumDivisors[index], numGreater[index])

print "Answer:", answerCount % 10**18

print "Time Taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 378 is correct.

You are the 496th person to have solved this problem.

147534623725724718
Time Taken: 197.984318972 # Using pypy... urgh. Normal python would have been way too slow @.@

Okay. Pretty simple problem here. First off, we need to find the number of divisors of a triangle number n(n+1)/2.
Since n and n+1 are relatively prime, this is:
    numDivisors(n/2) x numDivisors(n+1) if n% 2 == 0
  else
    numDivisors(n) x numDivisors((n+1)/2) if n% 2 == 1

After that, going backwards, we keep track of how many occurences we have seen of each numDivisorCount, and then increment it



"""
