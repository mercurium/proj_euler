import math, time
from bitarray import bitarray

START = time.time()
SIZE = 10**6

#Find the number of semiprimes less than size.
def findNumSemiprimes(size):
  numSemiprimes = 0
  isPrime1 = bitarray(size) #(0,0) = untouched. (0,1) = one prime so far
  isPrime2 = bitarray(size) #(1,0) = two primes, (1,1) = more than two distinct prime factors

  for i in xrange(SIZE): #sadly, need to do this to avoid running low on memory
    isPrime1[i] = 0
    isPrime2[i] = 0

  def getVal(i):
    return isPrime1[i]*2+isPrime2[i]
  def setVal(i, val):
    if val > 3:
      val = 3
    isPrime1[i] = val/2
    isPrime2[i] = val%2

  for i in xrange(2,SIZE):
    if getVal(i) == 2:
      numSemiprimes+=1
    elif getVal(i) == 0:
      for j in xrange(2*i,SIZE,i):
        setVal(j, getVal(j)+1)
    else:
      pass #We don't care about the number if it's not a semiprime or a prime
  return numSemiprimes

def getPrimeList(size):
  possiblePrimes = bitarray(size)
  for i in xrange(SIZE): #sadly, need to do this to avoid running low on memory
    possiblePrimes[i] = 0

  primes = [2]
  for i in xrange(3,size):
    if possiblePrimes[i] == 0:
      for j in xrange(i**2, size, 2*i):
        possiblePrimes[j] = 1
      primes.append(i)
  return primes

answer = findNumSemiprimes(SIZE)

#print "The answer is:", answer
print "Time Taken:", time.time() - START


#Since we have four states to deal with, prime, notseen yet, 2 distinct factors, and more than two distinct factors, we need two bits per number to store them. This unfortunately requires two bitarrays instead of one, but at least the memory cost is relatively cheap.

"""

Too lazy to run this, but going by the expected running time (seems linear), it's probably going to be 10 minutes to run for 10^8, and it looked like it was going to take ~20 mb to run on 10^8.

This method is not going to work for problem 501 if we're expected to take 10,000x more space and time... estimated 200 gb of memory and 70 days... hm..



"""
