import string
import math
true = True
false = False

#methods in file: is_prime(num), factor(val), totient(n), repeated_squaring(n,pow,mod), reverse_num(n), mergesort(list), gcd(a,b), ncr(n,r)


temp = open('primenum.txt','r')
primes = string.split(temp.read()[:-2],', ')
primes = [int(i) for i in primes]
del primes[primes.index(9999)]
primes_set = set(primes)


temp = open('primenum10000.txt','r')
primes_few = string.split(temp.read(),',')
primes_few = [int(i) for i in primes_few]

carmichael = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001, 410041, 449065, 488881, 512461, 530881, 552721, 656601, 658801, 670033, 748657, 825265, 838201, 852841, 997633, 1024651, 1033669, 1050985, 1082809, 1152271, 1193221, 1461241, 1569457, 1615681, 1773289, 1857241, 1909001, 2100901, 2113921, 2433601, 2455921, 2508013, 2531845, 2628073, 2704801, 3057601, 3146221, 3224065, 3581761, 3664585, 3828001]


def factor_rec(val, count):
  while(val >= count):
    if val % count == 0:
       return count
    count = count + 1

def factor(val):
  if val == 1:
    return [1]
  if primer2(val):
    return [val,1]
  temp = factor_smart(val)
  if temp == -1:
    temp = factor_rec(val, 2)
  return [temp] + factor(val/temp)
  
def factor_smart(val):
  found = -1
  for i in xrange(0, len(primes)):
    if val % primes[i] ==0:
      found =primes[i]
      break
  return found
  
def totient(n):
  lst = factor(n)[:-1]
  result = 1.0
  for i in range(0,len(lst)):
    if i==0 or lst[i] != lst[i-1]:
      result = result * (lst[i]-1)
    else:
      result = result * lst[i]
  return result

#this takes a set of values and bases so that we can find x s.t.
#x = a1 mod b1
#x = a2 mod b2
#... and so on for any number of bases

def crt(bases, vals):  
  big_base = 1 
  sumz = 0 
  for val in bases: big_base *= val 
  for i in range(0,len(bases)):
    curr_base = big_base / bases[i]
    inverse = ext_gcd(bases[i],curr_base)[1]
    sumz += vals[i] * curr_base * inverse
  return sumz % big_base


#http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def miller_rabin(n): 
  if n == 1: return False
  if n in primes_set: return True #doesn't work for n < 3
  
  for i in range(0,100): #save us some excessive calculations
    if n%primes[i] == 0:
      return False
  
  d,r = n-1, 0
  while d %2 == 0:
    r+=1 
    d/= 2 #We'll have n-1 = 2^r * d
  
  
  if n >= 3825123056546413051: return -1 #too large of an input for us
  if n < 1373653: lstz = [2,3]
  elif n < 9080191: lstz = [31,73]
  elif n < 4759123141: lstz = [2,7,61]
  elif n < 2152302898747: lstz = [2,3,5,7,11]
  elif n < 3474749660383: lstz = [2,3,5,7,11,13]
  elif n < 341550071728321:  lstz = [2,3,5,7,11,13,17]
  elif n < 3825123056546413051: lstz = [2,3,5,7,11,13,17,19,23]
  
  def try_composite(a):
    val = pow(a,d,n)
    if val == 1:
      return False
    for i in range(r):
      if val == n-1:
        return False
      val = pow(val,2,n)
    return True # n is definitely composite
 
  for a in lstz:
    if try_composite(a):
      return False
 
  return True 
  
mr = m_r = miller_rabin

def is_prime(n):
  return primer2(n)

def primer2(n):
  if n in carmichael or n ==1:
    return False
  
  if n <= primes[-1]:
    if n in primes_set:
      return True
    return False
  for i in range(0,100):
    if n % primes[i] == 0:
      return False
    if primes[i] >= n:
      return True
    if rep_sq(primes[i],n-1,n) != 1:
      return False
  return True
  
def rep_sq(n, powz, mod):
  if powz == 0: return 1
  if powz == 1: return n % mod
  
  
  val = int(math.log(powz,2))
  lst = [1,n] + [0] * val
  for i in range(2,len(lst)):
    lst[i] = lst[i-1]**2 % mod
  
  pows = [0] * (val+1)
  power = powz
  for i in range(0,len(pows)):
    pows[i] = power % 2
    power = power //2 
  product = 1
  for i in range(0,len(pows)):
    if pows[i] == 1:
      product = product * lst[i+1] % mod
  return product

def reverse(num):
  return int(str(num)[::-1])
  
def reverser(strs):
  return strs[::-1]


def mergesort(lst):
  temp = lst[:]
  temp.sort()
  return temp


def gcd(a,b):
  while b:
    a,b = b, a%b
  return a
  
import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    num = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return num//denom

