import time
from math import sqrt
start = time.time()

squares = set([x**2 for x in xrange(1,100000)])

square_sum = dict()
for i in xrange(2,10000,2):
  for j in xrange(2,i,2):
    if i**2+j**2 in squares:
      if i**2+j**2 not in square_sum:
        square_sum[i**2+j**2] = [(i,j)]
      else:
        square_sum[i**2+j**2] += [(i,j)]

for i in square_sum.keys():
  if len(square_sum[i]) >1:
    print i, square_sum[i]


for values in square_sum.keys():
  if len(square_sum[values]) >= 2:
    lst = square_sum[values]
    for a in lst:
      if 2*a[0]*a[1] in square_sum:
        print a,square_sum[2*a[0]*a[1]]
        print lst

print "Time Taken: " + str(time.time()-start)


"""
a^2 = x+y
b^2 = x-y
c^2 = x+z
d^2 = x-z
e^2 = y+z
f^2 = y-z
a^2+b^2 = c^2+d^2
b^2+f^2 = d^2
b^2+e^2 = c^2
b^2+e^2+f^2 = a^2


OR

x+y = (n+a)^2
x-y = (n-a)^2
x = n^2 + a^2
y = 2an

y+z = (m+b)^2
y-z = (m-b)^2
y = m^2 + b^2
z = 2mb

x+z = (p+c)^2
x-z = (p-c)^2
x = p^2+c^2
z = 2pc

So from the previous statements...

x = n^2+a^2 = p^2+c^2
y = m^2+b^2 = 2an
z = 2mb = 2pc


"""
