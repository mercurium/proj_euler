import time
START = time.time()
LIM   = 10**6

primes = [2,3,5,7,11,13,17,23]
product = 1
for prime in primes:
  if product * prime > LIM:
    break
  product *= prime

print "Answer:", product


"""
simple problem. Since n/totient(n) is minimized when you have as many prime factors as possible.... you should have as many prime factors as possible :P


"""
