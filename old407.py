#IMPORTANT! If a^2 = a mod n, then a(a-1) = 0 mod n, and thus a = 1 for primes.

import time
import sys
from primes import *

start = time.time()
size = int(sys.argv[1])

pfactor = range(0,size+1)
for i in xrange(2,len(pfactor)):
  if pfactor[i] == i:
    for j in xrange(i*2,len(pfactor),i):
      pfactor[j] = i
      
def extended_gcd(a, b): #returns c,d such that ac+bd =1
  if b == 0:
    return (1, 0)
  else:
    q, r = a/b, a%b
    s, t = extended_gcd(b, r)
    return (t, s - q * t)
ext_gcd = extended_gcd

def crt(bases, vals):  
  big_base = 1
  sumz = 0
  for val in bases: big_base *= val
  for i in range(0,len(bases)):
    curr_base = big_base / bases[i]
    inverse = ext_gcd(bases[i],curr_base)[1]
    sumz += vals[i] * curr_base * inverse
  return sumz % big_base

def upf(lst): #unique prime factors... :x
  return True in [lst[i] == lst[i-1] for i in xrange(1,len(lst)) ]

def calc(n):
  if pfactor[n] == n: return 1
  for i in xrange(n - pfactor[n], n/2-1, -1 * pfactor[n]):
    a = i**2
    if (a + i) % n == 0: return i+1
    if (a - i) % n == 0: return i
  return 1

def stupid_calc(n):
  if m_r(n): return 1
  for i in xrange(n-1,2,-1):
    if (i**2 - i)% n == 0:
      return i
  return 1

def sc_all(n): # a stupid calculator to figure out all # that work
  if m_r(n): return [1]
  works = [1]
  for i in xrange(2,n+1):
    if (i**2 - i)%n == 0:
      works.append(i)
  return works

def factorz(n):
  if n > size:return factor(n)
  if n == 1: return []
  return [pfactor[n]]+factorz(n/pfactor[n])
  
sumz = 0
for i in xrange(2,size+1):
  val = calc(i)
  sumz += val
  print i, val
print sumz
print "Time Taken: ", time.time() - start

#...LOL
#39782849136422 is the wrong answer I got after 
#Time Taken:  5072.10592484
#...aka, 1.4 hrs LOL

#LOL LOL LOL I HATE MYSELF. I REREAD THE QUESTION AND f(1) = 0, NOT f(1) = 1. BASICALLY I DIDN'T TURN THIS PROBLEM IN FOR A MONTH BECAUSE OF AN OFF BY ONE ERROR.... TT____TT
#39782849136421 is the right answer

