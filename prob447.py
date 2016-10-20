import time
from primes import m_r, pfactor_gen, factor_given_pfactor, ext_gcd
START = time.time()
SIZE  = 10**7
MOD   = 10**9 +7

pfactor = pfactor_gen(SIZE)

def factor(n):
  return factor_given_pfactor(n, pfactor)

def addToDict(valDict, key, value):
  if key in valDict:
    valDict[key] += value
  else:
    valDict[key] = value

count   = 0

for n in xrange(2,SIZE+1):
  prod    = 1
  changes = dict()

  # Add on the factors from the top
  for f in factor(n):
    addToDict(changes, f, 1)

  for f in changes.keys():
    prod = (1 + pow(f, changes[f], MOD)) * prod % MOD

  count = (count + prod) % MOD

  # Progress counter
  #if n% 1024 == 0:
  #  print n, time.time() - START

count = (count + 1 - (SIZE * (SIZE+1)/2)) % MOD

print "Answer is:", count
print "Time Taken:", time.time() - START

