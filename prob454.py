import time
START = time.time()

SIZE = 1000

count = 0
for k in range(1,SIZE):
    n = int( (-k + (k**2+4*SIZE*k)**.5)/(2*k)) -1
    print k, n
    if n < 0:
        break
    count += n
print count




"""
pfactor = range(SIZE)
for i in xrange(4,SIZE,2):
    pfactor[i] = 2
for i in xrange(3,SIZE,2):
    if pfactor[i] == i:
        for j in xrange(i**2,SIZE,2*i):
            pfactor[j] = i

def factor(n):
    factors = []
    while n > 1:
        factors.append(pfactor[n])
        n /= pfactor[n]
    return sorted(factors)

count = 0
for num in xrange(2,SIZE/2):
    if pfactor[num] == num:
        if num * (num +1) < SIZE:
            count += 1
        continue

    factors = factor(num)
    factor_map = dict()
    for f in factors:
        if f not in factor_map:
            factor_map[f] = 3
        else:
            factor_map[f] +=2    

    numz = 1
    for f in factor_map.keys():
        numz *= factor_map[f]
    count += (numz-1)/2
    if num * (num +1) < SIZE:
        continue

    divisors = set([1])
    for f in factor_map.keys():
        new_divisors = set()
        for power in xrange(factor_map[f]):
            for x in divisors:
                new_divisors.add(x*f**power)
        divisors = new_divisors
    divisors = sorted(list(divisors))

    for i in divisors:
        if num*num / i <= SIZE - num:
            break
        if num*num % i == 0:
            count -=1


print count
print "Time Taken:", time.time() - START
"""

"""
(x-z)*(y-z) = z^2
x' * y' = z^2
x < y <= SIZE
2z < y' < SIZE-z



"""
