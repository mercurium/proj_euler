import time
START = time.time()
from primes import factor, get_primes, primes
SIZE = 190


prime_list = get_primes(SIZE)
prod       = reduce(lambda x,y: x*y, prime_list)
PROD_LIM   = int(prod**.5)


vals   = set([1])
maxVal = 0
for p in prime_list:
    print p, maxVal, len(vals)
    for val in list(vals):
        if p * val > PROD_LIM:
            vals.remove(val)
            continue
        if p * val > maxVal:
            maxVal = p * val
        if p**2 * val < PROD_LIM:
            vals.add(p*val)



print len(vals), max(vals), maxVal

print "Time Taken:", time.time() - START
