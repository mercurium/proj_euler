import time
START = time.time()

a = 10**5
b = 64

values = set()

#for i in [2,3,5,7,11,13,17,23,29,31,37,41,43,47,53]:
for i in xrange(1,b+1):
  oldLen = len(values)
  values.update(set([x*i for x in xrange(1,a+1)]))
  print i, len(values), len(values) - oldLen

print len(values)


"""
1: 100%
2: 50% (1/2)
3: 50% (1/3 + 1/3 (1-1/2)
4: 5/12 (1/2 + 1/4 (2/3)
5: 31/60
6: 11/30 (1/3 + (1/2 - 1/6) +

intersect (a,b) = 1/b, if b > a and gcd(a,b) = 1

"""
