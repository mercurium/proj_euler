import time
start = time.time()
from bitarray import bitarray
from math import factorial as fa

def extended_gcd(a, b): #returns c,d such that ac+bd =1
  if b == 0:
    return (1, 0)
  else:
    q, r = a/b, a%b
    s, t = extended_gcd(b, r)
    return (t, s - q * t)
ext_gcd = extended_gcd

 
def ncr(n,r):
	if debug2 and n != size: print n,r
	if r == 0: return 1
	if r*2 > n: r = n-r
	prod = 1
	for i in xrange(r):
		prod *=	(n-i)
	return prod/fa(r)

size = 5*10**3 
tmp = bitarray('110'+ '01'*(size/2-1))
num_mod = 10**9+7

for i in xrange(3,size,2):
	if tmp[i] == 0:
		for j in xrange(i**2,size,i):
			tmp[j] = 1



print "Time Taken:", time.time() - start


sumz = 0 
count = 0 #for keeping track of how many primes we've seen so far...
debug = False
debug2 = False 

stored = 1

for n in xrange(2,size+1):
	if n%1024==0: print n
	if tmp[n] == 0:
		count+=1
		stored = stored  * (n-1)/(count)
	else:
		
		stored = stored * 5 * (n-1) / (n-count-1)
		if n== 4: stored = stored/5
		if debug2: print n-1,count	
		
		sumz += stored
		if debug: print n, count, ncr(n-1,count), stored*6

#up to here works.... :/

print "Time Taken:", time.time() - start

if debug: print 'dabuhhh'

prod = 5**(n-1)
sumz+= prod
for k in xrange(1,count+1):
	prod = prod * (n-k+1)/(5*k)
	sumz += prod
	if debug: print k, n, prod*6

print (sumz*6)%num_mod
print "Time Taken:", time.time() - start
