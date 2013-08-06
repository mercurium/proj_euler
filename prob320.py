"""
solve n/p+n/p^2 +... + n/p^k >= 1234567890 for all p < m for m in range 10 to size...
or equivalently... n(1/p+1/p^2+1/p^3+...)
(1/p + 1/p^2 + 1/p^3 + ... ) = 1/(p-1)
so we can use n = val / (1/p + 1/p^2 + 1/p^3 + ... etc)
 ---> n = val / (1/(p-1) ) --> n = val * (p-1) + stuff to be 0 mod p

okay, so that didn't work so i had to alter my original algorithm. Now I'm testing all primes less than n to see if they have the optimal solution. Obviously this is much slower than what we want since it requries a O(n/ln(n)) testing instead of a simple O(1) testing per number... and this testing doesn't come cheap...also it's not correct atm :D;; oops

raaaah @___@... I'll ask michikins to help me with this =D
"""
import time
#from bitarray import bitarray
start = time.time()
from math import *

val = 1234567890
sumz = 0
size = 10**3


prime_set = set([2])
#lst = bitarray('0'*(int(size*1.1)))
lst = [0]*int(size*1.3)
for i in xrange(3,len(lst),2):
	if lst[i] == 0:
		prime_set.add(i)
		for j in range(2*i,len(lst),i):
			lst[j]= 1
for i in xrange(2,len(lst),2):
	lst[i] = 1

prime_lst = list(prime_set)
prime_lst.sort()

print "Time Taken:", time.time()- start

def estimate(n,val,base):
	sumz = 0
	comp = base
	while comp <= n:
		sumz += n/comp
		comp *= base
	expected = sumz * val

	return expected * (base-1) + base*20

def cfpn(n, val, base): #compute for power of random base
	p = base
	sumz = 0
	comp = base
	while comp <= n:
		sumz += n/comp
		comp *= base
	expected = sumz * val

#	print sumz, val, base-1
	valz = expected * (base-1) + (expected % base) # not (sumz * val * -1) because (base-1) = -1 mod base

	############################################
	val_check = sum([valz/base**i for i in xrange(1,int(log(valz,base)+1) ) ])
	correction = valz + (expected - val_check) * (base-1)
	correction += (-1 * correction)%base	

	val_check2 = sum([correction/base**i for i in xrange(1,int(log(correction,base)+1) ) ])

	if val_check2 == expected:
		return correction
	diff = val_check2 - expected

	while diff > 0:
		if correction % (p**(diff+1)) == 0:
			return correction
		correction -= base
		val_check2 = sum([correction/base**i for i in xrange(1,int(log(correction,base)+1) ) ])
		diff = val_check2 - expected

	while diff < 0:
		correction += base
		val_check2 = sum([correction/base**i for i in xrange(1,int(log(correction,base)+1) ) ])
		diff = val_check2 - expected

	return correction

loop_count = 0	
sumz = 0
for i in xrange(10,size+1):
	val2 = 0
	maxz = 0
	if lst[i]:
		for j in xrange(0,len(prime_lst)):
			a = prime_lst[j]
			if a > i: break
			if i%a > 20: continue
			if estimate(i,val,a) < val2:
				continue
			temp = cfpn(i,val,a)
			loop_count +=1
			if temp > val2:
				val2 = temp
				maxz = a
	else:
		maxz = i
		val2 = cfpn(i,val,i)
		loop_count +=1
	#print maxz, i
	sumz+= val2

print sumz
print "Time Taken:", time.time()- start

print "damn, that was:", loop_count, "loops..."

"""
614538266565663 is the right answer,
614538266179707 is mine... =/
"""
