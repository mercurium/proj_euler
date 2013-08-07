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
size = 10**5

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

index = 0
least_prime = [0] * (size+1)
lp_sq = [0] * (size+1)
for i in range(len(least_prime)):
	if i**.5 >= prime_lst[index]:
		index+=1
	least_prime[i] = index

print "Time Taken:", time.time()- start

def estimate(n,val,base):
	n /= base
	sumz = 0
	while n != 0:
		sumz +=n
		n/=base	
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
	valz = expected * (base-1) + (expected % base)

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


pset = [2,3,5,7,11,13,17,19,23]

loop_count = 0	
lc = 0
bc = 0
sumz = 0
val2 = 0
maxz = 2
for i in xrange(10,size+1):
	if lst[i]:
		#processed_lst = pset[:]
		plst = pset[:]
		for arg in range(1,min(int(i**(1/3.) ), 20) ):
			temp_val = i/arg
			if temp_val in prime_set:
				plst.append(temp_val)
			#if int(temp_val**.5) in prime_set:
				#plst.append(int(temp_val**.5))
			plst.append(prime_lst[least_prime[temp_val]-1])
			plst.append(prime_lst[least_prime[temp_val]-2])

		#plst.append(prime_lst[least_prime[i]]) #least_prime is the smallest prime that is greater than i^(1/2)
		#plst.append(prime_lst[least_prime[i]-1]) #this is the largest prime bigger than i^(i/2)
		plst.append(maxz)


		#for j in xrange(0,len(prime_lst)):
		for j in xrange(len(plst)):
			lc +=1
			#a = prime_lst[j] 
			a = plst[j]  	#get rid of plst and replace with prime_lst to get exact ans
			if a > i/2:
				bc +=1
				break
			if i%a > 20:
				 continue
			if estimate(i,val,a) < val2:
				continue

			temp = cfpn(i,val,a)
			loop_count +=1
			if temp >= val2:
				val2 = temp
				maxz = a
	else:
		maxz = i
		val2 = cfpn(i,val,i)
		lc+=1
		loop_count +=1
	if lst[i] and maxz not in plst: #maxz > 13 and i/maxz > 13 and maxz != int(i**.5): 
		print maxz, i, i/maxz
	sumz+= val2

print sumz
print "Time Taken:", time.time()- start

print "damn, that was:", loop_count, "loops..."
print "total loop count was", lc
print "but we managed to break out of...", bc, "loops"
"""
614538266565663 is the right answer, for 10^3

My current fastest answer is:
Time Taken: 0.0379350185394

Stats on 10^4:
61690942682501005 CORRECT ANSWER   Time Taken: 1.33670401573
61690276015610065 Time Taken: 0.195645093918
61690035275036446 (my approximations)
61688283422307148
61683361197356786
Time Taken: 1.33670401573
damn, that was: 9149 loops...
total loop count was 3190078

"""
