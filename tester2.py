import time
start = time.time()
from bitarray import bitarray
from primes import mr
size = 10**6 # size of the problem 

#prime set generator
temp_lst = bitarray('1' * size)
prime_set = set([2,3,5])
for j in xrange(15,len(temp_lst),5):
      temp_lst[j] = 0
for i in xrange(1,len(temp_lst)//6):
  a,b = i*6+1,i*6+5
  if temp_lst[a]:
    prime_set.add(a)
    for j in xrange(a,len(temp_lst),a):
      temp_lst[j] = 0
  if temp_lst[b]:
    prime_set.add(b)
    for j in xrange(b,len(temp_lst),b):
      temp_lst[j] = 0
if size % 6 == 5:
  if temp_lst[size] == 1: prime_set.add(size)
  if temp_lst[6*(size//6)+1] == 1: prime_set.add(6*(size//6)+1)
elif size % 6 != 0:
  if temp_lst[6*(size//6)+1] == 1: prime_set.add(6*(size//6)+1)
print sum(prime_set)


print "Time Taken: ", time.time() -start


