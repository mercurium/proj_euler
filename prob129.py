import time
start = time.time()
from bitarray import bitarray

size = 10**6+10**5
prime_set = set()
p_lst = bitarray('0000'+'10'*(size/2))

for i in xrange(2,size):
  if p_lst[i] == 0:
    for j in range(i**2,size,i):
      p_lst[j] = 1
    prime_set.add(i)

primes_over_million = []
for i in xrange(10**6+1,size):
  if p_lst[i] ==0:
    primes_over_million.append(i)

print primes_over_million[:10]

for num in primes_over_million:
  if pow(10,num//2,num) != 1:
    print num
    break
  

print "Time Taken:", time.time()-start
