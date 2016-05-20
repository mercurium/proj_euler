#NOTE TODO need to solve it
import time
from primes import m_r
START = time.time()

count = 0
SIZE  = 10**5
MOD   = 10**9 +7

def get_pfactor(SIZE):
  pfactor = range(0,SIZE+1)
  for i in xrange(2,len(pfactor)):
    if pfactor[i] == i:
      for j in xrange(i*2,len(pfactor),i):
        pfactor[j] = i
  return pfactor

pfactor = get_pfactor(SIZE)

def factor(n):
  factors = []
  while n != 1:
    factors.append(pfactor[n])
    n /= pfactor[n]
  return factors

print "Part 1 done!", time.time() - START

val_dict = {}
for n in xrange(1,SIZE/2+1):

  # Add on the factors from the top
  for f in factor(SIZE-n+1):
    if f in val_dict:
      val_dict[f] +=1
    else:
      val_dict[f] = 1

  # Remove the denominator
  for d in factor(n):
    val_dict[d] -= 1
    if val_dict[d] == 0:
      del val_dict[d]

  # Increment count
  prod = 1
  for f in val_dict.keys():
    prod = ((1 + pow(f, val_dict[f],MOD)) * prod) % MOD
  count = (count + prod*2) % MOD # The cases for n are symmetric, so let's only do half the work to finish twice as fast!

  # Progress counter
  if n% 100 == 0:
    print n, time.time() - START

count -= prod # We don't want to count the middle case twice!
count = (count - pow(2,SIZE,MOD)+2) % MOD

print "Answer is:", count
print "Time Taken:", time.time() - START


"""



"""
