import time
START = time.time()
SIZE  = 10**4
# Problem size = 10^8

def get_primes_less_than(size):
  primes = [2]
  stuff = [0,1,2] + [1,2] *(size/2-1)
  for i in xrange(3,size,2):
    if stuff[i] == 1:
      for j in xrange(i**2,size,i*2):
        stuff[j] = i
      stuff[i] = i
      primes.append(i)
  return primes

primesList = get_primes_less_than(SIZE)
primeSet   = set(primesList)
primesSum  = 0
for i in xrange(len(primesList)):
  for j in xrange(i):
    c,b = primesList[i], primesList[j]
    if (b+1)**2 % (c+1) == 0 and ((b+1)**2 / (c+1) - 1) in primeSet:
      a = (b+1)**2 / (c+1) - 1
      primesSum += a + b + c
      #print a,b,c


print primesSum
print "Time Taken:", time.time() - START


"""
a,b,c
b/a = r
c/b = r
b^2 = a * c

a = k
b = kr
c = kr^2

Optimizations:
  - If we know 'b', we only have to check other primes 'c' where (c+1) | (b+1)^2
    - Might be much faster than iterating through each prime > 'b'.
    - Worst case, still O(n^2). Probably drops it closer to O(8n) though.
    - Still probaby worth doing...
  - Try out using k and r rather than a,b,c
    - If r is big, we don't need to test as many numbers.

10^2: 1035
10^3: 75019
10^4: 4225228

"""
