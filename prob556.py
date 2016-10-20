import time, math
START = time.time()
SIZE  = 10**2

squares = set([x**2 for x in xrange(0, int(math.sqrt(SIZE))+1)])

count = 0
for a in xrange(0, int(math.sqrt(SIZE))+1):
  for b in xrange(0, int(math.sqrt(SIZE))+1):
    if a**2 + b**2 > SIZE:
      continue
    if (a**2 + b**2 in squares):
      continue
    count += 1

print count


"""
Units: 1,-1,i,-i
Primes:
  (1+i)
  (1+2i)

"""
