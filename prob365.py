#NOTE TODO need to solve it
import time
START = time.time()
from primes import m_r 

#this takes a set of values and bases so that we can find x s.t.
#x = a1 MOD b1
#x = a2 MOD b2
#... and so on for any number of bases

BIG = 10**18
SMALL = 10**9

def crt(bases, vals):    
    big_base = 1 
    sumz = 0 
    for base in bases: big_base *= base 
    for i in range(0,len(bases)):
        curr_base = big_base / bases[i]
        inverse = ext_gcd(bases[i],curr_base)[1]
        sumz += vals[i] * curr_base * inverse
    return sumz % big_base

def mod_count(n,mod):
    return sum([ n/mod**x for x in xrange(1,10)])

def factorial(n,mod):
    prod = 1
    n = n%mod
    for i in xrange(2,n+1):
        prod = (prod * i) % mod
    return prod


def extended_gcd(a, b): #returns c,d such that ac+bd =1
    if b == 0:
        return (1, 0)
    else:
        q, r = a/b, a%b 
        s, t = extended_gcd(b, r)
        return (t, s - q * t)
ext_gcd = extended_gcd

def inverted_fa(n,mod):
    return ext_gcd(factorial(n,mod),mod)[0]

def get_primes(start,end):
    primes = []
    for i in xrange(start,end):
        if m_r(i):
            primes.append(i)
    return primes

prime_nums = get_primes(1000,5000)

mod_vals = [0] * len(prime_nums)
for i in xrange(len(prime_nums)):
    if mod_count(BIG,prime_nums[i]) - mod_count(SMALL,prime_nums[i]) - mod_count(BIG-SMALL,prime_nums[i]) > 0:
        mod_vals[i] = 0
    else:
        mod_vals[i] = factorial(BIG,prime_nums[i]) * inverted_fa(SMALL,prime_nums[i]) * inverted_fa(BIG-SMALL,prime_nums[i])

num_mod_all = crt(prime_nums,mod_vals)

sumz = 0
for p1 in xrange(len(prime_nums)):
    for p2 in xrange(p1):
        for p3 in xrange(p2):
            sumz = (sumz + (num_mod_all % (prime_nums[p1] * prime_nums[p2] * prime_nums[p3])))
    print p1, sumz

print "The answer is:", sumz
print "Time taken:", time.time() - START


"""
Getting 162590298313536289... it's a bit off... o.O


"""
