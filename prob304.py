import time
start = time.time()
from primes import m_r 

MOD = 1234567891011

#this takes a set of values and bases so that we can find x s.t.
#x = a1 MOD b1
#x = a2 MOD b2
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


def extended_gcd(a, b): #returns c,d such that ac+bd =1
    if b == 0:
        return (1, 0)
    else:
        q, r = a/b, a%b 
        s, t = extended_gcd(b, r)
        return (t, s - q * t)
ext_gcd = extended_gcd


#############################################################
##################### Getting 100,000 primes ################
#############################################################

i = 10**14
count = 0
prime_lst = []
while count < 10**5:
    i +=1
    if m_r(i):
        count +=1
        prime_lst.append(i)

print "Time Taken:", time.time() - start

#############################################################
##################  Finding the nth fibo num ################
#############################################################

pToTest = [3,7,13,67,107,630803] #Factorization of 1234567891011
fibo_lsts = []

for prime in pToTest:
    fib = [0,1,1,2]
    while fib[-1] != 1 or fib[-2] != 0:
        fib.append( (fib[-1] + fib[-2]) % prime)
    fibo_lsts.append(fib[:-2])

print "Time Taken:", time.time() - start

sumz = 0
for prime in prime_lst:
    vals = [ fibo_lsts[i][ prime % len(fibo_lsts[i]) ] for i in xrange(len(pToTest)) ] #Getting the values of the fibo numbers mod p for each prime.
    ans = crt(pToTest,vals) #Using the chinese remainder theorem to get a number < MOD such that all constraints are satisfied.
    sumz += ans

print sumz % MOD
print "Time Taken:", time.time() - start


"""
61548431626872586 is the answer I'm getting... it's apparently wrong? =/...
LOL oops, forgot to take the sum MOD 1234567891011... ehehehe... :x. But yeah, rest were solved :)
283988410192

Congratulations, the answer you gave to problem 304 is correct.

You are the 978th person to have solved this problem.

Okay, cool. So first off, I found 100,000 primes greater than 10^14. Very very thankful that I have my miller rabin primality checker here...
After that, I need to find the fibonnacci numbers, fibo[prime]. This would normally be hard, but an interesting thing to note is that since we're taking the answer mod <something not prime>, with relatively small prime factors, we can figure out what the prime would be mod p1, mod p2, mod p3, ...etc, and then use the chinese remainder theorem to tie them together. This saves a lot of computational time, so YAY ME... xD
"""
