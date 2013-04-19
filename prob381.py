#for this problem, we pretty much just need to solve 8x = -3 mod p... for p < 10^8
import math
import time
from bitarray import bitarray
start = time.time()

def extended_gcd(a,b):
  x, y,lastx,lasty = 0,1,1,0
  while b != 0:
    quotient = a //b
    a,b = b, a%b
    x,lastx = lastx-quotient*x,x
    y,lasty = lasty-quotient*y,y
  return lastx

def test(p):
  val = extended_gcd(8,p)
  val = val * -3 % p
  return val

prime_set = set([])
lst = bitarray('0'*(10**6))
for i in xrange(3,len(lst),2):
  if lst[i] == 0:
    prime_set.add(i)
    for j in range(2*i,len(lst),i):
      lst[j]= 1
      
print "Time Taken:", time.time()- start

if 3 in prime_set:
  prime_set.remove(3)

lst = 1
sumz = 0
for prime in prime_set:
  sumz += test(prime)
print sumz
print "Time Taken:", time.time()- start







