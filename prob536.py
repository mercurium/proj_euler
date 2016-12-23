import time
from primes import get_primes, gcd, crt, lcm_list

START       = time.time()
SIZE        = 10**12
factor      = {1 : [], 2: [2], 3: [3]}
answers     = set([1,2])
possibleAns = set([1])
primes      = get_primes(int(SIZE**.5))

def checkProperty(m, factors=None):
  if not factors:
    factors = factor[m]
  for f in factors:
    if (m + 3) % (f - 1) != 0:
      return False
  return True

compatCache = dict()
def compat_check(p1, p2):
  if (p1,p2) in compatCache:
    return compatCache[(p1,p2)]
  gcd1 = gcd(p1-1, p2)
  if gcd1 != 1:
    if (p1-4) % gcd1 != 0:
      compatCache[(p1,p2)] = False
      return False

  gcd2 = gcd(p2-1, p1)
  if gcd2 != 1:
    if (p2-4) % gcd2 != 0:
      compatCache[(p1,p2)] = False
      return False
  compatCache[(p1,p2)] = True
  return True


def cheat_crt(prime_list):
  prime_prod = reduce(lambda x,y: x*y, prime_list)
  prime_tot  = lcm_list([x-1 for x in prime_list])

  prime_prod /= gcd(prime_prod, prime_tot)
  return crt([prime_prod, prime_tot], [0, prime_tot - 3])

def dealWithLargePrime(prime):
  num = prime - 4
  while num * prime < SIZE:
    if num in possibleAns:
      if checkProperty(num*prime, factor[num] + [prime]):
        factor[num*prime] = factor[num] + [prime]
        answers.add(num*prime)
    num += prime - 1

def check(prime, lim=64):
  if prime**3/lim > SIZE:
    dealWithLargePrime(prime)
    return

  for n in list(possibleAns):
    if n * prime > SIZE or len(factor[n]) == 9:
      possibleAns.remove(n)
      if checkProperty(n):
        answers.add(n)
      continue

    if n * prime**2 > SIZE:
      if checkProperty(n*prime, factor[n] + [prime]):
        factor[n*prime] = factor[n] + [prime]
        answers.add(n*prime)
    else:
      if not cheat_crt(factor[n] + [prime]) < SIZE:
        continue
      if not all([compat_check(x, prime) for x in factor[n]]):
        continue

      factor[n*prime] = factor[n] + [prime]
      possibleAns.add(n*prime)


for prime in primes[1:]:
  print prime, len(possibleAns), time.time() - START
  check(prime)

answers.add(2)
print "Time Taken:", time.time() - START

for i in possibleAns:
  if checkProperty(i):
    answers.add(i)

print sum(answers), len(answers)
print "Time Taken:", time.time() - START


"""

  Congratulations, the answer you gave to problem 536 is correct.

  You are the 182nd person to have solved this problem.

  Answer: 3557005261906288


  Numbers that seem to work: products of primes with no repeats (aka, p^2k does not work), and no evens besides 2.

  For each prime, p, we need the number to equal:
  m = p-4 (mod p-1)

  We can figure out which multiples of primes work for a prime by using:
  m = p(p-4 + k(p-1)) for all k >= 0

  Ex: for 7, we can have...
    7((7-4) + 0(7-1)) = 21 <-- actual answer that works
    7((7-4) + 1(7-1)) = 21 + 42 = 63. <-- Doesn't work since 63 = 3^2 * 7, but it satisfies the 7 req
    7((7-4) + 2(7-1)) = 21 + 84 = 105. <--- actual answer that works

  10^2 has 5    answers
  10^3 has 9    answers
  10^4 has 15   answers
  10^5 has 36   answers
  10^6 has 84   answers (0.044378 seconds)
  10^7 has 175  answers (0.1339559 seoncds)
  10^8 has 439  answers (1.19557906 seconds)
  10^9 has 1038 answers? (12.05828 seconds)
  10^10 has 2348 answers? (46.2426 seconds now!)
  10^12 has 12997 answers (4500ish seconds, didn't actually time it, had to modify it later)


"""
