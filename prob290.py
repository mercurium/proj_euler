from bitarray import bitarray
import sys
import time

start = time.time()

size = 10**5
if len(sys.argv) > 1:
  size = int(sys.argv[1])

debug = False
if len(sys.argv) > 2:
    debug = (sys.argv[2] == 't')

def test(n):
  count = 0
  nums = []
  for i in xrange(0,n,9):
    if sum(int(x) for x in str(i)) == sum(int(x) for x in str(137*i)):
      count += 1
      nums += [i]
  return (count,nums)

def factor_lst(size):
  primes = [2]
  stuff = bitarray('0' * size)
  for i in xrange(3,size,2):
    if stuff[i] == 0:
      for j in xrange(i**2,size,i*2):
        stuff[j] = 1
      primes += [i]
  return primes

def pfactor_gen(size):
  stuff = [0,1,2] + [1,2] *(size/2-1)
  for i in xrange(3,size,2):
    if stuff[i] == 1:
      for j in xrange(i**2,size,i*2):
        stuff[j] = i
      stuff[i] = i
  return stuff

def factor(n):
  factors = []
  while n > 1:
    factors += [pfactor[n]]
    n/= pfactor[n]
  return sorted(factors)


count,lst = test(size)
if debug:
  pfactor = pfactor_gen(size)
  for i in lst:
    print i, i/9, factor(i/9)

print "Answer for size", size, "is", count
print "Time Taken:", time.time() - start