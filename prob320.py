"""
solve n/p+n/p^2 +... + n/p^k >= 1234567890 for all p < m for m in range 10 to SIZE...
or equivalently... n(1/p+1/p^2+1/p^3+...)
(1/p + 1/p^2 + 1/p^3 + ... ) = 1/(p-1)
so we can use n = val / (1/p + 1/p^2 + 1/p^3 + ... etc)
 ---> n = val / (1/(p-1) ) --> n = val * (p-1) + stuff to be 0 MOD p

okay, so that didn't work so i had to alter my original algorithm. Now I'm testing all primes less than n to see if they have the optimal solution. Obviously this is much slower than what we want since it requries a O(n/ln(n)) testing instead of a simple O(1) testing per number... and this testing doesn't come cheap...also it's not correct atm :D;; oops

raaaah @___@... I'll ask michikins to help me with this =D
"""
import time,math, sys
from bitarray import bitarray
start = time.time()


val = 1234567890
sumz = 0
MOD = 10**18
SIZE = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6

prime_set = set([2])
is_prime = bitarray('1'*(int(SIZE*1.1)))
for i in xrange(3,len(is_prime),2): #Dealing with evens later, generic sieve of Eratosthenes 
	if is_prime[i]:
		prime_set.add(i)
		for j in xrange(2*i,len(is_prime),i):
			is_prime[j]= False
for i in xrange(4,len(is_prime),2): #all multiples of 2 are prime
	is_prime[i] = False

prime_lst = list(prime_set)
prime_lst.sort()

index = 0
least_prime_sqrt = [0] * (SIZE+1)
lp_sq = [0] * (SIZE+1)
for i in xrange(len(least_prime_sqrt)):  #I slightly regret this implementation, but this gives you the largest prime < sqrt(n)
	if i**.5 >= prime_lst[index]:
		index+=1
	least_prime_sqrt[i] = index

print "Time Taken:", time.time()- start

def estimate(n,val,base): #Compute an upper bound for how big the number can be
	n /= base
	sumz = 0
	while n != 0:
		sumz +=n
		n/=base	
	expected = sumz * val

	return expected * (base-1) + base*20

def cfpn(n, val, base): #Compute For Power of Number 
	p = base
	sumz = 0
	comp = base
	while comp <= n:
		sumz += n/comp
		comp *= base
	expected = sumz * val

	valz = expected * (base-1) + (expected % base)  #This is the estimate of our answer, however it's not always right...

	val_check = sum([valz/base**i for i in xrange(1,int(math.log(valz,base)+1) ) ])  #checking to see how much we're off by...
	correction = valz + (expected - val_check) * (base-1)
	correction += (-1 * correction)%base	

	val_check2 = sum([correction/base**i for i in xrange(1,int(math.log(correction,base)+1) ) ]) #and a second check...

	if val_check2 == expected:
		return correction
	diff = val_check2 - expected

	while diff > 0: #Adjusting our value down, we got a power higher than needed
		if correction % (p**(diff+1)) == 0:
			return correction
		correction -= base
		val_check2 = sum([correction/base**i for i in xrange(1,int(math.log(correction,base)+1) ) ])
		diff = val_check2 - expected

	while diff < 0: #Adjusting our value up, we got a power lower than we need.
		correction += base
		val_check2 = sum([correction/base**i for i in xrange(1,int(math.log(correction,base)+1) ) ])
		diff = val_check2 - expected

	return correction


pset = prime_lst[:40]

loop_count = total_count = sumz = max_req = 0	
max_val = 2
for i in xrange(10,SIZE+1):
	if not is_prime[i]: #primes are a nice special case so we can do it elsewhere.
		plst = pset[:]
		for arg in xrange(1,int(i**(1/3.)) ):  # Figuring out the prime powers that we need to check.
			temp_val = i/arg #We need to check if the largest power comes from a multiple of the number
			if temp_val in prime_set and i%temp_val == 0: 
				plst.append(temp_val)

			a,b = prime_lst[least_prime_sqrt[temp_val] - 1], prime_lst[least_prime_sqrt[temp_val] - 2]
			if i%a == 0: plst.append(a)
			if i%b == 0: plst.append(b)


		for a in plst: #For every single potential prime that could give the largest power
			total_count +=1
			#shortcut compute some values so we don't have to do all of them.
			if estimate(i,val,a) < max_req: 
				continue #computations skipped :)

			temp = cfpn(i,val,a) #This function is more costly...
			loop_count +=1 #keeping track of how many times we actually need to do expensive computations
			if temp >= max_req:
				max_req = temp
				max_val = a
	else:
		max_val = i
		max_req = cfpn(i,val,i) #For primes p, we know that p is going to give the largest power that we need.
		total_count +=1
		loop_count +=1
	sumz= (sumz + max_req) % MOD #funny thing, I always forget to mod since I'm using python and I submit a 30 digit answer when they ask for 18 digits... :D;;
	if i%1024 == 0:
		print i

print sumz
print "Time Taken:", time.time()- start

print "damn, that was:", loop_count, "loops..."
print "total loop count was", total_count



"""
OKAY, so my notes for this problem before I forget. All those numbers below are the computations that I was keeping track of.

So first off, the problem wants you to find the smallest n such that (a!)^(1234567890)|n!. However, the only terms that really matter are one of the prime terms in 'a'. Thus, we only need to check the primes. Of course, of these primes, not all of them are relevant. As such, we want to limit our checking of irrelevant numbers. Originally, I was trying to only check ~40 numbers per 'a' (in contrast to checking all primes < a, which is a/log(a) of them), but when I realized that I only had to do this for 10^6, I broke out of this and started checking ~120 numbers per 'a', making it slower, but still a linear time algorithm...

'estimate' was my fast checker to see if a prime couldn't be a candidate for a solution, and i used cfpn to geck for prime numbers to find the smallest number N such that N! is a multiple of prime^large number.

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
Time Taken: 8.22241616249

278157919195482643

Congratulations, the answer you gave to problem 320 is correct.

You are the 432nd person to have solved this problem.

Time Taken: 86.4940459728
damn, that was: 421026 loops...
total loop count was 38692684


Haha... originally I was computing for 10^8... was taking my computer forever xP
"""

