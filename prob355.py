import time,math
START = time.time()
from primes import *
SIZE = 30

sumz = 0
val = [1]
for i in primes:
    if i> SIZE:
        break
    val.append( (  i,i**int( math.log(SIZE,i) )  ))

print len(val)




"""
Co(10) = {1,5,7,8,9}
Co(30 = {1,11,13,17,19,23,25,27,28,29}

"""
