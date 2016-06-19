import time, math
from primes import factor, m_r

START = time.time()
SIZE  = 10**11
LIM   = SIZE / 12101
MOD   = 2017
vals  = dict()

for n in sorted(range(1722, int(SIZE**(1/2.)), MOD) + range(294, int(SIZE**(1/2.)), MOD)):
  if n**2 > SIZE:
    break
  if m_r(n):
    vals[n] = 2

for n in sorted(range(1788, int(SIZE**(1/3.)), MOD) + range(229, int(SIZE**(1/3.)), MOD)):
  if n**3 > SIZE:
    break
  if m_r(n):
    vals[n] = 3

ansNum = 0
for n in xrange(MOD-1, SIZE, MOD):
  if m_r(n):
    if n > LIM:
      # don't bother storing large numbers, they won't run into the duplicate problem
      for j in xrange(1,SIZE/n+1):
        ansNum += j * n
    else:
      vals[n] = 1
print "Time Taken:", time.time() - START

answers = set()
for prime in vals:
  for j in xrange(1,SIZE/prime**vals[prime]+1):
    if j % prime == 0:
      continue
    answers.add(j * prime**vals[prime])
    
print sum(answers) + ansNum

print "Time Taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 565 is correct.
You are the 39th person to have solved this problem.


2992480851924313898
Time Taken: 332.678000212

(1+294+294^2) mod 2017 = (1+1722+1722^2) mod 2017 = 0
(1+229+229^2+229^3) mod 2017 = (1+1788+1788^2+1788^3) mod 2017 = 0


"""
