import time

START = time.time()
SIZE = 10**6+1

totients = range(0,SIZE)
for i in xrange(2,len(totients)):
    if i == totients[i]:
        for j in xrange(i,len(totients),i):
            totients[j] *= (i-1.)/i

sumz = sum([int(x) for x in totients[2:]])

print "The answer is:", sumz
print "Time Taken:", time.time() - START

"""
The main trick to this problem is that the only numbers n that can be put over a denominator d are those where gcd(d,n) = 1. This means that there are totient(d) numbers that can be above it in a fraction, so we can use this fact to compute it haha.

~/proj_euler $python prob072.py 
The answer is: 303963552391
Time Taken: 1.56138300896


"""
