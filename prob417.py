import time
from primes import pfactor_gen, get_totient, get_divisors_given_pfactor, mr, factor_given_pfactor, lcm
START = time.time()
SIZE  = 10**8

def get_divisors(n): # returns all divisors of n.
  return get_divisors_given_pfactor(n, pfactors)

def factor(n):
  return sorted(factor_given_pfactor(n, pfactors))

def rep_dig(n): #Gives the first power of 10 such that 10^k = 1 mod n.
  potential_pows = get_divisors(totient[n])
  for powz in potential_pows:
    if pow(10,powz,n) == 1:
      return powz

def rep_dig_prime(p):
  potential_pows = get_divisors(p-1)
  for powz in potential_pows:
    if pow(10,powz,p) == 1:
      return powz

pfactors  = pfactor_gen(SIZE)
#totient   = get_totient(SIZE)
values    = [0] * SIZE
values[3] = 1
for i in xrange(5,SIZE,2): #Evens are easy to compute, do it later
  if i %1024 == 1:
    print i
  if i %5 == 0: # multiples of 5 add no extra digits from the factor of 5.
    values[i] = values[i/5]
    continue
  if pfactors[i] == i:
    values[i] = rep_dig_prime(i)
  else:
    prime_factors = factor(i)
    values[i]     = values[prime_factors[0]]
    for index in xrange(1,len(prime_factors)):
      prime = prime_factors[index]
      if prime == 3 and index == 1:
        continue
      if prime_factors[index] == prime_factors[index-1]:
        values[i] *= prime
      else:
        values[i] = lcm(values[i], values[prime])
    if i % 237169 == 0:
      values[i] /= 487


for i in xrange(2,SIZE,2):
  values[i] = values[i/2]

print sum(values)
print "Time Taken:", time.time() - START

"""
For comparison sake, 94288
is the right answer for size 10^3

17:43 ~/Desktop/python_projects/proj_euler $ python prob417.py 1000000
55535191115
time taken: 22.1281189919


446572970925740 (answer)
time taken: 4837.17608619
Time Taken: 2301.69793391 # Used pypy instead on work mac
Time Taken: 139.207489014 # Holy shit optimization using https://en.wikipedia.org/wiki/Repeating_decimal#Other_properties_of_repetend_lengths


For comparison sake... LOL, 7200ish seconds on school computer (via ssh) 7214.40327597

Okay, cool. So for this problem, I used the fact that a fraction, 1/n repeats after we can find a 'k' value such that 10^k = 1 mod n. This can be seen to be true since, supposing we have 5 repeating digits for 1/n. Then
1/n = .abcdeabcdeabcde.... And that means that 10^5/n = abcde.abcdeabcde.... Then 99999/n = abcde. This means that 99999 = 0 mod n, and so 10^5 = 1 mod n.

Now that we've established why we need to find 10^k = 1 mod n for all n, we can use Fermat's Little Theorem (a generalization) to tell us that a^k = 1 mod n if and only if 'k' is a divisor of totient(n). Computing this for all numbers, we get the algorithm that we desire. Wins :)

"""
