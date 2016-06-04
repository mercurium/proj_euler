import time, math
from primes import divisors, totient

START = time.time()
LIM   = 10**15

sumz  = 0
for m in xrange(2,20):
  for n in xrange(1,30):
    num_sum = 0
    for d in divisors(n):
      num_sum += totient(n/d) * math.factorial(m*d) / math.factorial(d)**m
    num_sum /= m*n
    if num_sum < LIM:
      sumz += num_sum
    else:
      break
  if n == 1:
    break

print "Answer:", sumz
print "Time Taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 281 is correct.

You are the 611th person to have solved this problem.


t(1,n) = 1
t(2,n) = OEIS series here: https://oeis.org/A003239
t(3,n) = OEIS series here: https://oeis.org/A118644


jchen@jchen-mbp 16:40:33 ~/Developer/proj_euler(master) % pypy prob281new.py
Answer: 1485776387445623
Time Taken: 0.00566101074219

...I don't really feel like I solved this. I used OEIS and that pretty much solved it for me...


"""
