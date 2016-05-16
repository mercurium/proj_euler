import string
import math

#methods in file: is_prime(num), factor(val), totient(n), repeated_squaring(n,pow,mod), reverse_num(n), mergesort(list), gcd(a,b), ncr(n,r)

# While not all of these methods are as optimial as they should be, this is a sort of file for me to keep my old algorithms that I wrote at one point in case I would like to use a variant later.
# Afte all, it's much easier to modify code that's already there (this only holds for my own code) than dealing with off by one errors with a new algorithm :)

temp = open('primenum.txt','r')
primes = [int(i) for i in string.split(temp.read()[:-2],', ')]
del primes[primes.index(9999)]
primes_set = set(primes)


temp = open('primenum10000.txt','r')
primes_few = [int(i) for i in string.split(temp.read(),',')]

def factor(val): #dumb factoring method, use the other one instead...
    if mr(val):
        return [val]
    factors = []
    for x in primes_few:
        if x > val:
            break
        while val % x == 0:
            factors.append(x)
            val /= x
            if val == 0:
                print "BIG FAT ERROR!!!"
    for x in xrange(primes_few[-1], int(math.sqrt(val)+1)):
        while val % x == 0:
            factors.append(x)
            val /= x
    if val != 1:
        factors.append(val)
    return factors

def totient(n): #dumb version, don't use this...
    lst = factor(n)
    result = lst[0] - 1
    for i in xrange(1,len(lst)):
        if lst[i] != lst[i-1]:
            result = result * (lst[i]-1)
        else:
            result = result * lst[i]
    return int(result)


def get_totient(size):  #gives you the totients of all numbers i <= size
    lst = range(size+1)
    lst[0] = 1
    for i in xrange(2,len(lst)):
        if lst[i] == i:
            for j in xrange(i,len(lst),i):
                lst[j] = (lst[j] * (i-1))/i
    return lst

def get_primes(size):  #gives you the totients of all numbers i <= size
    lst = [1] * (size+1)
    primes = [2]
    for i in xrange(3,len(lst), 2):
        if lst[i] == 1:
            primes.append(i)
            for j in xrange(i**2,len(lst),2 * i):
                lst[j] = 0
    return primes

def pfactor_gen(size): #for each number n, return some factor of it.
    stuff = [0,1,2] + [1,2] *(size/2-1)
    for i in xrange(3,size,2):
        if stuff[i] == 1:
            for j in xrange(i**2,size,i*2):
                stuff[j] = i
            stuff[i] = i
    return stuff


def factor_given_pfactor(n): #simple factoring method, put one of the factors of n onto the list until we run out of factors
    if n == 1:
        return []
    if pfactor[n] == n:
        return [n]
    factors = []
    while pfactor[n] != 1:
        factors.append(pfactor[n])
        n /= pfactor[n]
    return factors


def legendre(a,p): # http://en.wikipedia.org/wiki/Legendre_symbol
    if a <= 1:
        return 1
    if a == 2:
        if (p**2 -1)% 16 == 0:
            return 1
        return  -1
    factors = factor(a)
    product = 1
    for f in factors:
        if f == 2:
            if (p**2 -1) % 16 != 0:
                product *= -1
        else:
            product *= legendre(p%f,f) * pow(-1,(f-1)*(p-1)/4)
    return product
lg = legendre


def cipolla(p): # http://en.wikipedia.org/wiki/Cipolla%27s_algorithm
    n = 5
    a = random.randint(int(p**.5)+1,p-1)
    while legendre((a**2-n)%p,p) == 1:
        a = random.randint(int(p**.5)+1,p-1)
    val = rep_sq_sqrt((a,1,(a**2-n)%p), (p+1)/2, p)
    return val[0]


def rep_sq_sqrt(n, powz, mod): #NOTE, n is a tuple... a,b,c so that we had a + b * sqrt(c)
    def mult(a,b,mod): #multiplying numbers which share a square root (sqrt)
        full = a[0] * b[0] + a[1] * b[1] * a[2]
        frac = a[1] * b[0] + a[0] * b[1]
        return (full%mod,frac%mod,a[2])
    if powz == 0: return 1
    if powz == 1: return (n[0] % mod,n[1] % mod, n[2])

    val = int(math.log(powz,2))
    lst = [1,n] + [0] * val
    for i in range(2,len(lst)):
        lst[i] = mult(lst[i-1],lst[i-1],mod)

    pows = [0] * (val+1)
    power = powz
    for i in range(0,len(pows)):
        pows[i] = power % 2
        power = power //2
    product = (1,0,n[2])
    for i in range(0,len(pows)):
        if pows[i] == 1:
            product = mult(product,lst[i+1], mod)
    return product

def extended_gcd(a, b): #returns c,d such that ac+bd =1
	if b == 0:
		return (1, 0)
	else:
		q, r = a/b, a%b
		s, t = extended_gcd(b, r)
		return (t, s - q * t)
ext_gcd = extended_gcd

#this takes a set of values and bases so that we can find x s.t.
#x = a1 mod b1
#x = a2 mod b2
#... and so on for any number of bases

def crt(bases, vals):
    big_base = 1
    sumz = 0
    for val in bases: big_base *= val
    for i in range(0,len(bases)):
        curr_base = big_base / bases[i]
        inverse = ext_gcd(bases[i],curr_base)[1]
        sumz += vals[i] * curr_base * inverse
    return sumz % big_base


#http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def miller_rabin(n):
    if n == 1: return False
    if n in primes_set: return True #doesn't work for n < 3

    for i in range(0,100): #save us some excessive calculations
        if n%primes[i] == 0:
            return False

    d,r = n-1, 0
    while d %2 == 0:
        r+=1
        d/= 2 #We'll have n-1 = 2^r * d


    if n >= 3825123056546413051: return -1 #too large of an input for us
    if n < 1373653: lstz = [2,3]
    elif n < 9080191: lstz = [31,73]
    elif n < 4759123141: lstz = [2,7,61]
    elif n < 2152302898747: lstz = [2,3,5,7,11]
    elif n < 3474749660383: lstz = [2,3,5,7,11,13]
    elif n < 341550071728321:    lstz = [2,3,5,7,11,13,17]
    elif n < 3825123056546413051: lstz = [2,3,5,7,11,13,17,19,23]

    def try_composite(a):
        val = pow(a,d,n)
        if val == 1:
            return False
        for i in range(r):
            if val == n-1:
                return False
            val = pow(val,2,n)
        return True # n is definitely composite

    for a in lstz:
        if try_composite(a):
            return False

    return True

mr = m_r = miller_rabin

def is_prime(n):
    return mr(n)

def rep_sq(n, powz, mod):
    if powz == 0: return 1
    if powz == 1: return n % mod

    val = int(math.log(powz,2))
    lst = [1,n] + [0] * val
    for i in range(2,len(lst)):
        lst[i] = lst[i-1]**2 % mod

    pows = [0] * (val+1)
    power = powz
    for i in range(0,len(pows)):
        pows[i] = power % 2
        power = power //2
    product = 1
    for i in range(0,len(pows)):
        if pows[i] == 1:
            product = product * lst[i+1] % mod
    return product


def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    num = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return num//denom

