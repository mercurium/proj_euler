import time
SIZE  = 10**14

def getPrimesLessThanN(n):
  largestPrimeFactors = range(n+1)
  primes = set([2])
  for i in xrange(3,n,2):
    if largestPrimeFactors[i] == i:
      primes.add(i)
      for j in xrange(i**2, n, i*2):
        largestPrimeFactors[j] = i
  return sorted(primes)

def getLargestPrimeFactorsRange(start,end):
  largestPrimeFactors = range(start,end+9)
  primeFactors        = getPrimesLessThanN(int(end**.5))

  print "Time taken for part 0:", time.time() - START

  for primeFactor in primeFactors:
    startCounter = ( primeFactor - start ) % primeFactor
    for i in xrange(startCounter, len(largestPrimeFactors), primeFactor):
      # TODO need a cleaner way to express these next four lines... not to mention this is stupidly inefficient
      while largestPrimeFactors[i] % primeFactor == 0:
        largestPrimeFactors[i] /= primeFactor
      if largestPrimeFactors[i] == 1:
        largestPrimeFactors[i] = primeFactor

  return largestPrimeFactors

def getLargestPrimeFactors(n):
  numPrimes = 0
  largestPrimeFactors = range(n+10)
  for i in xrange(2,n+10):
    if largestPrimeFactors[i] == i:
      numPrimes +=1
      for j in xrange(2*i, n+10, i):
        largestPrimeFactors[j] = i
  return largestPrimeFactors

def testFastMethod():
  start = SIZE - 10 * int(SIZE**0.5) # TODO: Unless the actual answer is really close to SIZE (< 10^9 away), this isn't going to work...
  largestPrimeFactors = getLargestPrimeFactorsRange(start, SIZE)
  largestSum          = 0

  print "Time taken for part 1:", time.time() - START
  runningSum = sum(largestPrimeFactors[-9:])
  for n in xrange(len(largestPrimeFactors)-9,1,-1):
    if runningSum > largestSum:
      largestSum = runningSum
      print start + n, runningSum, [ (round(x/(1.0 * (start+n)),4)) for x in largestPrimeFactors[n:n+9]], runningSum / (1.0 * (start+n))
    runningSum -= (largestPrimeFactors[n+8] - largestPrimeFactors[n-1])

    if (n+start) * 5 < largestSum:
      break
  print largestSum
  print "Time taken:", time.time() - START

def correctSlowMethod():
  largestPrimeFactors = getLargestPrimeFactors(SIZE)
  largestSum          = 0
  timesIncreased      = 0

  print largestPrimeFactors[-50:]
  print "Time taken for part 1:", time.time() - START

  runningSum = sum(largestPrimeFactors[SIZE:SIZE+9])
  for n in xrange(SIZE,1,-1):
    if runningSum > largestSum:
      timesIncreased +=1
      largestSum = runningSum
      print n, runningSum, [ (round(x/(1.0 * n),4)) for x in largestPrimeFactors[n:n+9]], runningSum / (1.0 * n)
      print n, runningSum, largestPrimeFactors[n:n+9], runningSum / (1.0 * n)
    runningSum -= (largestPrimeFactors[n+8] - largestPrimeFactors[n-1])

    if n * 5 < largestSum:
      break

  print largestSum, timesIncreased
  print "Time taken:", time.time() - START

print "Starting fast test method:"
START = time.time()
testFastMethod()
