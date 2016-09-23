#NOTE TODO need to solve it
import time
from primes import m_r, gcd, primes, pollard_rho
from heapq import *
START = time.time()
SIZE  = 10**5 * 2
MOD   = 10**9 +7
count = 0

def isSquare(n):
  a = int(n**.5+.5)
  if a**2 == n:
    return true

small_primes = primes[:1000]

def insertIntoDict(valDict, key, value):
    if key in valDict:
      valDict[key] += value
    else:
      valDict[key] = value

def factor(n):
  if m_r(n):
    return [n]
  factorList = []
  for p in small_primes:
    while n % p == 0 and n > 1:
      factorList.append(p)
      n /= p
  while n != 1:
    if m_r(n):
      return (factorList + [n])
    d = pollard_rho(n)
    while n % d == 0:
      factorList.append(d)
      n /= d
  return factorList

heapA = []
heappush(heapA, (10**9,10**9))
heapB = []
heappush(heapB, (10**9,10**9))

for n in xrange(1,SIZE+1):
  valDict  = dict()

  a        = n**2 - 2*n + 2
  factorsA = []
  while heapA[0][0] == n:
    factorsA.append(heappop(heapA)[1])

  factorsA = list(set(factorsA))
  for f in factorsA:
    heappush(heapA, (n+f, f))
    while a % f == 0:
      a /= f
      insertIntoDict(valDict, f, 1)
  factorsA = factor(a)
  for f in set(factorsA):
    heappush(heapA, (n+f, f))
  for f in factorsA:
    insertIntoDict(valDict, f, 1)


  b        = n**2 + 2*n + 2
  factorsB = []
  while heapB[0][0] == n:
    factorsB.append(heappop(heapB)[1])

  factorsB = list(set(factorsB))
  for f in factorsB:
    heappush(heapB, (n+f, f))
    while b % f == 0:
      b /= f
      insertIntoDict(valDict, f, 1)
  factorsB = factor(b)
  for f in set(factorsB):
    heappush(heapB, (n+f, f))
  for f in factorsB:
    insertIntoDict(valDict, f, 1)

  prod     = 1

  for f in valDict.keys():
    prod = ((1 + pow(f, valDict[f],MOD)) * prod) % MOD

  count += prod - (n**4 + 4)% MOD

  if n% 1024 == 0:
    print n, time.time() - START

print count % MOD
print "Time Taken:", time.time() - START


"""
So, 2/20/2015, I'm looking at the code again. It seems to work. but I don't remember why. I didn't submit the problem, so I suspect that the limiting factor on this was the runtime. Yeah, for the 10**5 size problem, it's taken 18 seconds, and it only seems to be getting slower.

Congratulations, the answer you gave to problem 446 is correct.

You are the 206th person to have solved this problem.

Answer: 907803852
Time Taken: 747.287427902

9/23/2016 notes:
Lol, remembered that
  n^4 + 4 = 0 mod p
    then we have
  (n+p)^4 + 4 = 0 mod p



Size: 161792 Time Taken: 42.5061249733

Definitely not going to scale, but let's figure out why it works first...

"""
