import time
START = time.time()
SIZE = 9

primes = [2]
tempLst = range(10**4+1)
for i in range(3, len(tempLst), 2):
    if tempLst[i] == i:
        primes.append(i)
        for j in range(i**2, len(tempLst), 2*i):
            tempLst[j] = 0


def getNumDivisors(n):
    prod = 1
    for p in primes:
        pProd = 1
        if p*p > n:
            break
        while n % p == 0:
            pProd += 1
            n /= p
        prod *= pProd
    if n != 1:
        prod *= 2
    return prod



count = 0
for size in range(1,SIZE+1):
    for a in xrange(0, size+1):
        for b in xrange(0, size+1):
            n = 2**a * 5**b
            modNum = 10**size * (2**a + 5**b) / n
            count += getNumDivisors(modNum)
    
    for a in xrange(1, size+1):
        for b in xrange(1, size+1):
            n = 2**a * 5**b
            modNum = 10**size * (1+n) / n
            count += getNumDivisors(modNum)

print count
print "Time Taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 157 is correct.

You are the 1451st person to have solved this problem.

Answer = 53490
Time Taken: 0.0065701007843

All solutions satisfying the conditions are of the form:

1/ak + 1/bk = (a+b)/(abk) =  m/10^n,

where a = 2^i
      b = 5^j
      k | (10^n / ab) * (a+b)      
OR

1/k + 1/(ck) = (c+1)/ck = m/10^n
where c = 2^i * 5^j
      k | (n+1) * (10^n / c)

After getting to this form, I just needed to count how many possible k values this works for, and then the answer came out. 

"""
