#NOTE TODO need to solve it

import time
START = time.time()
from primes import factor, is_prime

MAX_SIZE = 71
num_iter = 0

numToExclude = [17,19,23,25,29,31,34,37,38,41,43,46,47,49,50,51,53,57,58,59,61,62,67,68,69,71,73,74,75,76,79]

inverse = [0,0] + [1./x**2 for x in range(2,MAX_SIZE+1)]

# This value is useful for figuring out how much more we could possibly add.
partial_sums = [inverse[-1]]
for i in xrange(MAX_SIZE):
    partial_sums.append(partial_sums[-1] + inverse[MAX_SIZE-i-1])
partial_sums = partial_sums[::-1]

print [round(x,3) for x in partial_sums]

nums = [1,1,1] + [( 1 if (factor(n)[-1] > 7) else 0) for n in xrange(3,MAX_SIZE)]

cache = {}
def recurse(n,num,denom):
    # Personal counter variable so I know how inefficient my code is.
    global num_iter
    if num_iter % (2**18) == 0:
        print num_iter, n
    num_iter +=1

    # If numerator is too big, we've exceeded the limit,
    # or the numerator will be too small, return
    if num*2 > denom or n > MAX_SIZE or num*1./denom + partial_sums[n] < .4999999:
        return 0
    if num * 2 == denom:
        print int(denom**.5), factor(int(denom**.5)), n-1
        return 1
    while n < MAX_SIZE and n*3 > MAX_SIZE and nums[n] == 1:
        n+=1
    if n > MAX_SIZE:
        return 0
    if (n in numToExclude):
      b = 0
    else:
      b = recurse(n+1,num*n**2+denom, denom* n**2)
    a = recurse(n+1,num,denom)
    return a+b

# If we exclude 1/4, 1/9, or 1/16, the result won't be big enough.
numer = 4*9 + 4*16 + 9*16
denom = 4*9*16

print recurse(5,numer,denom), num_iter
print "Time Taken:", time.time() - START

"""
17 using 60 or less
56 using 70


"""


