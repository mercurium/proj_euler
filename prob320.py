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
import sys


val = 1234567890
sumz = 0

if len(sys.argv) > 1:
	size = int(sys.argv[1])
else:
	size = 10**4

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

loop_count = lc = sumz = max_req = 0	
max_val = 2
for i in xrange(10,size+1):
	if lst[i]:
		#processed_lst = pset[:]
		plst = pset[:]
		for arg in range(1,min(int(i**(1/3.) ), 20) ):
			temp_val = i/arg
			if temp_val in prime_set and i%temp_val == 0:
				plst.append(temp_val)


			a,b = prime_lst[least_prime[temp_val] - 1], prime_lst[least_prime[temp_val] - 2]
			if i%a == 0:
				plst.append(a)
			if i%b == 0:
				plst.append(b)

		#for j in xrange(0,len(prime_lst)):
		for j in xrange(len(plst)):
			lc +=1
		#	a = prime_lst[j] 
			a = plst[j]  	#get rid of plst and replace with prime_lst to get exact ans

			if estimate(i,val,a) < max_req: #shortcut compute some values so we don't have to do all of them.
				continue

			temp = cfpn(i,val,a)
			loop_count +=1
			if temp >= max_req:
				max_req = temp
				max_val = a
	else:
		max_val = i
		max_req = cfpn(i,val,i)
		lc+=1
		loop_count +=1
	#if lst[i] and max_val not in plst: #max_val > 13 and i/max_val > 13 and max_val != int(i**.5): 
	#	print max_val, i, i/max_val
	sumz+= max_req

print sumz
print "Time Taken:", time.time()- start

print "damn, that was:", loop_count, "loops..."
print "total loop count was", lc



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

Stats on 10^5: (on mac) it's now linear <3
[tw-mbp13-jerrychen proj_euler (prob320)]$ python prob320.py 100000
Time Taken: 0.150601148605
6172360352621332245
Time Taken: 7.22241616249
"""
