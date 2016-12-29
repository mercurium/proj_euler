#NOTE TODO need to solve it
import time, math
from primes import gcd, get_totient
START = time.time()
LIM   = 10**8


totientVals = get_totient(int(math.sqrt(LIM) + 10))

# naive method. Not bad, .04737 seconds for 10^6
count = 0
for m in xrange(2,int(math.sqrt(LIM))+1):
  if m**2 > LIM:
    break

  # \/ this part is the slowest.
  if m**2 + (m-1)**2 > LIM:
    nRange = xrange(1,m,2) if m%2 == 0 else xrange(2,m,2)
    for n in nRange:
      if m**2 + n**2 > LIM:
        break
      if gcd(m,n) != 1:
        continue
      count += 1
  elif m % 2 == 1:
    count += totientVals[m] / 2
  else:
    count += totientVals[m]



print "Answer:", count
print "Time taken:", time.time() - START


"""
Time taken: 0.120429039001 # time for 10^7
Time taken: 0.00853085517883 # time for 10^7 excluding the slowest part... 15x faster to exclude it... gg
computing the numbers that don't let us go up to the limit for n are the slowest ones, by a huge factor.


"""
