import time
from bitarray import bitarray


SIZE  = 10**6
START = time.time()

def prime_gen(size):
  temp = bitarray(size)
  for i in xrange(1,len(temp),2):
    temp[i] = 0
  primeLst = []
  for i in xrange(3,len(temp),2):
    if temp[i] == 0:
      for j in xrange(i**2, len(temp),2*i):
        temp[j] = 1
      primeLst.append(i)
  return primeLst


primes   = prime_gen(SIZE/6)
primeLen = len(primes)
print "Time Taken:", time.time() - START

count = 0

index = 0
LIM   = SIZE**(1/7.)
while primes[index] <= LIM:
  index +=1
count += index

i,j = 0,0
while primes[i]*8 <= SIZE:
  while primes[j]**3*primes[i] <= SIZE:
    if i != j:
      count +=1
    j+=1
  j = 0
  i+= 1

print "Part 2 is:", count

i,j,k = range(3)
while i < primeLen and primes[i] * 6 < SIZE:
  j = i + 1
  while j < primeLen and primes[i]*primes[j]* 5 < SIZE:
    val = primes[i] * primes[j]
    k = j+1
    while k < primeLen and val * primes[k] <= SIZE:
      count += 1
      k     += 1
    j += 1
  i += 1

print "Part 3 is:", count


print "Answer is:", count
print "Time Taken:", time.time() - START


"""

8 divisors means that a number is either in the form

p^7
p^3 x q
p x q x r


p^7 case is super easy to handle. p^3 x q should also not be too bad to handle.

p x q x r might be a bit more annoying
"""
