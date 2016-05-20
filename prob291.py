import time, math
from primes import m_r

START = time.time()
LIM   = 10**5

"""
(x^4 - y^4) / (x^3 + y^3)
= ((x^2 + y^2)(x-y)(x+y)) / ((x+y)(x^2 - xy + y^2)
= stuff + (x^3 - x^2y + xy^2 - y^3) / (x^2 - xy + y^2)
= stuff + ( x(x^2 - xy + y^2) - y^3) / (x^2 - xy + y^2)
= stuff +  - y^3 / (x^2 - xy + y^2)

->
(x^2 - xy + y^2) | y^3

For now, assume:
  x^2 - xy + y^2 = y^3
Then:
  x = (y + y * sqrt(4y - 3)) / 2

"""

count = 0

for i in xrange(1, int(math.sqrt(LIM)), 2):
  for v in xrange(1,100):
    y = v * (i**2 + 3 ) / 4
    x = y * (1 + i) / (2*v)
    if x < y:
      continue
    if (x**4 - y**4) % (x**3 + y**3) != 0:
      # print x, y, (x**4 - y**4) % (x**3 + y**3), "ERROR"
      continue
    number = (x**4 - y**4) / (x**3 + y**3)
    if number > LIM:
      break
    if m_r(number):
      print number, x,y, v, x**4 - y**4, x**3 + y**3
      count += number

print "answer:", count
print "Time taken:", time.time() - START
