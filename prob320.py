"""
solve n/p+n/p^2 +... + n/p^k >= 1234567890 for all p < m for m in range 10 to size...
or equivalently... n(1/p+1/p^2+1/p^3+...)
(1/p + 1/p^2 + 1/p^3 + ... ) = 1/(p-1)
so we can use n = val / (1/p + 1/p^2 + 1/p^3 + ... etc)
 ---> n = val / (1/(p-1) ) --> n = val * (p-1) + stuff to be 0 mod p

okay, so that didn't work so i had to alter my original algorithm. Now I'm testing all primes less than n to see if they have the optimal solution. Obviously this is much slower than what we want since it requries a O(n/ln(n)) testing instead of a simple O(1) testing per number... and this testing doesn't come cheap...also it's not correct atm :D;; oops

raaaah @___@... I'll ask michikins to help me with this =D
"""
import time
from bitarray import bitarray
from primes import *
start = time.time()

val = 1234567890
sumz = 0
size = 10**3


prime_set = set([2])
lst = bitarray('0'*(int(size*1.1)))
for i in xrange(3,len(lst),2):
  if lst[i] == 0:
    prime_set.add(i)
    for j in range(2*i,len(lst),i):
      lst[j]= 1
prime_lst = list(prime_set)
prime_lst.sort()

print "Time Taken:", time.time()- start


def cfpn(n, val, base): #compute for power of random base
  sumz = 0
  comp = base
  while comp <= n:
    sumz += n/comp
    comp *= base
#  print sumz, val, base-1
  valz = sumz * val* (base-1) + (( sumz * val )%base )
  return valz
  
  
sumz = 0
for i in xrange(10,size+1):
  val2 = 0
  maxz = 0
  if i not in prime_set:
    for j in xrange(0,len(prime_lst)):
      if prime_lst[j] > i: break
      temp = cfpn(i,val,prime_lst[j])
      if temp > val2:
        val2 = temp
        maxz = prime_lst[j]
  else:
    maxz = i
    val2 = cfpn(i,val,i)
  #print maxz, i
  sumz+= val2

print sumz
print "Time Taken:", time.time()- start



