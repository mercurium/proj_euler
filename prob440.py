import time
START = time.time()
from primes import m_r

def gcd(a,b):
    while a != 0:
        a,b = b%a, a
    return b

def pollard_rho(n):
    def func(x):
        return (x**2+1)%n
    def func2(x):
        return (x**2+3)%n
    x,y = 2,2
    d = 1
    while d==1: 
        x = func(x)
        y = func(func(y))
        d = gcd(abs(x-y),n)
    
    if d==n:
        d=1
        while d==1:
            x = func2(x)
            y = func2(func2(y))
            d = gcd(abs(x-y),n)
    return d

small_primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,113,127,131,137,139,149,151,157,163,167,173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]


def factor(n):
    if m_r(n):
        return [n]
    factor_lst = []
    for i in small_primes:
        while n % i == 0:
            factor_lst.append(i)
            n /= i
    while n != 1:
        if m_r(n):
            return (factor_lst + [n])
        d = pollard_rho(n)
        while n % d == 0:
            factor_lst.append(d)
            n /= d
    return factor_lst


T = [1,10]
for i in range(31):
    T.append(T[-1] * 10 + T[-2])

sumz = 0
for a in range(1,4):
    for b in range(1,4):
        for c in range(1,4):
            sumz += gcd(T[c**a], T[c**b])
print sumz

print "Time Taken:", time.time() - START
