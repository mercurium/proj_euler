import time
START = time.time()

def tri(n): return n*(n+1)/2

sumz = 0
for a in xrange(2,16):
    prod = 1
    prod = (a*1./tri(a))**tri(a)
    for i in xrange(1,a+1):
        prod *= pow(i,i)
    print int(prod)
    sumz += int(prod)

print sumz

print "Time Taken:", time.time() - START
