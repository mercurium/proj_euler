import string
import time
from bitarray import bitarray
START = time.time()

LIM = 10**4
is_prime = bitarray('001' + '10' * LIM)[:LIM]
for i in xrange(3,LIM,2):
    if is_prime[i]:
        for j in xrange(i**2,LIM,2*i):
            is_prime[j] = False
prime_lst = []
for i in xrange(1000,10000):
    if is_prime[i]:
        prime_lst.append(i)


def rotation(a,b,c):
    a,b,c = sorted(str(a)),sorted(str(b)),sorted(str(c))
    return a == b and a == c

def dig(a):
    return string.join(sorted(str(a)),'')        

d = dict()
for item in prime_lst:
    if dig(item) in d:
        d[dig(item)] += [item]
    else:
        d[dig(item)] = [item]
    
nums_to_test = d.keys()

for sorted_dig in nums_to_test:
    if len(d[sorted_dig]) >= 3:
            primes = d[sorted_dig]
            primes.sort()
            for i in range(0,len(primes)-1):
                for j in range(i+1,len(primes)):
                    if 2*primes[j]-primes[i] in primes:
                        print primes[i], primes[j], 2*primes[j]-primes[i]

print "Time taken:",time.time() -START

"""
12:33 ~/Desktop/python_projects/proj_euler $ python prob49.py 
2969 6299 9629
1487 4817 8147
Time Taken:0.00468802452087

NOTE this isn't feeling satisfactory to me either... =/...Will need to redo later...
"""
