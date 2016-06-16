import time
from primes import get_primes, get_divisors_given_pfactor, pfactor_gen
START = time.time()
SIZE  = 10**4

fibo = [1,1,2,3]
for i in xrange(SIZE):
  fibo.append(fibo[-1] + fibo[-2])

primes  = get_primes(SIZE)
pfactor = pfactor_gen(SIZE)

def divisors(n):
  return get_divisors_given_pfactor(n, pfactor)

def addToDict(valDict, key):
  if key in valDict:
    valDict[key] += 1
  else:
    valDict[key] = 1

#count = 0
#valDict = dict()
#for index in xrange(SIZE):
#  if not any([ fibo[index] % p**2 == 0 for p in primes]):
#    count +=1

#print fibo[index]
#print valDict

for p in primes:
  for div in sorted(divisors(p-1) + divisors(p+1)):
    if fibo[div-1] % p == 0:
      print p, div-1
      break

print "Time Taken:", time.time() - START
