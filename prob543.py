import time
from primes import get_prime_count
START = time.time()


SIZE      = 44
sumz      = 0
prev_n, n = 1,2

for k in xrange(3,SIZE+1):
  print k,n
  # add in all primes
  sumz += get_prime_count(n)
  # add in sums of 2 + prime
  sumz += max(get_prime_count(n - 2) - 1, 0)

  # All even numbers m > 2 can be expressed as the sum of g primes, where 2 <= g <= m / 2
  sumz += (n/2)     * ((n-2)/2) /2
  # All odd numbers m > 2 can be expressed as the sum of g primes, where 3 <= g <= m / 2 - 1
  if n > 5:
    sumz += ((n-3)/2) * ((n-5)/2) / 2

  prev_n, n = n, prev_n + n

print sumz
print "Time Taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 543 is correct.

You are the 296th person to have solved this problem.


Answer: 199007746081234640
Time Taken: 0.46103811264

Main point for this problem is goldbach's conjecture.

Total for S(n) =
  Sum of 1 prime: number of primes < n
  Sum of 2 primes (odd numbers): number of primes < n - 2
  Sum of k primes, k > 2 for odds, k > 1 for evens:
    All even numbers m > 2 can be expressed as a sum of 2 to m/2 - 1 primes
    All odd numbers m > 2 can be expressed as the sum of g primes, where 3 <= g <= m / 2 - 1

"""

