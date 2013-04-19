import time
start = time.time()
from bitarray import bitarray

size = 10**7
threshold = 15499/94744.
pc = bitarray('0'*size)
max_factor = [0,1] + [0] * size

for i in xrange(2,size):
  if pc[i] == 0:
    for j in xrange(i,size,i):
      max_factor[j] = i
      pc[j] = 1

def pfactor(n):
  if n == 1: return [1]
  return [max_factor[n]] + pfactor(n/max_factor[n])

print "Time Taken:", time.time() - start
minz = 1
for i in xrange(1,size):
  prod = 1.0
  factors = pfactor(i)
  for j in xrange(0,len(factors)-1):
    if factors[j] != factors[j+1]:
      prod =prod * (factors[j] -1) / factors[j]
  if minz > prod: minz = prod
  if prod < threshold: 
    print i, prod
    break

print minz
print "Time Taken:", time.time() - start

#okay, it turns out this is a stupid way to do it. "resilience = totient(n)/(n-1) so... lol... not very hard to deal with.
