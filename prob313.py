import time
from primes import get_primes
START  = time.time()
SIZE   = 10**6
primes = get_primes(SIZE)
count  = 1 + (sum([p**2 for p in primes]) - len(primes) + 2)/12

print count
print "Time Taken:", time.time() - START

"""
Tl;dr: Use code from 244 to create a brute force method, then look at patterns to get the closed form answer

I started with the maze solver code from problem 244 to create a brute force way of computing the length of the path of a grid of size (n,m).

Using that brute force method, I found out:
  lenShortestPath(n,m) = 8n - 11 + 6 * (m - n)     if n <= m
  lenShortestPath(n,m) = 8n - 11 - 2 * (n - m + 1) if n >  m

Grinding that out a bit, it becomes pretty easy to compute
that numGrids with path len = prime^2 is:
  2 * ( (prime^2 - 13) / 24 + 1)

Congratulations, the answer you gave to problem 313 is correct.

You are the 1013th person to have solved this problem.


Answer     : 2057774861813004
Time Taken : 0.0258250236511

for prime in primes:
  count += 2 * ((prime**2 - 13) / 24 + 1)

"""
