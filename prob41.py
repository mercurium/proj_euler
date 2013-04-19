from primes import *
import time
from itertools import permutations
import string


start = time.time()
lst = permutations(['1','2','3','4','5','6','7'],7)
max = 0
for item in lst:
  n = int(string.join(item, ''))
  if n > max and is_prime(n):
    max = n
print max

print "Time taken: " + str(time.time() -start)
