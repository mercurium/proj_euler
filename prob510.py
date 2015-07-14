import time, math
START = time.time()
LIMIT = 10**9

def gcd(a,b):
  while b:
    a,b = b, a%b
  return a

def lcm(a,b):
  return a*b / gcd(a,b)


count = 0
for A in xrange(1,int(LIMIT**.25+1)):
  for B in xrange(1,A+1):
    if gcd(A,B) != 1: # exclude cases where C is smaller than it should be
      continue

    a = (A+B)**2 * A**2
    b = (A+B)**2 * B**2
    c = lcm(A,B) ** 2

    if a > LIMIT:
      break

    numTimes    = LIMIT / a
    tripletSum  = a+b+c
    count      += tripletSum * (numTimes * (numTimes +1)/2)

print "The answer is:", count
print "Time Taken:", time.time() - START


"""
How to figure out if a triplet (a,b,c) can form three circles for which the situation holds (all tangent)
Rules:
  -a,b, and c are squares
  -If a,b,c works, then so does ka, kb, kc for any positive integer k
  -If a,b,c works, and there is no such k such that k|a, k|b, and k|c, then c = lcm(a,b)/gcd(a,b)
  -If the ratio a/b = A^2/B^2, there exists an a,b,c where there are tangent circle with that a/b ratio
    - b = (A+B)^2 * B^2, a = b * ratio

Congratulations, the answer you gave to problem 510 is correct.

You are the 173rd person to have solved this problem.

The answer is: 315306518862563689
Time Taken: 0.0166640281677 


"""
