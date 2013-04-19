#cool. So the method of attack is, figure out the best strategy given n digits of precision then test for .ab0, .ab1, .ab2, ...etc then compute for .abcd0, .abcd1, ...yeah. That's the compute method

#then the main method iterates through those choices.
#0.999992836187
#Time Taken: 11.9163689613
import time
start = time.time()
from primes import ncr

def compute(f):
  prob = 0
  loss = 1.-f
  win  = 1.+2*f
  for i in xrange(0,1001):
    if loss**i * win ** (1000-i) >= 10**9:
      prob += ncr(1000,i)
  return prob

def main():
  top = 0.1
  for i in xrange(2,13):
    lst = [0]*20
    for dig in xrange(-9,9):
      lst[dig] = compute(top + dig/(10.**i))
    maxz,index = 0,-1
    for j in range(-9,10):
      if lst[j] > maxz:
        maxz = lst[j]
        index = j
    top += index / (10.**i)
    print top
  print compute(top) / 2**1000.

main()
print "Time Taken:", time.time() -start
