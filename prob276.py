import time, math
from primes import gcd
START = time.time()
SIZE  = 10**3

def gcd3(a,b,c):
  return gcd(gcd(a,b),c)

# This counts the number of triangles with perimeter at most = size
def countNumSlow(size):
  count = 0
  countNums = [0] * size
  for c in xrange(size//2):
    for b in xrange(c+1):
      for a in xrange(min(b+1, size-b-c)):
        if a+b > c and a <= b:
          if gcd3(a,b,c) ==1:
            #print a,b,c, a+b+c
            count+=1
            countNums[a+b+c] +=1
  #for i in xrange(3,size):
    #print i, countNums[i]
  return count

# This counts the exact number of triangles with perimeter = size
def countExactN(size):
  count = 0
  for c in xrange(size//3, (size+1) //2):
    count += max(0, (c+1 - (size+1-c)/2))
    print c, max(0, (c+1 - (size+1-c)/2))
  return count

# This is an experiment to see how we can get countExactN in O(1) time
def countExactNTest(size):
  count = 0
  for c in xrange((size+2)//3, (size+1)//2):
    count +=  (size+1-c)/2
    print c,  (size+1-c)/2, c+1 - (size+1-c)/2
  return count
cent = countExactNTest

# Also an experiment to get to O(1) time for countExactN
def countExactNTest2(size):
  count = 0
  startVal = 1 if size % 3 != 1 else 2
  endVal   = 
  for c in xrange((size+2)/3, (size+1) //2):
    count += max(0, (c+1 - (size+1-c)/2))
cent2 = countExactNTest2

# This is an iterative method that figures out the number of primitive triangles of size S for each S < SIZE, then sums them together
def countNumLessThan(size):
  counts = [0] * (size+1)
  for i in xrange(3,size+1):
    counts[i] += countExactN(i)
    for j in xrange(2*i, size+1, i):
      counts[j] -= counts[i]
    #print i, countExactN(i), (2 - size // i )
  return sum(counts)

#slowAnswer = countNumSlow(SIZE+1)
#print "There are:", slowAnswer, "primitive triangles with perimeter <=", SIZE
#print "Time Taken:", time.time() - START
#
#START = time.time()

#fastAnswer = countNumLessThan(SIZE)
#print "There are:", fastAnswer, "primitive triangles with perimeter <=", SIZE

print "Time Taken:", time.time() - START


"""



"""
