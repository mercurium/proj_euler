import time,math
from primes import get_primes

START = time.time()
SIZE  = 100

primes = get_primes(SIZE)
sumz   = 0
val    = [1]

for i in primes[::-1]:
  if i > SIZE / 2:
    val.append(i)
    continue
  val.append( i**int( math.log(SIZE,i)))

print len(val)
print sum(val)
print val

print "Time taken:", time.time() - START



"""
Co(10) = {1,5,7,8,9}
Co(30 = {1,11,13,17,19,23,25,27,28,29}

"""
