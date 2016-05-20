import time
from primes import get_totient, gcd, crt
START       = time.time()
lower_bound = 10**6
upper_bound = lower_bound + 5000
answer      = 0

totients    = get_totient(upper_bound)

for n in xrange(lower_bound, upper_bound):
  for m in xrange(lower_bound, n):
    gcdVal = gcd(m,n)
    if gcdVal == 1:
      number = crt([n,m], [totients[n], totients[m]]) % (n * m)
      answer += number
    else:
      # if the two totients aren't equal mod the gcd, continue
      if totients[n] % gcdVal != totients[m] % gcdVal:
        continue
      values = [ (totients[n] / gcdVal), totients[m] / gcdVal ]
      number = crt([n/ gcdVal, m / gcdVal], values) * gcdVal + totients[n] % gcdVal

      answer += number

print answer
print "Time Taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 531 is correct.

You are the 448th person to have solved this problem.
pypy prob531.py
Answer: 4515432351156203105
Time Taken: 14.7158670425

pretty easy problem. If the two bases are relatively prime, we can run the normal CRT algorithm on the pair.

If they're not relatively prime, and their totients aren't equal mod the gcd, then there is no solution for the pair.

If the two totients are congruent mod the prime, and the gcd isn't 1, then the formula becomes:
  gcd = gcd(n,m)
  f(tot(n), n, tot(m), m)
    = crt( [n/gcd, m/gcd], [tot(n)/gcd, tot(m)/gcd]) * gcd + tot(n) % gcd

  yup. pretty straightforward



"""
