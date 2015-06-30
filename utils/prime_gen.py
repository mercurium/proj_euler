import time, sys, math
from bitarray import bitarray


# This is made for larger sizes, so it might return weird results for n < 30
def prime_sum(size):

  primes            = [2,3,5,7,11,13,17,19,23,29]
  next_to_check     = primes[:]#[30,30,30,49,121,169,289, 361, 529, 841]
  running_prime_sum = sum(primes)

  max_prime_size_to_append = int(size**0.5)

  indices_to_check  = [1,7,11,13,17,19,23,29]

  for i in xrange(1,size//30 +1):
    thirty_i = 30 * i

    # marking the 8 indices out of 30 that we even need to bother to check
    nums_to_check = [1] * 30
    for j in indices_to_check:
      nums_to_check[j] = 0

    for prime_index in xrange(len(primes)):
      # went past the limit here

      prime = primes[prime_index]

      while next_to_check[prime_index] < thirty_i + 30:
        while next_to_check[prime_index] < thirty_i:
          next_to_check[prime_index] += primes[prime_index]
        spot = next_to_check[prime_index] % 30
        nums_to_check[spot] = 1
        next_to_check[prime_index] += primes[prime_index]

    # Updating our list of primes with the new ones we've discovered.
    for j in indices_to_check:
      new_prime = thirty_i + j
      if nums_to_check[j] == 0 and new_prime < size:
        if new_prime <= max_prime_size_to_append:
          primes.append(new_prime)
          next_to_check.append(new_prime ** 2)
        running_prime_sum += new_prime

  while len(primes) > 0 and primes[-1] > size:
    overly_large_prime = primes.pop()
    running_prime_sum -= overly_large_prime

  return running_prime_sum

# This is made for larger sizes, so it might return weird results for n < 30
def prime_gen(size):

  primes = [2,3,5,7,11,13,17,19,23,29]

  indices_to_check = [1,7,11,13,17,19,23,29]

  for i in xrange(1,size//30 +1):
    thirty_i = 30 * i

    # marking the 8 indices out of 30 that we even need to bother to check
    nums_to_check = bitarray('1' * 30)
    for j in indices_to_check:
      nums_to_check[j] = 0

    for prime in primes:
      # went past the limit here
      if prime ** 2 > thirty_i + 30:
        break

      starting_spot = ((prime - thirty_i) % prime)
      for spot in xrange(starting_spot, 30, prime):
        nums_to_check[spot] = 1

    # Updating our list of primes with the new ones we've discovered.
    for j in indices_to_check:
      if nums_to_check[j] == 0:
        primes.append(thirty_i + j)

  while len(primes) > 0 and primes[-1] > size:
    primes.pop()
  return primes


def pfactor_gen(size): #for each number n, return some factor of it.
  factors = [0,1,2] + [1,2] *(size/2-1)
  for i in xrange(3,size,2):
    if factors[i] == 1:
      for j in xrange(i**2,size,i*2):
        if factors[j] == 1:
          factors[j] = i
      factors[i] = i
  return factors

def expensive_pfactor_gen(size):
  pfactors = pfactor_gen(size)
  print "expensive pfactor needs:", sys.getsizeof(pfactors) / 10**6., "mb"
  primes = []
  for i in xrange(2,size+1):
    if pfactors[i] == i:
      primes.append(i)
  return primes

epg = expensive_pfactor_gen
SIZE = 10**7

START_1  = time.time()
primes_1 = epg(SIZE)
END_1    = time.time()
print "method one took:", END_1 - START_1


START_2      = time.time()
primes_sum_2 = prime_sum(SIZE)
END_2        = time.time()
print "method two took:", END_2 - START_2
print "cheaper pfactor needs:", sys.getsizeof(primes_sum_2) / 10**6., "MB"

print "difference in two methods was:", sum(primes_1) - primes_sum_2




#START_2  = time.time()
#primes_2 = prime_gen(SIZE)
#END_2    = time.time()
#print sys.getsizeof(primes_2)
#print "method two took:", END_2 - START_2




