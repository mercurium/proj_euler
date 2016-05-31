import time
from primes import get_primes, ext_gcd, cipolla

START = time.time()
SIZE  = 10**7

def solveForPSquared(prime, m):
  a  = (m*(m-3) - 1) / prime
  k  = ext_gcd( 2*m-3, prime)[0] * (-1 * a)

  n  = (m + prime * k) % (prime**2)
  n2 = prime**2 + 3 - n
  return min(n,n2)

primes = get_primes(SIZE)

# need to skip 2,3,5,7,11,13 for this

# solution for p = 3 is 5, 2,7,11,13 have no solution
sumz = 5

# 4(n^2 - 3n - 1) = (2n-3)^2 - 13
# --> Cipolla's algorithm on (2n-3)^2 = 13 mod p
for prime in sorted(primes)[6:]:
  val = cipolla(prime, 13)
  if val == 0:
    continue
  elif val %2 == 0:
    m = (val+prime+3) / 2
  else:
    m = (val+3) / 2
  sumz += solveForPSquared(prime, m)

print "Answer:", sumz
print "Time Taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 457 is correct.

You are the 428th person to have solved this problem.


Answer: 2647787126797397063
Time Taken: 22874.3746512 <-- ...6.6 hours -_-;;
Time Taken: 86.7825520039 <-- after reading the forums and realiziing I need to use cipolla's algorithm... which i had already coded up before anyways. Derp lol


4(n^2 - 3n - 1) = 4n^2 - 12n - 4 = (2n-3)^2 -13
-> (2n-3)^2 = 13

Applying Cipolla's algorithm to that, we get a value, 'val', where 2n-3 = m (mod p), which we can solve pretty darn easily.
After that, we have:
  m^2 - 3m - 1 = 0 mod p
  -> m^2 - 3m - 1 = a*p (for some a)

So, if we let n = m + kp, we get:
  n^2 - 3n - 1
  = (m+kp)^2 - 3(m+kp) - 1
  = m^2 + 2mkp + k^2p^2 - 3m - 3kp - 1
  = (m^2 - 3m - 1) + kp(2m-3) + k^2p^2
  = ap + kp(2m-3) + k^2p^2
  -> p | (a + k(2m-3))   (last term falls off since it is divisible by p^2)

Since we know a and m at this point, we just need to solve for k. Ex:
  p = 17, m = 6
  -> 6^2 - 3(6) - 1 = 17
  -> (6^2 - 3*6 - 1) = 1 * 17
  -> a = 1
  -> 1 + k(2(6) - 3) = 0 mod 17
  -> 9k = -1 mod 17
  -> use extended_gcd algorithm to solve:
      c(17) + d(9) = 1
  (This solves to -1 * 17 + 2*9 = 1 -> k = 2 * -a -> k = 15 mod 17)
  -> n = m + kp = 6 + 15 * 17 = 261

Plugging in 261 and checking, we get:
  261^2 - 3*261 - 1 = 67337 = 233 * 289, which works!

Also, since n^2 - 3n - 1 = (n-1)(n-2) - 1, we get that:
  (p+3-n-1)(p+3-n-2) - 1
  = p^2 + 6p - 2pn + 9 - 6n + n^2 -3p - 9 + 3n - 1
  = (n^2 -3n -1) + p(3-2n)
  = (n^2 -3n -1) mod p

We get that if 'n' is a solution, then so is 'p+3-n' for the mod p part. For the mod p^2 part,
  n being a solution <=> `p^2+3-n` is a solution

"""

