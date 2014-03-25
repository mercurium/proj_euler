import time
from bitarray import bitarray
from math import *

START = time.time()
SIZE = 10**6

def extended_gcd(a, b): #returns c,d such that ac+bd =1
    if b == 0:
        return (1, 0)
    else:
        q, r = a/b, a%b
        s, t = extended_gcd(b, r)
        return (t, s - q * t)

def make_primes(size): #generates the list of primes < size
    lst = [0] * size
    primes = []
    for i in xrange(2,len(lst)):
        if lst[i] == 0:
            for n in xrange(i*2,len(lst),i):
                lst[n]+=1
            primes.append(i)
    return primes

def finder(a,b): #we're finding a mod b
    dig = 10**int(log(a,10)+1) %b
    c,d = extended_gcd(dig,b)
    ans = c*(-a) % b
    return int(str(ans)+str(a))


lst = make_primes(SIZE+1000)[2:]

print "Time taken:", time.time() - START
sumz = 0
for i in range(0,len(lst)):
    if lst[i] > SIZE:
        break
    sumz += finder(lst[i],lst[i+1])
print sumz

print "Time taken:", time.time() - START
