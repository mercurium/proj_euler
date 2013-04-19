import time
start = time.time()
from bitarray import bitarray


def extended_gcd(a, b): #returns c,d such that ac+bd =1
  if b == 0:
    return (1, 0)
  else:
    q, r = a/b, a%b
    s, t = extended_gcd(b, r)
    return (t, s - q * t)
ext_gcd = extended_gcd


size = 10**7
tmp = bitarray('0'*size)
primes = set()
for i in xrange(3,size,2):
	if tmp[i] == 0:
		for j in xrange(i**2,size,2*i):
			tmp[j] = 1
		primes.add(i)
primes.remove(5)
prime_lst = sorted(list(primes))

sumz = 0

for prime in prime_lst:
	sumz += (extended_gcd(10,prime)[0])%prime
 
print sumz

print "Time Taken:", time.time() - start


"""

Let the number be of the form (10n+m). We want p|(n+am) if p|(10n+m). If 10a = 1 mod p, then (n+am)*10 = 10n+10am = 10n+m mod p. Thus we just need to find a mod p such that 10*a%p = 1

1601912348822
Time Taken: 5.88567185402

"""
