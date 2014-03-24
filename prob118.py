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

prime_lst = sorted(prime_sets)
print "Time Taken:", time.time() - START

def get_next(seen,max_size, last_seen):
    if max_size == 0 and len(seen) == 9:
        return 1
    elif max_size == 0:
        return 0
    sumz = 0
    for prime in prime_sets[max_size]:
        if prime > last_seen:  #Since we're not requiring that the num_digs goes down, we still need some ordering to avoid double counting.
            continue
        new_set = set(seen) 
        for dig in str(prime): new_set.add(dig) #Add all the new digits to the set 
        if len(new_set) == len(seen) + len(str(prime)): #If there's a repeat of digits, this will be false.
            sumz += get_next(new_set,min(max_size,9 - len(new_set)),prime)
    sumz += get_next(seen,max_size-1,last_seen) #In case we want to decrement the number of digits we're considering.
    return sumz
print "Answer is:", get_next(set(),8,9999999999) #999999999999 is an arbitrarily large number so that the next number will be smaller than it.

print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 118 is correct.

You are the 3110th person to have solved this problem.

~/Desktop/python_projects/proj_euler $python prob118.py 
Time Taken: 5.21821713448
Answer is: 44680
Time Taken: 10.939330101

Okay, so for this problem, what I did was I first generated all the primes with unique digits of length 1, length 2, 3, 4, etc. After this, I tried pairing up the primes with each other to see if they could make a set of 9 with no repeated digits.

We can do this by choosing to add each element or not to add it, and for each one that we add, we can't consider the other elements that have shared digits with it. After that, we sum up the number of ways we can do this problem and we get 44680 in 10.9 seconds on my laptop (est ~5 sec on desktop?), so not bad :)


"""
