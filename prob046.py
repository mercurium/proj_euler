import time
START = time.time()
from bitarray import bitarray

SIZE = 10000

is_prime = bitarray('001' + '10' * SIZE)
primes = [2]
for p in xrange(3,len(is_prime),2):
    if is_prime[p]:
        for not_p in xrange(p**2,len(is_prime),p*2):
            is_prime[not_p] = False
        primes.append(p)

squares = set( [x**2 for x in xrange(0,SIZE)] )

for num in range(9,10000,2):

    if not is_prime[num]:
        prime_index = 0
        sol_not_found = True  #unless we find a prime that works, we're sol_not_found.
        while primes[prime_index] < num and sol_not_found:
            n = (num-primes[prime_index])/2
            if n in squares:
                sol_not_found = False
                break
            prime_index = prime_index+1
        if sol_not_found:
            print num
            break
            

print "Time taken:",time.time() -START

"""
Huh, who knew. math.sqrt(n) is faster than n**.5... o.O

12:13 ~/Desktop/python_projects/proj_euler $ python prob46.py 
5777
Time Taken: 0.107497930527

"""
