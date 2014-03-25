import time
START = time.time()

def gcd(a,b):
    while a!= 0:
        a,b = b%a,a
    return b

count = 0
for d in xrange(5,12001):
    for n in xrange(d/3 +1, d/2+1):
        if gcd(d,n) ==1:
            count +=1
print count
print "Time Taken:", time.time() - START

"""
Simple brute force iteration through all i = 5 to i = 12,000, and taking numerators where 1/3 < d/n < 1/2


"""
