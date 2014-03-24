from primes import *
import time
START = time.time()
SIZE = 150000 # Arbitrary, would have increased if I didn't get an answer.

num_prime_factors = [0] * SIZE 
for i in xrange(2,SIZE):
    if num_prime_factors[i] == 0:
        for n in xrange(i*2,len(num_prime_factors),i):
            num_prime_factors[n]+=1

print "Time taken for first step:",time.time() -START

for i in xrange(0,SIZE - 4):
    if num_prime_factors[i:i+4] == [4,4,4,4]:
        print "The answer is:", i
        break
print "Time taken:",time.time() -START

"""
12:28 ~/Desktop/python_projects/proj_euler $ python prob47.py
Time taken for first step: 0.059818983078
The answer is: 134043
Time taken: 0.0975661277771

"""
