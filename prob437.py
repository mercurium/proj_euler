from bitarray import bitarray
import time,random,math
START = time.time()

SIZE = 10**8


def get_totient(size):  #gives you the totients of all numbers i <= size
    lst = range(size+1)
    lst[0] = 1
    for i in xrange(2,len(lst)):
        if lst[i] == i:
            for j in xrange(i,len(lst),i):
                lst[j] = (lst[j] * (i-1))/i 
    return lst
totient = get_totient(SIZE)
print "totients found!", time.time() - START

def pfactor_gen(size): #for each number n, return some factor of it.
    stuff = [0,1,2] + [1,2] *(size/2-1)
    for i in xrange(3,size,2):
        if stuff[i] == 1:
            for j in xrange(i**2,size,i*2):
                stuff[j] = i
            stuff[i] = i
    return stuff
pfactor = pfactor_gen(SIZE)
print "pfactors found!", time.time() - START

def factor(n): #simple factoring method, put one of the factors of n onto the list until we run out of factors
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

sumz = 5
count = 1
for p in xrange(7,SIZE):
    if p% 1024 == 0: #counter to see how far the program is.
        print p, count, sumz
    if pfactor[p] != p: #it's not prime, ignore it.
        continue
    if p % 10 != 1 and p% 10 != 9 and p != 5: #x^2 = 5 mod p does not have a solution
        continue
    
    if p%4 == 3:
        num = pow(5,(p+1)/4,p)
        ab = ( (num+1)*(p+1)/2 % p), ((1 - num)*(p+1)/2) % p 
    else:
        num = cipolla(p)
        ab = ( (num+1)*(p+1)/2 % p), ((1 - num)*(p+1)/2) % p 


    for a in ab:
        tot = totient[p]
        factor1 = pfactor[tot]
        while tot % factor1 == 0:
            tot /= factor1

        while pfactor[tot] != 1:
            if pow(a,totient[p]/factor1,p) != 1:
                factor1 = pfactor[tot]
                while tot % factor1 == 0:
                    tot /= factor1
            else:
                break #this number doesn't satisfy our conditions
        if pow(a,totient[p]/factor1,p) != 1: #a bit excessive, but a safeguard
            sumz +=p
            count +=1
            break




print 
print "total sum:", sumz
print "total number of primes for which this works:", count
print "Time taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 437 is correct.

You are the 89th person to have solved this problem.

total sum: 74204709657207
total number of primes for which this works: 1531317
Time taken: 281.228798866


On the plus side, I only need to check two numbers to see if they're primitive roots...
the solutions to n^2 - n - 1 = 0 mod p.

If x is a solution to n^2 - n - 1 = 0 mod p, then so is (p-x+1)...



omg, the notes for this one are going to be so long LOL... (except I'm kind of lazy so they're not :D:;; )

So first off, I want to find out if a primitive root has the property r^n + r^{n+1} = r^{n+2} mod p.
This is simple to check, we just need r^2 = r + 1. However, it's hard to check all primitive roots for this property, hard to get them all, and we really only need to check if a number is a primitive root if it satisfies this condition.

So... first off, how to check if a number is a primitive root. We know that a number is a primitive root if r^k != 1 mod p for all 1 <= k < p -1. The only times we can have a^k = 1 mod p is if k|(p-1), nifty rule due to congruence rings,etc. So I only need to check the factors of p-1, and see if r^{(p-1)/f} = 1 mod p, to see if it's a primitive root.

Beyond that, finding the solutions for x^2 = 5 mod p was kind of hard... THANKFULLY.... I discovered http://en.wikipedia.org/wiki/Quadratic_residue#Complexity_of_finding_square_roots and http://en.wikipedia.org/wiki/Cipolla%27s_algorithm

So if p%4 = 3, then x^2 = 5 = (5^(1/2))^2 = (5^(1/2))^(p+1) = 5^((p+1)/2) => x = 5^((p+1)/4). Since we know that p = 3 mod 4, p+1 = 0 mod 4, and so we can find 5^((p+1)/4).

If we don't have p%4 = 3, then we have to deal with some more annoying things to get it to work. Using cipolla's algorithm, we can compute it. However, to do that, we need to find a repeated square of an irrational number, which repeated squaring built into python doesn't do for us. So I wrote my own method for this. Also, to get this to work, we need a nonquadratic residue, which can be computed using legendre symbols ( http://en.wikipedia.org/wiki/Legendre_symbol ).

After that, it was just plugging it in and making sure all the code fit together... hehe...

Darn it, I could have been much faster xD. I saw this at 10 pm, then went to sleep at 1 am, got up at 9 am, finished ~1 pm, so I actually took 7 hours, not 23 =(... would have been like... 43rd LOL


"""
