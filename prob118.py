import time, string
START = time.time()
from itertools import permutations
from primes import mr


digits = [str(i) for i in range(1,10)] 

prime_sets = [set() for i in range(10)]
SIZE_LIM = 9

for num_dig in range(1,SIZE_LIM):
	for perm in permutations(digits,num_dig):
		next_num = int(string.join(perm,''))
		if mr(next_num):
			prime_sets[num_dig].add(next_num)
	print num_dig, len(prime_sets[num_dig])

print len(prime_sets) 
prime_lst = sorted(prime_sets)
print "Time Taken:", time.time() - START

def get_next(seen,max_size, last_seen):
	if max_size == 0 and len(seen) == 9:
		return 1
	elif max_size == 0:
		return 0
	sumz = 0
	for prime in prime_sets[max_size]:
		if prime > last_seen:
			continue
		new_set = set(seen)
		for dig in str(prime): new_set.add(dig)
		if len(new_set) == len(seen) + len(str(prime)):
			sumz += get_next(new_set,min(max_size,9 - len(new_set)),prime)
	sumz += get_next(seen,max_size-1,last_seen)
	return sumz
print "Answer is:", get_next(set(),8,9999999999)

print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 118 is correct.

You are the 3110th person to have solved this problem.

~/Desktop/python_projects/proj_euler $python prob118.py 
Time Taken: 5.21821713448
Answer is: 44680
Time Taken: 10.939330101
OA
"""
