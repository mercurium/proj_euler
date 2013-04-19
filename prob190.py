import time
start = time.time()

"""
maxz,ma,mb = 0,0,0
for i in xrange(1,200):
  a,b = i/100.,(200-i)/100.
  if maxz < a * b *b: maxz,ma,mb = a*b*b,a,b
print maxz,ma,mb

maxz,ma,mb,mc = 0,0,0,0
for i in xrange(1,300):
  for j in xrange(1,300-i):
    a,b,c = i/100.,j/100.,(300-i-j)/100.
    if maxz < a * b *b* c**3: maxz,ma,mb,mc = a*b*b*c*c*c,a,b,c
print maxz,ma,mb,mc
"""

# 2/3, 4/3 = (2/3)^3 * 1 * 2^2
# 2/4, 4/4, 6/4 = (3/6)^6 * 1 * 2^2 * 3^3
# 4/10, 8/10, 12/10, 16/10 =(4/10)^10 * 1* 2^2 * 3^3 * 4^4

def tri(n): return n*(n+1)/2

sumz = 0
for a in xrange(2,16):
  prod = 1
  prod = (a*1./tri(a))**tri(a)
  for i in xrange(1,a+1):
    prod *= pow(i,i)
  print int(prod)
  sumz += int(prod)

print sumz

print "Time Taken:", time.time() - start
