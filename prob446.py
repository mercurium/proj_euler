#NOTE TODO need to solve it
import time
from primes import m_r, gcd, primes, pollard_rho
from heapq import *
START = time.time()
SIZE  = 10**7
MOD   = 10**9 +7
count = 0

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
  while n != 1:
    if m_r(n):
      return (factorList + [n])
    d = pollard_rho(n)
    while n % d == 0:
      factorList.append(d)
      n /= d
  return factorList

heaps = [ [], [] ]
heappush(heaps[0], (10**9,10**9)) # hack to get around dealing with empty heaps
heappush(heaps[1], (10**9,10**9))

for n in xrange(1,SIZE+1):
  # n^4 + 4 = (n^2 - 2n + 2)(n^2 + 2n + 2)
  nFactors  = [n**2 - 2*n + 2, n**2 + 2*n + 2]
  valDict   = dict()

  for i in xrange(2):
    num     = nFactors[i]
    factors = []
    while heaps[i][0][0] == n:
      factors.append(heappop(heaps[i])[1])

    for f in factors:
      heappush(heaps[i], (n+f, f))
      while num% f == 0:
        num /= f
        insertIntoDict(valDict, f, 1)

    for f in factor(num):
      heappush(heaps[i], (n+f, f))
      insertIntoDict(valDict, f, 1)

  prod = 1

  for f in valDict.keys():
    prod = ((1 + pow(f, valDict[f],MOD)) * prod) % MOD

  count += prod

  if n% 1024 == 0:
    print n, time.time() - START

count = count - (6 * SIZE**5 + 15 * SIZE**4 + 10 * SIZE**3 - SIZE)/30 - 4*SIZE

print count % MOD
print "Time Taken:", time.time() - START


"""
So, 2/20/2015, I'm looking at the code again. It seems to work. but I don't remember why. I didn't submit the problem, so I suspect that the limiting factor on this was the runtime. Yeah, for the 10**5 size problem, it's taken 18 seconds, and it only seems to be getting slower.

Congratulations, the answer you gave to problem 446 is correct.

You are the 206th person to have solved this problem.

Answer: 907803852
Time Taken: 747.287427902
Time Taken: 641.248315811 # Cleaned up previous code a bit


9/23/2016 notes:
Lol, remembered that
  n^4 + 4 = 0 mod p
    then we have
  (n+p)^4 + 4 = 0 mod p



Size: 161792 Time Taken: 42.5061249733

Definitely not going to scale, but let's figure out why it works first...

"""
