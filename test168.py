import time
start = time.time()
from bitarray import bitarray

size = 10**4
prime_ba = [1] * size
primes =[]
for i in xrange(3,size,2):
  if prime_ba[i] == 1:
    primes.append(i)
    for j in xrange(i**2,size,2*i):
      if prime_ba[j] ==1:
        prime_ba[j] = i



setz = set()
for i in xrange(3,size,2):
  if i %5 == 0 or (prime_ba[i] == 1 and i > 101):
    continue
  for j in xrange(1,min(i,100)):
    if pow(10,j,i) == 1:
      for k in xrange(1,i):
        a = 10**j*k//i
        b = a/10 + (a%10)*10**(j-1)
        if b%a == 0 and len(str(a)) == len(str(b)):
          setz.add(a)
      break
print sum(setz)%10**6, len(setz)
print "Time Taken:" ,time.time() - start
