import string, math, os, random, commands

#methods in file: is_prime(num), factor(val), totient(n), repeated_squaring(n,pow,mod), reverse_num(n), mergesort(list), gcd(a,b), ncr(n,r)

# While not all of these methods are as optimial as they should be, this is a sort of file for me to keep my old algorithms that I wrote at one point in case I would like to use a variant later.
# Afte all, it's much easier to modify code that's already there (this only holds for my own code) than dealing with off by one errors with a new algorithm :)

def get_primes(size):  #gives you all the primes < size
  lst = [1] * (size+1)
  primes = [2]
  for i in xrange(3,len(lst), 2):
    if lst[i] == 1:
      primes.append(i)
      for j in xrange(i**2,len(lst),2 * i):
        lst[j] = 0
  return primes

primes     = get_primes(10**6)
primes_set = set(primes)
primes_few = filter((lambda x: x < 105000), primes)

def factor(n):
  if n == 0:
    return []
  if m_r(n):
    return [n]
  factor_lst = []
  for i in primes_few:
    while n % i == 0:
      factor_lst.append(i)
      n /= i
  while n != 1:
    if m_r(n):
      return (factor_lst + [n])
    d = pollard_rho(n)
    while n % d == 0:
      factor_lst.append(d)
      n /= d
  return factor_lst

def divisors(n): # don't use for larger numbers...
  factors  = factor(n)
  divisors = set([1])
  for f in factors:
    divisors = divisors.union(set([x*f for x in divisors]))
  return sorted(divisors)

def get_prime_count(n):
  fileName = 'tempVal1s34af44'
  os.system('primecount ' + str(n) + ' > ' + fileName)
  dataFile = open(fileName, 'r')
  value    = int(dataFile.read().strip())
  dataFile.close()

  return value

def totient(n): #dumb version, don't use this...
  if n == 1:
    return 1
  lst = factor(n)
  result = lst[0] - 1
  for i in xrange(1,len(lst)):
    if lst[i] != lst[i-1]:
      result = result * (lst[i]-1)
    else:
      result = result * lst[i]
  return int(result)

def get_totient(size):  #gives you the totients of all numbers i <= size
  lst = range(size+1)
  lst[0] = 1
  for i in xrange(2,len(lst)):
    if lst[i] == i:
      for j in xrange(i,len(lst),i):
        lst[j] = (lst[j] * (i-1))/i
  return lst


def pfactor_gen(size): #for each number n, return some factor of it.
    stuff = [0,1,2] + [1,2] *(size/2-1)
    for i in xrange(3,size,2):
        if stuff[i] == 1:
            for j in xrange(i**2,size,i*2):
                stuff[j] = i
            stuff[i] = i
    return stuff

def factor_given_pfactor(n, pfactor):
  #simple factoring method, put one of the factors of n onto the list until we run out of factors
  if n == 1:
    return []
  if pfactor[n] == n:
    return [n]
  factors = []
  while pfactor[n] != 1:
    factors.append(pfactor[n])
    n /= pfactor[n]
  return factors

def get_divisors_given_pfactor(n, pfactor):
  factors = factor_given_pfactor(n, pfactor)
  divisors = set([1])
  for f in factors:
    divisors = divisors.union(set([ x*f for x in divisors]))
  return sorted(divisors)

def legendre(a,p): # http://en.wikipedia.org/wiki/Legendre_symbol
  if a <= 1:
    return 1
  if a == 2:
    if (p**2 -1)% 16 == 0:
      return 1
    return  -1
  factors = factor(a)
  product = 1
  for f in factors:
    if f == 2:
      if (p**2 -1) % 16 != 0:
        product *= -1
    else:
      product *= legendre(p%f,f) * pow(-1,(f-1)*(p-1)/4)
  return product
lg = legendre


def cipolla(p, n): # http://en.wikipedia.org/wiki/Cipolla%27s_algorithm
  a = random.randint(int(p**.5)+1,p-1)
  while legendre((a**2-n)%p,p) == 1:
    a = random.randint(int(p**.5)+1,p-1)
  val = rep_sq_sqrt((a,1,(a**2-n)%p), (p+1)/2, p)
  return val[0]


def rep_sq_sqrt(n, power, mod): #NOTE, n is a tuple... a,b,c so that we had a + b * sqrt(c)
  def mult(a,b): #multiplying numbers which share a square root (sqrt)
    full = a[0] * b[0] + a[1] * b[1] * a[2]
    frac = a[1] * b[0] + a[0] * b[1]

    if abs(full) > mod: full = full % mod
    if abs(frac) > mod: frac = frac % mod
    return (full, frac, a[2])

  if power == 0: return (1,0,n[0])
  if power == 1: return n

  binRepOfPower = [int(x) for x in bin(power)[2:][::-1]]
  numRepSq      = [1,n] + [0] * len(binRepOfPower)
  for i in xrange(2,len(numRepSq)):
    numRepSq[i] = mult(numRepSq[i-1],numRepSq[i-1])

  product = (1,0,n[2])
  for i in xrange(0,len(binRepOfPower)):
    if binRepOfPower[i] == 1:
      product = mult(product,numRepSq[i+1])
  return product

def extended_gcd(a, b): #returns c,d such that ac+bd =1
  if b == 0:
    return (1, 0)
  else:
    q, r = a/b, a%b
    s, t = extended_gcd(b, r)
    return (t, s - q * t)
ext_gcd = extended_gcd

def multInverse(n, mod):
  return ext_gcd(n, mod)[0] % mod

#this takes a set of values and bases so that we can find x s.t.
#x = a1 mod b1
#x = a2 mod b2
#... and so on for any number of bases

def crt(bases, vals):
  big_base = reduce(lambda x,y: x*y, bases)
  sumz = 0
  for i in xrange(0,len(bases)):
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

is_prime = mr = m_r = miller_rabin

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


def gcd(a,b):
  while b:
    a,b = b, a%b
  return a

def lcm(a,b):
  return a*b / gcd(a,b)

def lcm_list(lst):
  return reduce(lambda x,y: lcm(x,y), lst)

import operator as op
def ncr(n, r):
  if r > n:
    return 0
  r = min(r, n-r)
  if r == 0: return 1
  num = reduce(op.mul, xrange(n, n-r, -1))
  denom = reduce(op.mul, xrange(1, r+1))
  return num//denom

def findNumLessThan(lst, num):
  if lst[-1] <= num:
    return len(lst)
  if lst[0] > num:
    return 0

  start = 0
  end   = len(lst)
  index = (start+end)/2

  def helper(index, start,end):
    if lst[index] <= num and lst[index+1] > num:
      return index
    elif lst[index] > num:
      start = index
    else:
      end = index
    index = (start+end)/2
    return helper(index, start, end)
  return helper(start, end, index)

def pollard_rho(n):
  def func(x):
    return (x**2+1)%n
  def func2(x):
    return (x**2+3)%n
  x,y = 2,2
  d = 1
  while d==1:
    x = func(x)
    y = func(func(y))
    d = gcd(abs(x-y),n)

  if d==n:
    d=1
    while d==1:
      x = func2(x)
      y = func2(func2(y))
      d = gcd(abs(x-y),n)
  return d

