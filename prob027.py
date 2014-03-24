from primes import mr, primes # miller_rabin method defined in primes.py, primes is a list of primes

import time
START = time.time()

a_lst = range(-1,-1000,-2)
b_lst = primes[12:168] 


a_lst2 = []
b_lst2 = []

maxz = 0
for a in a_lst:
    for b in b_lst:
        n = 1
        while True:
            if n**2 + n*a + b < 0: # We're no longer dealing with positive composite numbers
                break
            elif not mr(n): # Honestly, I don't remember why I had this condition...
                n+=1
            elif mr(n**2 + n*a + b): #If the result is a prime, keep going
                n+=1
            else: break
        if 40 < n: 
            maxz = n-1
            #print maxz, a, b
            a_lst2 += [a]
            b_lst2 += [b]

#print 'ON TO PHASE 2. YAY!'
maxz = 0
max_values = (0,0)
for i in range(0,len(a_lst2)):
    n = 1
    while n < 80: # We know 80 is the limit since the website said so.
        if mr(n**2 + n*a_lst2[i] + b_lst2[i]):
            n+=1
        else:
            break
    if maxz < n-1:
        maxz = n-1
        max_values = (a_lst2[i],b_lst2[i])
        print maxz, a_lst2[i], b_lst2[i]

print maxz, max_values[0] * max_values[1]
print "Time Taken:", time.time() - START


"""
we know that since n^2+an+b = prime has to include the 0 case
b has to be positive and prime. Also n has to be odd or else:
we get odd *odd + odd*even + odd = even = not prime

Time Taken: 9.46837615967
"""
