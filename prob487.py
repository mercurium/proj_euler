import time
from primes import m_r
START = time.time()

num         = 10**12
start_val   = 2*10**9
end_val     = 2*10**9 + 2000
power       = 10**4
running_sum = 0

for p in xrange(start_val, end_val):
  # ignore non primes
  if m_r(p):
    nModp = num % p
    running_sum += (-1 * sum( [ (nModp + 1 - x) * pow(x, power, p) \
                      for x in xrange((num+1)%p, p+1) ])) % p
    print p, running_sum

print running_sum
print "Time Taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 487 is correct.
You are the 358th person to have solved this problem.

Answer     : 106650212746
Time Taken : 16.3226361275

Quick summary on this problem.

The problem asks us to find:
  sum_{2*10^9 <= p <= 2*10^9, p prime} (
    sum_{1 <= i <= 10^12} ( (10^12 + 1 - i) * i^(10^4)) mod p
  )

Looking at a quick example below, we note that for n=10, prime = 7, we only need to examine 8 to 10 instead of 1-10. Alternatively, we can also look at just 12-14, since we know that going from 1 mod p to p-1 mod p with the right multiples gives us 0.

Axioms:
  1) 1^k + 2^k + .. + p^k = 0 mod p.
    - Using a proof by induction on the formulas in #547, we can prove this to be true
  2) n^2 = (p-n)^2 mod p
    - (p-n)^2 = p^2 - 2pn + n^2 = n^2 mod p
  3) n^(10^4) = (p-n)^(10^4)
    - Obvious via 2). Just use m = n^5000


smaller example:
  n     = 10
  power = 2
  prime = 7

  S_2(10) mod 7 = (10 * 1^2 + 9 * 2^2 + 8 * 3^2 + 7 * 4^2 + 6 * 5^2 + 5 * 6^2 + 4 * 7^2 + 3 * 8^2 + 2 * 9^2 + 1 * 10^2) % 7

  = (10 * 1^2 + 9 * 2^2 + 8 * 3^2 + 7 * 4^2 + 6 * 5^2 + 5 * 6^2 + 4 * 7^2) % 7  + (3 * 8^2 + 2 * 9^2 + 1 * 10^2) % 7

  = (3 * 8^2 + 2 * 9^2 + 1 * 10^2) % 7 // We can collapse away most of it

"""
