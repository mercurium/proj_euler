import time
start = time.time()
from bitarray import bitarray

def primes_less_than(n):
        tmp = bitarray('0' * (n+1))
        prime_lst = [2]
        for i in xrange(3,n+1,2):
                if tmp[i] == 0:
                        prime_lst.append(i)
                        for j in xrange(i**2,n+1,2*i):
                                tmp[j] = 1
        return tmp

size = 10**6
prime_lst = primes_less_than(size)

count = 0
sumz = 0
for i in xrange(3,size,2):
	if i%5 != 0 and prime_lst[i] != 0 and i%3 != 0:
		if pow(10,i-1,i) == 1:
			count += 1
			print i, count
			sumz +=  i 
	if count == 25:
		break

print sumz, count
print "Time Taken:", time.time()-start

"""
I noticed that:

a^k == 1 (mod p) <--> sum(10^n for n in range(k)) == 0 (mod p)
Somehow this also holds for composite numbers that are not multiples of 2,3, or 5. It's obvious why this is true for 2 and 5, since the moding would be interefered with since gcd(10,2) and gcd(10,5) != 1. However, I don't know why this works if you don't use multiples of 3... AHA. I got it. Since 10 % 3 == 1, and using CRT, we get that it repeats every 3 steps, and the other number repeats every phi(n) steps... oO


149253 25
Time Taken: 0.292575836182
"""
