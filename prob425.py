import time, Queue
START = time.time()
SIZE = 10**7

prime_lst = [2]
is_prime = ([0,0,1] + [1,0]*(SIZE//2 -1))[:SIZE+1]

for i in xrange(3,SIZE+1,2):
	if is_prime[i]:
		for j in xrange(i**2,SIZE+1,2*i):
			is_prime[j] = False
		prime_lst.append(i)
prime_set = set(prime_lst)

relatives = {2,3,5,7}  #Our set of answers
reachable = {2:2,3:3,5:5,7:7}
reach_lst = Queue.PriorityQueue(len(prime_set)) #All the primes that we're iterating over

reach_lst.put(2) #Putting all 1 digit primes on the queue first, since we're incrementing up.
reach_lst.put(3)
reach_lst.put(5)
reach_lst.put(7)

while not reach_lst.empty(): 
	next_prime= reach_lst.get() 
	for digit in xrange(0,len(str(next_prime) ) + 1):
		# Zeroing out one of the digits of the prime.
		num2 = (next_prime/ (10 ** (digit + 1)) ) * 10 ** (digit + 1) + next_prime% (10 ** digit)

		for next_test_num in xrange(num2,num2+10**(digit+1), 10**digit):
			if next_test_num in prime_set and next_test_num not in relatives: # Forget it if it's not a prime (or too big), and if we've already seen it, skip it.

				if next_test_num not in reachable:  # If we didn't see it before...
					if next_test_num > reachable[next_prime]:  # If the next_test_number is bigger than all other primes in the chain...
						relatives.add(next_test_num) #It's a relative of 2!
						reachable[next_test_num] = next_test_num #We'll put it down as largest in the chain to use it.
					else:
						reachable[next_test_num] = reachable[next_prime]
					reach_lst.put(next_test_num) #Add it to our queue of numbers to check.


print sum(prime_lst) - sum(relatives)
print "Time Taken:", time.time() - START

"""
09:47 ~/Desktop/python_projects/proj_euler $ python prob425.py 
46479497324
Time Taken: 29.9781889915


Okay, very short summary of how this method works. We make a priority queue of numbers, removing them off the queue one at a time, and checking all the numbers that are one digit off from it. At each point, we record the largest number that it took to get to a prime in reachable. reachable[p] gives you the largest number from 2 to p that was required to get to p. So at each point, popping off new primes, we check if we can get to it without going over the limit, and if we can, then it's a relative.

We end with subtracting the set of all primes < SIZE from the relatives of 2, which gives us the answer in ~30 seconds =P. Looks pretty linear to me~
"""
